from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['vserver'].lower() + '/' + str(item['share-name'])
    return item


async def check_cifs(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cifs-share-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'cifs': rows,
    }
