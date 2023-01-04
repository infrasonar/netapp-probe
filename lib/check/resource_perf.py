from libprobe.asset import Asset
from ..netappquery import query_perf_counters
from ..netappquery import query_perf_objects, query_perf
from ..utils import flatten, on_counterinfos


OBJECT_NAME = 'resource'
COUNTERS = (
    'busy_percent',
    'cpu_elapsed_time',
)


async def check_resource_perf(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    tree = await query_perf_counters(
        asset, asset_config, check_config, OBJECT_NAME)
    counterinfos = {a['name']: a for a in flatten(tree)}

    tree = await query_perf_objects(
        asset, asset_config, check_config, OBJECT_NAME)

    names = [a['uuid'] for a in flatten(tree)]
    tree = await query_perf(
        asset, asset_config, check_config, OBJECT_NAME, COUNTERS, names)

    perf_items = []
    for result in tree:
        for instances in result:
            for instance in instances:
                item = {'name': instance[1].text}
                for ct in instance[0]:
                    item[ct[0].text] = int(ct[1].text)
                perf_items.append(item)
                on_counterinfos(item, counterinfos)

    return {
        OBJECT_NAME: perf_items
    }
