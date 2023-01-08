from libprobe.asset import Asset
from . import query


async def check_qtree(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/qtrees?fields=statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'qtree': [{
            'export_policy_id': item['export_policy']['id'],
            'export_policy_name': item['export_policy']['name'],
            **({'group_id': item['group']['id'], } if 'group' in item else {}),  # 9.8
            'id': item['id'],
            'name': item['name'],
            **({'nas_path': item['nas']['path'], } if 'nas' in item else {}),  # 9.9
            # 'path': item['path'],
            'security_style': item['security_style'],
            **({'statistics_iops_raw_other': item['statistics']['iops_raw']['other'],
                'statistics_iops_raw_read': item['statistics']['iops_raw']['read'],
                'statistics_iops_raw_total': item['statistics']['iops_raw']['total'],
                'statistics_iops_raw_write': item['statistics']['iops_raw']['write'],
                'statistics_status': item['statistics']['status'],
                'statistics_throughput_raw_other': item['statistics']['throughput_raw']['other'],
                'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
                'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
                'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
                'statistics_timestamp': item['statistics']['timestamp'], } if 'statistics' in item else {}),  # 9.8
            'svm_name': item['svm']['name'],
            'svm_uuid': item['svm']['uuid'],
            'unix_permissions': item['unix_permissions'],
            **({'user_id': item['user']['id'], } if 'user' in item else {}),  # 9.8
            'volume_name': item['volume']['name'],
            'volume_uuid': item['volume']['uuid'],
        } for item in data['records']]
    }
