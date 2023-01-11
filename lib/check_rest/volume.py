from libprobe.asset import Asset
from . import query
from ..utils import datetime_to_ts


def space_percent_used(item: dict):
    available = item.get('space', {}).get('available')
    size = item.get('space', {}).get('size')
    try:
        return round((1 - available / size) * 100)
    except Exception:
        return None


async def check_volume(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/volumes?fields=autosize,space,statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'volume': [{
            'activity_tracking_state': item.get('activity_tracking', {}).get('state'),
            'activity_tracking_supported': item.get('activity_tracking', {}).get('supported'),  # 9.10
            'analytics_state': item.get('analytics', {}).get('state'),  # 9.8
            'autosize_mode': item.get('autosize', {}).get('mode'),
            'clone_is_flexclone': item.get('clone', {}).get('is_flexclone'),
            'cloud_retrieval_policy': item.get('cloud_retrieval_policy'),  # 9.8
            'comment': item.get('comment'),
            'create_time': datetime_to_ts(item.get('create_time')),
            'efficiency_state': item.get('efficiency', {}).get('state'),  # 9.9
            'efficiency_volume_path': item.get('efficiency', {}).get('volume_path'),
            'language': item.get('language'),
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
            'metric_timestamp': datetime_to_ts(item.get('metric', {}).get('timestamp')),
            'name': item.get('name'),
            'nas_export_policy_name': item.get('nas', {}).get('export_policy', {}).get('name'),
            'scheduled_snapshot_naming_scheme': item.get('scheduled_snapshot_naming_scheme'),
            'size': item.get('size'),
            'snapmirror_destinations_is_cloud': item.get('snapmirror', {}).get('destinations', {}).get('is_cloud'),
            'snapmirror_destinations_is_ontap': item.get('snapmirror', {}).get('destinations', {}).get('is_ontap'),
            'snapmirror_is_protected': item.get('snapmirror', {}).get('is_protected'),  # 9.7
            'snapshot_count': item.get('snapshot_count'),  # 9.10
            'snapshot_policy_name': item.get('snapshot_policy', {}).get('name'),
            'space_afs_total': item.get('space', {}).get('afs_total'),
            'space_available': item.get('space', {}).get('available'),
            'space_percent_used': space_percent_used(item),
            'space_size': item.get('space', {}).get('size'),
            'space_size_available_for_snapshots': item.get('space', {}).get('size_available_for_snapshots'),
            'space_snapshot_reserve_size': item.get('space', {}).get('snapshot', {}).get('reserve_size'),
            'space_used': item.get('space', {}).get('used'),
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
            'statistics_timestamp': datetime_to_ts(item.get('statistics', {}).get('timestamp')),
            'style': item.get('style'),
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
            'tiering_policy': item.get('tiering', {}).get('policy'),
            'type': item.get('type'),
            'uuid': item.get('uuid'),
        } for item in data['records']]
    }
