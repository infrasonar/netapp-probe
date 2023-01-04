from libprobe.asset import Asset
from ..netappquery import query_perf_objects, query_perf
from ..utils import flatten


async def check_uptime(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    tree = await query_perf_objects(
        asset, asset_config, check_config, 'system')

    names = [a['uuid'] for a in flatten(tree)]
    tree = await query_perf(
        asset, asset_config, check_config, 'system', ['uptime'], names)

    perf_items = []
    for result in tree:
        for instances in result:
            for instance in instances:
                uptime = int(instance[1][0][1].text)
                perf_items.append({'name': 'system', 'uptime': uptime})

    return {
        'uptime': perf_items
    }
