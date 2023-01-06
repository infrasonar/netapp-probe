from libprobe.asset import Asset
from . import query


async def check_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/luns?fields=statistics,metric,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'lun': [{
            # TODO metrics
        } for item in data['records']]
    }
