from libprobe.asset import Asset
from . import query


async def check_cifs_options(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/protocols/cifs/services?fields=statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cifs_options': [{
            'name': item['name'],
            # TODO metrics
        } for item in data['records']]
    }
