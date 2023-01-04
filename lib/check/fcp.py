from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['port-name']
    return item


async def check_fcp(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<fcp-adapter-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'fcp': rows,
    }
