from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    # TODO waarom zo veel metrics in de itemnaam?
    item['name'] = (item['owner'] + '/' + item['package'] if 'owner' in item else item['package']) + \
        '/' + item['serial-number'] if 'serial-number' in item else ''
    return item


async def check_license_v2(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<license-v2-list-info />')
    rows = flatten(tree, on_item)
    return {
        'license': rows,
    }
