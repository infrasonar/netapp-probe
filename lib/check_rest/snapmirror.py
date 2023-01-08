from libprobe.asset import Asset
from . import query


async def check_snapmirror(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/snapmirror/relationships?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'snapmirror': [{
            'name': item['name'],
            # TODO metrics
        } for item in data['records']]
    }
