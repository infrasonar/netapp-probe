from libprobe.asset import Asset
from . import query


async def check_cluster_peer(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/cluster/peers?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cluster_peer': [{
            # TODO metrics
        } for item in data['records']]
    }
