import aiohttp
import base64
from libprobe.asset import Asset
from typing import List, Dict


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        route: str) -> List[Dict]:

    address = check_config.get('address')
    if not address:
        address = asset.name
    assert asset_config, 'missing credentials'
    username = asset_config['username']
    password = asset_config['password']

    url = f'{address}/{route}'

    auth_str = base64.encodebytes(
        f'{username}:{password}'.encode()).decode().replace('\n', '')
    headers = {
        'authorization': f'Basic {auth_str}',
        'content-type': 'application/json',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url,
                               headers=headers,
                               ssl=False) as resp:
            data = await resp.json()
            return data
