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
            'block_storage_hybrid_cache_enabled': item['block_storage']['hybrid_cache']['enabled'],
            'block_storage_mirror_enabled': item['block_storage']['mirror']['enabled'],
            'block_storage_mirror_state': item['block_storage']['mirror']['state'],
            'block_storage_primary_checksum_style': item['block_storage']['primary']['checksum_style'],
            'block_storage_primary_disk_class': item['block_storage']['primary']['disk_class'],
            'block_storage_primary_disk_count': item['block_storage']['primary']['disk_count'],
            'block_storage_primary_disk_type': item['block_storage']['primary'].get('disk_type'),  # 9.7
            'block_storage_primary_raid_size': item['block_storage']['primary']['raid_size'],
            'block_storage_primary_raid_type': item['block_storage']['primary']['raid_type'],
            'cloud_storage_attach_eligible': item['cloud_storage']['attach_eligible'],
            'create_time': item['create_time'],
            'data_encryption_drive_protection_enabled': item['data_encryption']['drive_protection_enabled'],
            'data_encryption_software_encryption_enabled': item['data_encryption']['software_encryption_enabled'],
            'home_node_name': item['home_node']['name'],
            'home_node_uuid': item['home_node']['uuid'],
            **({'inactive_data_reporting_enabled': item['inactive_data_reporting']['enabled'], } if 'inactive_data_reporting' in item else {}),  # 9.8
            **({'metric_duration': item['metric']['duration'],
                'metric_iops_other': item['metric']['iops']['other'],
                'metric_iops_read': item['metric']['iops']['read'],
                'metric_iops_total': item['metric']['iops']['total'],
                'metric_iops_write': item['metric']['iops']['write'],
                'metric_latency_other': item['metric']['latency']['other'],
                'metric_latency_read': item['metric']['latency']['read'],
                'metric_latency_total': item['metric']['latency']['total'],
                'metric_latency_write': item['metric']['latency']['write'],
                'metric_status': item['metric']['status'],
                'metric_throughput_other': item['metric']['throughput']['other'],
                'metric_throughput_read': item['metric']['throughput']['read'],
                'metric_throughput_total': item['metric']['throughput']['total'],
                'metric_throughput_write': item['metric']['throughput']['write'],
                'metric_timestamp': item['metric']['timestamp'], } if 'metric' in item else {}),  # 9.7
            'name': item['name'],
            'node_name': item['node']['name'],
            'node_uuid': item['node']['uuid'],
            'snaplock_type': item['snaplock_type'],
            **({'snapshot_files_total': item['snapshot']['files_total'],
                'snapshot_files_used': item['snapshot']['files_used'],
                'snapshot_max_files_available': item['snapshot']['max_files_available'],
                'snapshot_max_files_used': item['snapshot']['max_files_used'], } if 'snapshot' in item else {}),  # 9.10
            'space_block_storage_available': item['space']['block_storage']['available'],
            'space_block_storage_data_compacted_count': item['space']['block_storage'].get('data_compacted_count'),  # 9.10
            'space_block_storage_data_compaction_space_saved': item['space']['block_storage'].get('data_compaction_space_saved'),  # 9.10
            'space_block_storage_data_compaction_space_saved_percent': item['space']['block_storage'].get('data_compaction_space_saved_percent'),  # 9.10
            'space_block_storage_full_threshold_percent': item['space']['block_storage']['full_threshold_percent'],
            'space_block_storage_physical_used': item['space']['block_storage'].get('physical_used'),  # 9.9
            'space_block_storage_physical_used_percent': item['space']['block_storage'].get('physical_used_percent'),  # 9.10
            'space_block_storage_size': item['space']['block_storage']['size'],
            'space_block_storage_used': item['space']['block_storage']['used'],
            'space_block_storage_volume_deduplication_shared_count': item['space']['block_storage'].get('volume_deduplication_shared_count'),  # 9.10
            'space_block_storage_volume_deduplication_space_saved': item['space']['block_storage'].get('volume_deduplication_space_saved'),  # 9.10
            'space_block_storage_volume_deduplication_space_saved_percent': item['space']['block_storage'].get('volume_deduplication_space_saved_percent'),  # 9.10
            'space_cloud_storage_used': item['space']['cloud_storage']['used'],
            'space_efficiency_logical_used': item['space']['efficiency']['logical_used'],
            'space_efficiency_ratio': float(item['space']['efficiency']['ratio']),
            'space_efficiency_savings': item['space']['efficiency']['savings'],
            'space_efficiency_without_snapshots_logical_used': item['space']['efficiency_without_snapshots']['logical_used'],
            'space_efficiency_without_snapshots_ratio': item['space']['efficiency_without_snapshots']['ratio'],
            'space_efficiency_without_snapshots_savings': item['space']['efficiency_without_snapshots']['savings'],
            **({'space_efficiency_without_snapshots_flexclones_logical_used': item['space']['efficiency_without_snapshots_flexclones']['logical_used'],
                'space_efficiency_without_snapshots_flexclones_ratio': item['space']['efficiency_without_snapshots_flexclones']['ratio'],
                'space_efficiency_without_snapshots_flexclones_savings': item['space']['efficiency_without_snapshots_flexclones']['savings'], } if 'efficiency_without_snapshots_flexclones' in item['space'] else {}),  # 9.9
            # 'space_snapshot_available': item['space']['snapshot'].get('available'),  # 9.10
            # 'space_snapshot_reserve_percent': item['space']['snapshot']['reserve_percent'],
            # 'space_snapshot_total': item['space']['snapshot'].get('total'),  # 9.10
            # 'space_snapshot_used': item['space']['snapshot']['used'],
            # 'space_snapshot_used_percent': item['space']['snapshot'].get('used_percent'),  # 9.10
            'state': item['state'],
            **({'statistics_iops_raw_other': item['statistics']['iops_raw']['other'],
                'statistics_iops_raw_read': item['statistics']['iops_raw']['read'],
                'statistics_iops_raw_total': item['statistics']['iops_raw']['total'],
                'statistics_iops_raw_write': item['statistics']['iops_raw']['write'],
                'statistics_latency_raw_other': item['statistics']['latency_raw']['other'],
                'statistics_latency_raw_read': item['statistics']['latency_raw']['read'],
                'statistics_latency_raw_total': item['statistics']['latency_raw']['total'],
                'statistics_latency_raw_write': item['statistics']['latency_raw']['write'],
                'statistics_status': item['statistics']['status'],
                'statistics_throughput_raw_other': item['statistics']['throughput_raw']['other'],
                'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
                'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
                'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
                'statistics_timestamp': item['statistics']['timestamp'], } if 'statistics' in item else {}),  # 9.7
            'uuid': item['uuid'],
        } for item in data['records']],
    }
