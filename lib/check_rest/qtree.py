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
            'export_policy_id': item.get('export_policy', {}).get('id'),
            'export_policy_name': item.get('export_policy', {}).get('name'),
            'group_id': item.get('group', {}).get('id'),  # 9.8
            'id': item.get('id'),
            'name': item.get('name'),
            'nas_path': item.get('nas', {}).get('path'),  # 9.9
            'path': item.get('path'),
            'security_style': item.get('security_style'),
            'statistics_iops_raw_other': item.get('statistics', {}).get('iops_raw', {}).get('other'),
            'statistics_iops_raw_read': item.get('statistics', {}).get('iops_raw', {}).get('read'),
            'statistics_iops_raw_total': item.get('statistics', {}).get('iops_raw', {}).get('total'),
            'statistics_iops_raw_write': item.get('statistics', {}).get('iops_raw', {}).get('write'),
            'statistics_status': item.get('statistics', {}).get('status'),
            'statistics_throughput_raw_other': item.get('statistics', {}).get('throughput_raw', {}).get('other'),
            'statistics_throughput_raw_read': item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_total': item.get('statistics', {}).get('throughput_raw', {}).get('total'),
            'statistics_throughput_raw_write': item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'statistics_timestamp': item.get('statistics', {}).get('timestamp'),  # 9.8
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
            'unix_permissions': item.get('unix_permissions'),
            'user_id': item.get('user', {}).get('id'),  # 9.8
            'volume_name': item.get('volume', {}).get('name'),
            'volume_uuid': item.get('volume', {}).get('uuid'),
        } for item in data['records']]
    }
