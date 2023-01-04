from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['volume'] + '/' + str(item['id'])
    if 'vserver' in item:
        item['name'] = item['vserver'] + '/' + item['name']
    return item


async def check_qtree(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<qtree-list-iter />')
    rows = flatten(tree, on_item)
    return {
        'qtree': rows,
    }
