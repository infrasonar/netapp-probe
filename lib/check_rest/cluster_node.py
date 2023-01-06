from libprobe.asset import Asset
from . import query


async def check_cluster_node(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/cluster/nodes?fields=statistics,metric,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cluster_node': [{
            'controller_board': item['controller']['board'],
            'controller_cpu_count': item['controller']['cpu']['count'],
            'controller_failed_fan_count': item['controller']['failed_fan']['count'],
            'controller_failed_fan_message_code': item['controller']['failed_fan']['message']['code'],
            'controller_failed_fan_message_message': item['controller']['failed_fan']['message']['message'],
            'controller_failed_power_supply_count': item['controller']['failed_power_supply']['count'],
            'controller_failed_power_supply_message_code': item['controller']['failed_power_supply']['message']['code'],
            'controller_failed_power_supply_message_message': item['controller']['failed_power_supply']['message']['message'],
            'controller_memory_size': item['controller']['memory_size'],
            'controller_over_temperature': item['controller']['over_temperature'],
            'date': item['date'],
            'location': item['location'],
            'membership': item['membership'],
            'metric_duration': item['metric']['duration'],
            'metric_processor_utilization': item['metric']['processor_utilization'],
            'metric_status': item['metric']['status'],
            'metric_timestamp': item['metric']['timestamp'],
            'model': item['model'],
            'name': item['name'],
            'nvram_battery_state': item['nvram']['battery_state'],
            'nvram_id': item['nvram']['id'],
            'owner': item['owner'],
            'serial_number': item['serial_number'],
            'service_processor_ipv6_interface_enabled': item['service_processor']['ipv6_interface']['enabled'],
            'service_processor_state': item['service_processor']['state'],
            'state': item['state'],
            'statistics_processor_utilization_base': item['statistics']['processor_utilization_base'],
            'statistics_processor_utilization_raw': item['statistics']['processor_utilization_raw'],
            'statistics_status': item['statistics']['status'],
            'statistics_timestamp': item['statistics']['timestamp'],
            'storage_configuration': item['storage_configuration'],
            'system_id': item['system_id'],
            'uptime': item['uptime'],
            'uuid': item['uuid'],
            'version_full': item['version']['full'],
            'version_generation': item['version']['generation'],
            'version_major': item['version']['major'],
            'version_minor': item['version']['minor'],
        } for item in data['records']]
    }
