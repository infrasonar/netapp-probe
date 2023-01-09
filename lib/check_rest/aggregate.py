from libprobe.asset import Asset
from . import query


async def check_aggregate(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/aggregates?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'aggregate': [{
            'block_storage_hybrid_cache_enabled': item.get('block_storage', {}).get('hybrid_cache', {}).get('enabled'),
            'block_storage_mirror_enabled': item.get('block_storage', {}).get('mirror', {}).get('enabled'),
            'block_storage_mirror_state': item.get('block_storage', {}).get('mirror', {}).get('state'),
            'block_storage_primary_checksum_style': item.get('block_storage', {}).get('primary', {}).get('checksum_style'),
            'block_storage_primary_disk_class': item.get('block_storage', {}).get('primary', {}).get('disk_class'),
            'block_storage_primary_disk_count': item.get('block_storage', {}).get('primary', {}).get('disk_count'),
            'block_storage_primary_disk_type': item.get('block_storage', {}).get('primary', {}).get('disk_type'),  # 9.7
            'block_storage_primary_raid_size': item.get('block_storage', {}).get('primary', {}).get('raid_size'),
            'block_storage_primary_raid_type': item.get('block_storage', {}).get('primary', {}).get('raid_type'),
            'cloud_storage_attach_eligible': item.get('cloud_storage', {}).get('attach_eligible'),
            'create_time': item.get('create_time'),
            'data_encryption_drive_protection_enabled': item.get('data_encryption', {}).get('drive_protection_enabled'),
            'data_encryption_software_encryption_enabled': item.get('data_encryption', {}).get('software_encryption_enabled'),
            'home_node_name': item.get('home_node', {}).get('name'),
            'home_node_uuid': item.get('home_node', {}).get('uuid'),
            'inactive_data_reporting_enabled': item.get('inactive_data_reporting', {}).get('enabled'),  # 9.8
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
            'name': item.get('name'),
            'node_name': item.get('node', {}).get('name'),
            'node_uuid': item.get('node', {}).get('uuid'),
            'snaplock_type': item.get('snaplock_type'),
            'snapshot_files_total': item.get('snapshot', {}).get('files_total'),
            'snapshot_files_used': item.get('snapshot', {}).get('files_used'),
            'snapshot_max_files_available': item.get('snapshot', {}).get('max_files_available'),
            'snapshot_max_files_used': item.get('snapshot', {}).get('max_files_used'),  # 9.10
            'space_block_storage_available': item.get('space', {}).get('block_storage', {}).get('available'),
            'space_block_storage_data_compacted_count': item.get('space', {}).get('block_storage', {}).get('data_compacted_count'),  # 9.10
            'space_block_storage_data_compaction_space_saved': item.get('space', {}).get('block_storage', {}).get('data_compaction_space_saved'),  # 9.10
            'space_block_storage_data_compaction_space_saved_percent': item.get('space', {}).get('block_storage', {}).get('data_compaction_space_saved_percent'),  # 9.10
            'space_block_storage_full_threshold_percent': item.get('space', {}).get('block_storage', {}).get('full_threshold_percent'),
            'space_block_storage_physical_used': item.get('space', {}).get('block_storage', {}).get('physical_used'),  # 9.9
            'space_block_storage_physical_used_percent': item.get('space', {}).get('block_storage', {}).get('physical_used_percent'),  # 9.10
            'space_block_storage_size': item.get('space', {}).get('block_storage', {}).get('size'),
            'space_block_storage_used': item.get('space', {}).get('block_storage', {}).get('used'),
            'space_block_storage_volume_deduplication_shared_count': item.get('space', {}).get('block_storage', {}).get('volume_deduplication_shared_count'),  # 9.10
            'space_block_storage_volume_deduplication_space_saved': item.get('space', {}).get('block_storage', {}).get('volume_deduplication_space_saved'),  # 9.10
            'space_block_storage_volume_deduplication_space_saved_percent': item.get('space', {}).get('block_storage', {}).get('volume_deduplication_space_saved_percent'),  # 9.10
            'space_cloud_storage_used': item.get('space', {}).get('cloud_storage', {}).get('used'),
            'space_efficiency_logical_used': item.get('space', {}).get('efficiency', {}).get('logical_used'),
            'space_efficiency_ratio': float(item.get('space', {}).get('efficiency', {}).get('ratio')),
            'space_efficiency_savings': item.get('space', {}).get('efficiency', {}).get('savings'),
            'space_efficiency_without_snapshots_logical_used': item.get('space', {}).get('efficiency_without_snapshots', {}).get('logical_used'),
            'space_efficiency_without_snapshots_ratio': item.get('space', {}).get('efficiency_without_snapshots', {}).get('ratio'),
            'space_efficiency_without_snapshots_savings': item.get('space', {}).get('efficiency_without_snapshots', {}).get('savings'),
            'space_efficiency_without_snapshots_flexclones_logical_used': item.get('space', {}).get('efficiency_without_snapshots_flexclones', {}).get('logical_used'),
            'space_efficiency_without_snapshots_flexclones_ratio': item.get('space', {}).get('efficiency_without_snapshots_flexclones', {}).get('ratio'),
            'space_efficiency_without_snapshots_flexclones_savings': item.get('space', {}).get('efficiency_without_snapshots_flexclones', {}).get('savings'),  # 9.9
            'space_snapshot_available': item.get('space', {}).get('snapshot', {}).get('available'),  # 9.10
            'space_snapshot_reserve_percent': item.get('space', {}).get('snapshot', {}).get('reserve_percent'),
            'space_snapshot_total': item.get('space', {}).get('snapshot', {}).get('total'),  # 9.10
            'space_snapshot_used': item.get('space', {}).get('snapshot', {}).get('used'),
            'space_snapshot_used_percent': item.get('space', {}).get('snapshot', {}).get('used_percent'),  # 9.10
            'state': item.get('state'),
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
            'uuid': item.get('uuid'),
        } for item in data['records']],
    }
