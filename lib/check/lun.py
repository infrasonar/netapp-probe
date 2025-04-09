from libprobe.asset import Asset
from ..netappquery import query
from ..utils import datetime_to_ts


def space_percent_used(item: dict):
    used = item.get('space', {}).get('used')
    size = item.get('space', {}).get('size')
    try:
        assert isinstance(used, (float, int))
        assert isinstance(size, (float, int))
        return round(used / size * 100)
    except Exception:
        return None


async def check_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/luns?fields=statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'lun': [{
            'auto_delete': item.get('auto_delete'),
            'class': item.get('class'),
            'clone_source_name':
            item.get('clone', {}).get('source', {}).get('name'),
            'clone_source_uuid':
            item.get('clone', {}).get('source', {}).get('uuid'),
            'comment': item.get('comment'),
            'consistency_group_name':
            item.get('consistency_group', {}).get('name'),
            'consistency_group_uuid':
            item.get('consistency_group', {}).get('uuid'),  # 9.10
            'convert_namespace_name':
            item.get('convert', {}).get('namespace', {}).get('name'),
            'convert_namespace_uuid':
            item.get('convert', {}).get('namespace', {}).get('uuid'),  # 9.11
            'create_time': datetime_to_ts(item.get('create_time')),  # 9.7
            'enabled': item.get('enabled'),
            'location_logical_unit':
            item.get('location', {}).get('logical_unit'),
            'location_node_name':
            item.get('location', {}).get('node', {}).get('name'),
            'location_node_uuid':
            item.get('location', {}).get('node', {}).get('uuid'),
            'location_qtree_id':
            item.get('location', {}).get('qtree', {}).get('id'),
            'location_qtree_name':
            item.get('location', {}).get('qtree', {}).get('name'),
            'location_volume_name':
            item.get('location', {}).get('volume', {}).get('name'),
            'location_volume_uuid':
            item.get('location', {}).get('volume', {}).get('uuid'),
            'name': item.get('name'),
            'os_type': item.get('os_type'),
            'qos_policy_name': item.get('qos_policy', {}).get('name'),
            'qos_policy_uuid': item.get('qos_policy', {}).get('uuid'),
            'serial_number': item.get('serial_number'),
            'space_guarantee_requested':
            item.get('space', {}).get('guarantee', {}).get('requested'),
            'space_guarantee_reserved':
            item.get('space', {}).get('guarantee', {}).get('reserved'),
            'space_scsi_thin_provisioning_support_enabled':
            item.get('space', {}).get(
                'scsi_thin_provisioning_support_enabled'),
            'space_percent_used': space_percent_used(item),
            'space_size': item.get('space', {}).get('size'),
            'space_used': item.get('space', {}).get('used'),
            'statistics_iops_raw_other':
            item.get('statistics', {}).get('iops_raw', {}).get('other'),
            'statistics_iops_raw_read':
            item.get('statistics', {}).get('iops_raw', {}).get('read'),
            'statistics_iops_raw_write':
            item.get('statistics', {}).get('iops_raw', {}).get('write'),
            'statistics_throughput_raw_other':
            item.get('statistics', {}).get('throughput_raw', {}).get('other'),
            'statistics_throughput_raw_read':
            item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_write':
            item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'status_container_state':
            item.get('status', {}).get('container_state'),
            'status_mapped': item.get('status', {}).get('mapped'),
            'status_read_only': item.get('status', {}).get('read_only'),
            'status_state': item.get('status', {}).get('state'),
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
            'uuid': item.get('uuid'),
            'vvol_is_bound': item.get('vvol', {}).get('is_bound'),  # 9.10
        } for item in data['records']]
    }
