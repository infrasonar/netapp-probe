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
            'comment': item['comment'],
            'default_unix_user': item['default_unix_user'],
            'enabled': item['enabled'],
            'group_policy_object_enabled': item.get('group_policy_object_enabled'),  # 9.12
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
                'metric_throughput_read': item['metric']['throughput']['read'],
                'metric_throughput_total': item['metric']['throughput']['total'],
                'metric_throughput_write': item['metric']['throughput']['write'],
                'metric_timestamp': item['metric']['timestamp'], } if 'metric' in item else {}),  # 9.7
            'name': item['name'],
            **({'statistics_iops_raw_other': item['statistics']['iops_raw']['other'],
                'statistics_iops_raw_read': item['statistics']['iops_raw']['read'],
                'statistics_iops_raw_total': item['statistics']['iops_raw']['total'],
                'statistics_iops_raw_write': item['statistics']['iops_raw']['write'],
                'statistics_latency_raw_other': item['statistics']['latency_raw']['other'],
                'statistics_latency_raw_read': item['statistics']['latency_raw']['read'],
                'statistics_latency_raw_total': item['statistics']['latency_raw']['total'],
                'statistics_latency_raw_write': item['statistics']['latency_raw']['write'],
                'statistics_status': item['statistics']['status'],
                'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
                'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
                'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
                'statistics_timestamp': item['statistics']['timestamp'], } if 'statistics' in item else {}),  # 9.7
            'svm_name': item['svm']['name'],
            'svm_uuid': item['svm']['uuid'],
        } for item in data['records']]
    }
