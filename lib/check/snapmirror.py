from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['destination-volume']
    return item


async def check_snapmirror(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<snapmirror-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'snapmirror': rows,
    }
