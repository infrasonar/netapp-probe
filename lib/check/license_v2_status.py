from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['package']
    return item


async def check_license_v2_status(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<license-v2-status-list-info />')
    rows = flatten(tree, on_item)
    return {
        'license': rows,
    }
