from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['vserver'].lower() + '/' + item['interface-name']
    return item


async def check_interface(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<net-interface-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'interface': rows,
    }
