from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten_one


async def check_ontapi_version(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<system-get-ontapi-version />')
    item = flatten_one(tree)
    item['name'] = 'apiversion'
    return {
        'apiversion': [item],
    }
