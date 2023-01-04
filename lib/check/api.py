from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


async def check_api(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<system-api-list />')
    rows = flatten(tree)
    return {
        'apicall': rows,
    }
