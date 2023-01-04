from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['node']
    return item


async def check_system_health(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<system-node-get-iter />')

    # TODO
    rows = flatten(tree, on_item)
    return {
        'systemNodes': rows,
    }
