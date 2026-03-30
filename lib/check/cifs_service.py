from libprobe.asset import Asset
from libprobe.check import Check
from ..netappquery import query


class CheckCifsService(Check):
    key = 'cifs_service'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/api/protocols/cifs/services?fields=statistics,*'
        data = await query(asset, local_config, config, url)
        return {
            'cifs_service': [{
                'comment': item.get('comment'),
                'default_unix_user': item.get('default_unix_user'),
                'enabled': item.get('enabled'),
                'group_policy_object_enabled':
                item.get('group_policy_object_enabled'),  # 9.12
                'name': item.get('name'),
                'statistics_iops_raw_other':
                item.get('statistics', {}).get('iops_raw', {}).get('other'),
                'statistics_iops_raw_read':
                item.get('statistics', {}).get('iops_raw', {}).get('read'),
                'statistics_iops_raw_write':
                item.get('statistics', {}).get('iops_raw', {}).get('write'),
                'statistics_throughput_raw_read':
                item.get('statistics', {}).get('throughput_raw', {}).get(
                    'read'),
                'statistics_throughput_raw_write':
                item.get('statistics', {}).get('throughput_raw', {}).get(
                    'write'),
                'svm_name': item.get('svm', {}).get('name'),
                'svm_uuid': item.get('svm', {}).get('uuid'),
            } for item in data['records']]
        }
