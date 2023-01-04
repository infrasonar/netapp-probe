from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['node-name']
    return item


async def check_cluster_node(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cluster-node-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'cluster_node': rows,
    }
