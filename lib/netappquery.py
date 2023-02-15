import aiohttp
import base64
import logging
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreResultException, CheckException
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
        logging.error(f'missing credentails for {asset}')
        raise IgnoreResultException

    url = f'https://{address}{route}'

    auth_str = base64.encodebytes(
        f'{username}:{password}'.encode()).decode().replace('\n', '')
    headers = {
        'authorization': f'Basic {auth_str}',
        'accept': 'application/hal+json',
    }

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
                    f'failed to read response: {resp.reason} ({resp.status})')
            return data
