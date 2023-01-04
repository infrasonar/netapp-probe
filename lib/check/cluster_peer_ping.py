from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['name'] = item['originating-node'] + '->' + item['destination-address']
    return item


async def check_cluster_peer_ping(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cluster-peer-ping-iter />')
    rows = flatten(tree)
    return {
        'ping': rows,
    }
