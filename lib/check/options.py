from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['key'] = item['name']
    if 'vserver' in item:
        # cluster mode
        item['name'] = item['vserver'].lower() + '/' + item['name']
    return item


async def check_options(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<options-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'options': rows,
    }
