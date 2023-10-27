from libprobe.asset import Asset
from ..netappquery import query


async def check_disk_wear(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    url = '/api/private/cli/storage/disk/show?ssd-wear=true'
    data = await query(asset, asset_config, check_config, url)
    return data
