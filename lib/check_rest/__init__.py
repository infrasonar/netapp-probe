import aiohttp
import base64
import logging
from libprobe.asset import Asset
from libprobe.exceptions import IgnoreResultException
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
        'content-type': 'application/json',
        'accept': 'application/json',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url,
                               headers=headers,
                               ssl=False) as resp:
            # disable content-type check becuase not sure if this is always
            # iso-8859-1
            data = await resp.json(content_type=None)
            return data
