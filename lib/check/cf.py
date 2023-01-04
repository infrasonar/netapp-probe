from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['sfo-node-info-node-related-info-node']
    return item


async def check_cf(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cf-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'cf': rows,
    }
