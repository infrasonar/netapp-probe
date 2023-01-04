from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


# TODO
def on_item(item: dict) -> dict:
    item['name'] = item['disk-uid']
    return item


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<storage-disk-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'disk': rows,
    }
