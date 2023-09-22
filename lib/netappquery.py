import aiohttp
import base64
import logging
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from typing import List, Dict


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        route: str) -> List[Dict]:

    address = check_config.get('address')
    if not address:
        address = asset.name
    username = asset_config.get('username')
    password = asset_config.get('password')
    if None in (username, password):
        raise CheckException('missing credentials')

    url = f'https://{address}{route}'

    auth_str = base64.encodebytes(
        f'{username}:{password}'.encode()).decode().replace('\n', '')
    headers = {
        'authorization': f'Basic {auth_str}',
        'accept': 'application/hal+json',
    }

    # Pagination
    #
    # See: https://library.netapp.com/ecmdocs/ECMLP2856304/html/index.html
    #
    # All calls to GET on a resource collection allow you to page through
    # the results. If the max_records parameter is not specified, the cluster
    # returns as many records as possible within the return_timeout time
    # threshold. The number of records returned can be further limited by
    # specifying a value for the max_records parameter. When the operation
    # reaches either the return_timeout or the max_records threshold,
    # it stops and returns the records as well as a HAL link that can be used
    # to get the next page of records. It is possible for a pagination
    # link to be returned even if there are no additional records.
    # This occurs because the cluster does not check if there is an additional
    # record before returning when it reaches a threshold. When there are
    # potentially additional records, the response header will also
    # contain a Link header containing the link followed by rel="next".
    #
    # Best for the probe:
    #   keep the defaults (no max and 15 seconds timeout) and implement
    #   pagination.

    records = []  # used for pagination when applicable

    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,
                                   headers=headers,
                                   ssl=False) as resp:
                # we use strict content_type hal+json
                # 400 exeptions will fail this check
                if resp.ok:  # status < 400
                    data = await resp.json(content_type='application/hal+json')
                else:
                    raise CheckException(
                        'failed to read response: '
                        f'{resp.reason} ({resp.status})')

        if 'records' in data:
            records.extend(data['records'])
            try:
                next = data['_links']['next']['href']
                assert next
            except Exception:
                data['records'] = records
                return data

            # next batch of records
            url = f'https://{address}{next}'
        else:
            return data
