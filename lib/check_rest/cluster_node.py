from libprobe.asset import Asset
from . import query


async def check_cluster_node(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/cluster/nodes?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cluster_node': [{
            'controller_board': item['controller'].get('board'),  # 9.9
            **({'controller_cpu_count': item['controller']['cpu']['count'], } if 'cpu' in item['controller'] else {}),  # 9.9
            **({'controller_failed_fan_count': item['controller']['failed_fan']['count'],
                'controller_failed_fan_message_code': item['controller']['failed_fan']['message']['code'],
                'controller_failed_fan_message_message': item['controller']['failed_fan']['message']['message'], } if 'failed_fan' in item['controller'] else {}),  # 9.9
            **({'controller_failed_power_supply_count': item['controller']['failed_power_supply']['count'],
                'controller_failed_power_supply_message_code': item['controller']['failed_power_supply']['message']['code'],
                'controller_failed_power_supply_message_message': item['controller']['failed_power_supply']['message']['message'], } if 'failed_power_supply' in item['controller'] else {}),  # 9.9
            'controller_memory_size': item['controller'].get('memory_size'),  # 9.9
            'controller_over_temperature': item['controller']['over_temperature'],
            'date': item['date'],
            'location': item['location'],
            'membership': item['membership'],
            **({'metric_duration': item['metric']['duration'],
                'metric_processor_utilization': item['metric']['processor_utilization'],
                'metric_status': item['metric']['status'],
                'metric_timestamp': item['metric']['timestamp'], } if 'metric' in item else {}),  # 9.8
            'model': item['model'],
            'name': item['name'],
            **({'nvram_battery_state': item['nvram']['battery_state'],
                'nvram_id': item['nvram']['id'], } if 'nvram' in item else {}),  # 9.9
            'owner': item.get('owner'),  # 9.9
            'serial_number': item['serial_number'],
            # 'service_processor_ipv6_interface_enabled': item['service_processor']['ipv6_interface']['enabled'],
            'service_processor_state': item['service_processor']['state'],
            'state': item.get('state'),  # 9.7
            **({'statistics_processor_utilization_base': item['statistics']['processor_utilization_base'],
                'statistics_processor_utilization_raw': item['statistics']['processor_utilization_raw'],
                'statistics_status': item['statistics']['status'],
                'statistics_timestamp': item['statistics']['timestamp'], } if 'statistics' in item else {}),  # 9.8
            'storage_configuration': item.get('storage_configuration'),  # 9.9
            'system_id': item.get('system_id'),  # 9.7
            'uptime': item['uptime'],
            'uuid': item['uuid'],
            'version_full': item['version']['full'],
            'version_generation': item['version']['generation'],
            'version_major': item['version']['major'],
            'version_minor': item['version']['minor'],
        } for item in data['records']]
    }
