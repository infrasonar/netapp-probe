from libprobe.asset import Asset
from ..netappquery import query_perf_counters
from ..netappquery import query_perf_objects, query_perf
from ..utils import flatten, on_counterinfos


OBJECT_NAME = 'volume'
COUNTERS = (
    # GLOBAL
    'other_latency',
    'other_ops',
    'read_data',
    'read_latency',
    'read_ops',
    'write_data',
    'write_latency',
    'write_ops',
    'read_blocks',
    'write_blocks',
    'avg_latency',
    'total_ops',
    # CIFS
    'cifs_other_latency',
    'cifs_other_ops',
    'cifs_read_data',
    'cifs_read_latency',
    'cifs_read_ops',
    'cifs_write_data',
    'cifs_write_latency',
    'cifs_write_ops',
    # FCP
    'fcp_other_latency',
    'fcp_other_ops',
    'fcp_read_data',
    'fcp_read_latency',
    'fcp_read_ops',
    'fcp_write_data',
    'fcp_write_latency',
    'fcp_write_ops',
    # iSCSI
    'iscsi_other_latency',
    'iscsi_other_ops',
    'iscsi_read_data',
    'iscsi_read_latency',
    'iscsi_read_ops',
    'iscsi_write_data',
    'iscsi_write_latency',
    'iscsi_write_ops',
    # NFS
    'nfs_other_latency',
    'nfs_other_ops',
    'nfs_read_data',
    'nfs_read_latency',
    'nfs_read_ops',
    'nfs_write_data',
    'nfs_write_latency',
    'nfs_write_ops',
    # SAN
    'san_other_latency',
    'san_other_ops',
    'san_read_data',
    'san_read_latency',
    'san_read_ops',
    'san_write_data',
    'san_write_latency',
    'san_write_ops',
    # Misc
    'wv_fsinfo_blks_res_state',  # Space reservation state for the volume
    'wvsnap_ondisk_count',  # Total number of snapshots on the volume
    'wv_fsinfo_blks_snap_reserve_pct',  # Snap reserved percentage for the volume
)


async def check_volume_perf(
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
