from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['system-id']
    return item


async def check_system_node(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<system-get-node-info-iter />')
    rows = flatten(tree, on_item)
    return {
        'system_node': rows,
    }
