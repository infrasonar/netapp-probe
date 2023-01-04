from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    # TODO waarom niet gewoon node:port?
    item['name'] = item['port'] + '-' + item['node'] + ':kernel:' + str(item['port'])
    return item


async def check_interface_ports(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<net-port-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'port': rows,
    }
