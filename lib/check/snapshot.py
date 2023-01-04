from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['snapshotName'] = item['name']
    item['name'] = item['vserver'].lower() + '/' + item['volume'] + ' ' + item['name']
    return item


async def check_snapshot(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<snapshot-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'snapshot': rows,
    }
