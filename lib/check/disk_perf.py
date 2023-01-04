from libprobe.asset import Asset
from ..netappquery import query_perf_counters
from ..netappquery import query_perf_objects, query_perf
from ..utils import flatten, on_counterinfos


# TODO samenvoegen met check_disk zoals vroeger?
OBJECT_NAME = 'disk'
COUNTERS = (
    'base_for_disk_busy',
    'cp_read_blocks',
    'cp_read_latency',
    'cp_write_latency',
    'disk_busy',
    # 'disk_io_latency_histogram',  # TODO list_int
    # 'dlsched_count',  # TODO list_int
    'dlsched_qtime',
    # 'dlsched_wait',  # TODO list_int
    'guaranteed_read_blocks',
    'guaranteed_read_latency',
    'guaranteed_write_blocks',
    'guaranteed_write_latency',
    'io_pending',
    'io_queued',
    'operation_latency',
    'read_data',
    'total_data',
    'total_transfers',
    'user_read_blocks',
    'user_read_latency',
    'user_write_blocks',
    'user_write_latency',
    'write_data',
)


async def check_disk_perf(
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
                item = {'name': instance[2].text}
                for ct in instance[1]:
                    item[ct[0].text] = int(ct[1].text)
                perf_items.append(item)
                on_counterinfos(item, counterinfos)

    return {
        OBJECT_NAME: perf_items
    }
