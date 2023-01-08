from libprobe.asset import Asset
from . import query


async def check_volume(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/volumes?fields=statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'volume': [{
            **({'activity_tracking_state': item['activity_tracking']['state'],
                'activity_tracking_supported': item['activity_tracking']['supported'], } if 'activity_tracking' in item else {}),  # 9.10
            **({'analytics_state': item['analytics']['state'], } if 'analytics' in item else {}),  # 9.8
            'clone_is_flexclone': item['clone']['is_flexclone'],
            'cloud_retrieval_policy': item.get('cloud_retrieval_policy'),  # 9.8
            'comment': item['comment'],
            'create_time': item['create_time'],
            # 'efficiency_state': item['efficiency'].get('state'),  # 9.9
            # 'efficiency_volume_path': item['efficiency']['volume_path'],
            'language': item['language'],
            'metric_duration': item['metric']['duration'],
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
            'metric_timestamp': item['metric']['timestamp'],
            'name': item['name'],
            'nas_export_policy_name': item['nas']['export_policy']['name'],
            'scheduled_snapshot_naming_scheme': item['scheduled_snapshot_naming_scheme'],
            'size': item['size'],
            **({'snapmirror_destinations_is_cloud': item['snapmirror']['destinations']['is_cloud'],
                'snapmirror_destinations_is_ontap': item['snapmirror']['destinations']['is_ontap'],
                'snapmirror_is_protected': item['snapmirror']['is_protected'], } if 'snapmirror' in item else {}),  # 9.7
            'snapshot_count': item.get('snapshot_count'),  # 9.10
            'snapshot_policy_name': item['snapshot_policy']['name'],
            'space_available': item['space']['available'],
            'space_size': item['space']['size'],
            'space_used': item['space']['used'],
            'state': item['state'],
            'statistics_iops_raw_other': item['statistics']['iops_raw']['other'],
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
            'statistics_timestamp': item['statistics']['timestamp'],
            'style': item['style'],
            'svm_name': item['svm']['name'],
            'svm_uuid': item['svm']['uuid'],
            'tiering_policy': item['tiering']['policy'],
            'type': item['type'],
            'uuid': item['uuid'],
        } for item in data['records']]
    }
