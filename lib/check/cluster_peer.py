from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


async def check_cluster_peer(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cluster-peer-get-iter />')
    rows = flatten(tree)  # TODO name
    return {
        'cluster_peer': rows,
    }
