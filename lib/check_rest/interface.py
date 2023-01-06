from libprobe.asset import Asset
from . import query


async def check_interface(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/network/ip/interfaces?fields=statistics,metric,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'interface': [{
            'dns_zone': item['dns_zone'],
            'enabled': item['enabled'],
            'ip_address': item['ip']['address'],
            'ip_family': item['ip']['family'],
            'ip_netmask': item['ip']['netmask'],
            'ipspace_name': item['ipspace']['name'],
            'ipspace_uuid': item['ipspace']['uuid'],
            'location_auto_revert': item['location']['auto_revert'],
            'location_failover': item['location']['failover'],
            'location_home_node_name': item['location']['home_node']['name'],
            'location_home_node_uuid': item['location']['home_node']['uuid'],
            'location_home_port_name': item['location']['home_port']['name'],
            'location_home_port_node_name': item['location']['home_port']['node']['name'],
            'location_home_port_uuid': item['location']['home_port']['uuid'],
            'location_is_home': item['location']['is_home'],
            'location_node_name': item['location']['node']['name'],
            'location_node_uuid': item['location']['node']['uuid'],
            'location_port_name': item['location']['port']['name'],
            'location_port_node_name': item['location']['port']['node']['name'],
            'location_port_uuid': item['location']['port']['uuid'],
            'metric_duration': item['metric']['duration'],
            'metric_status': item['metric']['status'],
            'metric_throughput_read': item['metric']['throughput']['read'],
            'metric_throughput_total': item['metric']['throughput']['total'],
            'metric_throughput_write': item['metric']['throughput']['write'],
            'metric_timestamp': item['metric']['timestamp'],
            'name': item['name'],
            'scope': item['scope'],
            'service_policy_name': item['service_policy']['name'],
            'service_policy_uuid': item['service_policy']['uuid'],
            'state': item['state'],
            'statistics_status': item['statistics']['status'],
            'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
            'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
            'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
            'statistics_timestamp': item['statistics']['timestamp'],
            'uuid': item['uuid'],
            'vip': item['vip'],
        } for item in data['records']]
    }
