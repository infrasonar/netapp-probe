from libprobe.asset import Asset
from . import query


async def check_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/luns?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'lun': [{
            'auto_delete': item.get('auto_delete'),
            'class': item.get('class'),
            'clone_source_name': item.get('clone', {}).get('source', {}).get('name'),
            'clone_source_uuid': item.get('clone', {}).get('source', {}).get('uuid'),
            'comment': item.get('comment'),
            'consistency_group_name': item.get('consistency_group', {}).get('name'),
            'consistency_group_uuid': item.get('consistency_group', {}).get('uuid'),  # 9.10
            'convert_namespace_name': item.get('convert', {}).get('namespace', {}).get('name'),
            'convert_namespace_uuid': item.get('convert', {}).get('namespace', {}).get('uuid'),  # 9.11
            'copy_source_max_throughput': item.get('copy', {}).get('source', {}).get('max_throughput'),
            'copy_source_name': item.get('copy', {}).get('source', {}).get('name'),
            'copy_source_progress_elapsed': item.get('copy', {}).get('source', {}).get('progress', {}).get('elapsed'),
            'copy_source_progress_percent_complete': item.get('copy', {}).get('source', {}).get('progress', {}).get('percent_complete'),
            'copy_source_progress_state': item.get('copy', {}).get('source', {}).get('progress', {}).get('state'),
            'copy_source_progress_volume_snapshot_blocked': item.get('copy', {}).get('source', {}).get('progress', {}).get('volume_snapshot_blocked'),
            'copy_source_uuid': item.get('copy', {}).get('source', {}).get('uuid'),  # 9.10
            'create_time': item.get('create_time'),  # 9.7
            'enabled': item.get('enabled'),
            'location_logical_unit': item.get('location', {}).get('logical_unit'),
            'location_node_name': item.get('location', {}).get('node', {}).get('name'),
            'location_node_uuid': item.get('location', {}).get('node', {}).get('uuid'),
            'location_qtree_id': item.get('location', {}).get('qtree', {}).get('id'),
            'location_qtree_name': item.get('location', {}).get('qtree', {}).get('name'),
            'location_volume_name': item.get('location', {}).get('volume', {}).get('name'),
            'location_volume_uuid': item.get('location', {}).get('volume', {}).get('uuid'),
            'metric_duration': item.get('metric', {}).get('duration'),
            'metric_iops_other': item.get('metric', {}).get('iops', {}).get('other'),
            'metric_iops_read': item.get('metric', {}).get('iops', {}).get('read'),
            'metric_iops_total': item.get('metric', {}).get('iops', {}).get('total'),
            'metric_iops_write': item.get('metric', {}).get('iops', {}).get('write'),
            'metric_latency_other': item.get('metric', {}).get('latency', {}).get('other'),
            'metric_latency_read': item.get('metric', {}).get('latency', {}).get('read'),
            'metric_latency_total': item.get('metric', {}).get('latency', {}).get('total'),
            'metric_latency_write': item.get('metric', {}).get('latency', {}).get('write'),
            'metric_status': item.get('metric', {}).get('status'),
            'metric_throughput_other': item.get('metric', {}).get('throughput', {}).get('other'),
            'metric_throughput_read': item.get('metric', {}).get('throughput', {}).get('read'),
            'metric_throughput_total': item.get('metric', {}).get('throughput', {}).get('total'),
            'metric_throughput_write': item.get('metric', {}).get('throughput', {}).get('write'),
            'metric_timestamp': item.get('metric', {}).get('timestamp'),  # 9.7
            'movement_max_throughput': item.get('movement', {}).get('max_throughput'),
            'movement_paths_destination': item.get('movement', {}).get('paths', {}).get('destination'),
            'movement_paths_source': item.get('movement', {}).get('paths', {}).get('source'),
            'movement_progress_elapsed': item.get('movement', {}).get('progress', {}).get('elapsed'),
            'movement_progress_percent_complete': item.get('movement', {}).get('progress', {}).get('percent_complete'),
            'movement_progress_state': item.get('movement', {}).get('progress', {}).get('state'),
            'movement_progress_volume_snapshot_blocked': item.get('movement', {}).get('progress', {}).get('volume_snapshot_blocked'),
            'name': item.get('name'),
            'os_type': item.get('os_type'),
            'qos_policy_name': item.get('qos_policy', {}).get('name'),
            'qos_policy_uuid': item.get('qos_policy', {}).get('uuid'),
            'serial_number': item.get('serial_number'),
            'space_guarantee_requested': item.get('space', {}).get('guarantee', {}).get('requested'),
            'space_guarantee_reserved': item.get('space', {}).get('guarantee', {}).get('reserved'),
            'space_scsi_thin_provisioning_support_enabled': item.get('space', {}).get('scsi_thin_provisioning_support_enabled'),
            'space_size': item.get('space', {}).get('size'),
            'space_used': item.get('space', {}).get('used'),
            'statistics_iops_raw_other': item.get('statistics', {}).get('iops_raw', {}).get('other'),
            'statistics_iops_raw_read': item.get('statistics', {}).get('iops_raw', {}).get('read'),
            'statistics_iops_raw_total': item.get('statistics', {}).get('iops_raw', {}).get('total'),
            'statistics_iops_raw_write': item.get('statistics', {}).get('iops_raw', {}).get('write'),
            'statistics_latency_raw_other': item.get('statistics', {}).get('latency_raw', {}).get('other'),
            'statistics_latency_raw_read': item.get('statistics', {}).get('latency_raw', {}).get('read'),
            'statistics_latency_raw_total': item.get('statistics', {}).get('latency_raw', {}).get('total'),
            'statistics_latency_raw_write': item.get('statistics', {}).get('latency_raw', {}).get('write'),
            'statistics_status': item.get('statistics', {}).get('status'),
            'statistics_throughput_raw_other': item.get('statistics', {}).get('throughput_raw', {}).get('other'),
            'statistics_throughput_raw_read': item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_total': item.get('statistics', {}).get('throughput_raw', {}).get('total'),
            'statistics_throughput_raw_write': item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'statistics_timestamp': item.get('statistics', {}).get('timestamp'),  # 9.7
            'status_container_state': item.get('status', {}).get('container_state'),
            'status_mapped': item.get('status', {}).get('mapped'),
            'status_read_only': item.get('status', {}).get('read_only'),
            'status_state': item.get('status', {}).get('state'),
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
            'uuid': item.get('uuid'),
            'vvol_is_bound': item.get('vvol', {}).get('is_bound'),  # 9.10
        } for item in data['records']]
    }
