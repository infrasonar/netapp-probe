from libprobe.asset import Asset
from . import query


async def check_cifs_options(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/protocols/cifs/services?fields=statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cifs_options': [{
            'comment': item.get('comment'),
            'default_unix_user': item.get('default_unix_user'),
            'enabled': item.get('enabled'),
            'group_policy_object_enabled': item.get('group_policy_object_enabled'),  # 9.12
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
            'metric_throughput_read': item.get('metric', {}).get('throughput', {}).get('read'),
            'metric_throughput_total': item.get('metric', {}).get('throughput', {}).get('total'),
            'metric_throughput_write': item.get('metric', {}).get('throughput', {}).get('write'),
            'metric_timestamp': item.get('metric', {}).get('timestamp'),  # 9.7
            'name': item.get('name'),
            'statistics_iops_raw_other': item.get('statistics', {}).get('iops_raw', {}).get('other'),
            'statistics_iops_raw_read': item.get('statistics', {}).get('iops_raw', {}).get('read'),
            'statistics_iops_raw_total': item.get('statistics', {}).get('iops_raw', {}).get('total'),
            'statistics_iops_raw_write': item.get('statistics', {}).get('iops_raw', {}).get('write'),
            'statistics_latency_raw_other': item.get('statistics', {}).get('latency_raw', {}).get('other'),
            'statistics_latency_raw_read': item.get('statistics', {}).get('latency_raw', {}).get('read'),
            'statistics_latency_raw_total': item.get('statistics', {}).get('latency_raw', {}).get('total'),
            'statistics_latency_raw_write': item.get('statistics', {}).get('latency_raw', {}).get('write'),
            'statistics_status': item.get('statistics', {}).get('status'),
            'statistics_throughput_raw_read': item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_total': item.get('statistics', {}).get('throughput_raw', {}).get('total'),
            'statistics_throughput_raw_write': item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'statistics_timestamp': item.get('statistics', {}).get('timestamp'),  # 9.7
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
        } for item in data['records']]
    }
