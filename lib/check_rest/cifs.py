from libprobe.asset import Asset
from . import query


async def check_cifs(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/protocols/cifs/shares?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cifs': [{
            'name': item['name'],
            # TODO metrics
        } for item in data['records']]
    }
