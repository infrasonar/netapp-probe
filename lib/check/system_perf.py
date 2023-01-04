from libprobe.asset import Asset
from ..netappquery import query_perf_counters
from ..netappquery import query_perf_objects, query_perf
from ..utils import flatten, on_counterinfos


OBJECT_NAME = 'system'
COUNTERS = (
    'disk_data_written',
    'read_ops',
    'total_processor_busy',
    'http_ops',
    'hdd_data_written',
    'num_processors',
    'hdd_data_read',
    'ssd_data_written',
    'nfs_ops',
    'net_data_recv',
    'system_id',
    'fcp_data_recv',
    'cpu_busy',
    'ssd_data_read',
    'disk_data_read',
    'total_ops',
    # TODO 'process_name',
    'net_data_sent',
    'write_ops',
    'iscsi_ops',
    'fcp_ops',
    'fcp_data_sent',
    # TODO 'node_name',
    'time',
    'cifs_ops',
    'avg_processor_busy',
    'cpu_elapsed_time2',
    'cpu_elapsed_time1',
    'cpu_elapsed_time',
)


async def check_system_perf(
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
