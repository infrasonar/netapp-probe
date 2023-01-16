from libprobe.asset import Asset
from . import query
from ..utils import datetime_to_ts


def statistics_processor_utilization(item: dict):
    val = item.get('statistics', {}).get('processor_utilization_raw')
    base = item.get('statistics', {}).get('processor_utilization_base')
    try:
        return round(val / base * 100)
    except Exception:
        return None


async def check_cluster_node(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/cluster/nodes?fields=metric,statistics,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cluster_node': [{
            'controller_board': item.get('controller', {}).get('board'),  # 9.9
            'controller_cpu_count': item.get('controller', {}).get('cpu', {}).get('count'),  # 9.9
            'controller_failed_fan_count': item.get('controller', {}).get('failed_fan', {}).get('count'),
            'controller_failed_fan_message_code': item.get('controller', {}).get('failed_fan', {}).get('message', {}).get('code'),
            'controller_failed_fan_message_message': item.get('controller', {}).get('failed_fan', {}).get('message', {}).get('message'),  # 9.9
            'controller_failed_power_supply_count': item.get('controller', {}).get('failed_power_supply', {}).get('count'),
            'controller_failed_power_supply_message_code': item.get('controller', {}).get('failed_power_supply', {}).get('message', {}).get('code'),
            'controller_failed_power_supply_message_message': item.get('controller', {}).get('failed_power_supply', {}).get('message', {}).get('message'),  # 9.9
            'controller_memory_size': item.get('controller', {}).get('memory_size'),  # 9.9
            'controller_over_temperature': item.get('controller', {}).get('over_temperature'),
            'date': datetime_to_ts(item.get('date')),
            'location': item.get('location'),
            'membership': item.get('membership'),
            'metric_duration': item.get('metric', {}).get('duration'),
            'metric_processor_utilization': item.get('metric', {}).get('processor_utilization'),
            'metric_status': item.get('metric', {}).get('status'),
            'metric_timestamp': datetime_to_ts(item.get('metric', {}).get('timestamp')),  # 9.8
            'model': item.get('model'),
            'name': item.get('name'),
            'nvram_battery_state': item.get('nvram', {}).get('battery_state'),
            'nvram_id': item.get('nvram', {}).get('id'),  # 9.9
            'owner': item.get('owner'),  # 9.9
            'serial_number': item.get('serial_number'),
            'service_processor_ipv6_interface_enabled': item.get('service_processor', {}).get('ipv6_interface', {}).get('enabled'),
            'service_processor_state': item.get('service_processor', {}).get('state'),
            'state': item.get('state'),  # 9.7
            'statistics_processor_utilization': statistics_processor_utilization(item),
            'statistics_processor_utilization_base': item.get('statistics', {}).get('processor_utilization_base'),
            'statistics_processor_utilization_raw': item.get('statistics', {}).get('processor_utilization_raw'),
            'statistics_status': item.get('statistics', {}).get('status'),
            'statistics_timestamp': datetime_to_ts(item.get('statistics', {}).get('timestamp')),  # 9.8
            'storage_configuration': item.get('storage_configuration'),  # 9.9
            'system_id': item.get('system_id'),  # 9.7
            'uptime': item.get('uptime'),
            'uuid': item.get('uuid'),
            'version_full': item.get('version', {}).get('full'),
            'version_generation': item.get('version', {}).get('generation'),
            'version_major': item.get('version', {}).get('major'),
            'version_minor': item.get('version', {}).get('minor'),
        } for item in data['records']]
    }
