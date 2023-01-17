from libprobe.asset import Asset
from . import query


async def check_interface(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    # use fields=** for compatibilty with older versions
    url = '/api/network/ip/interfaces?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'interface': [{
            'dns_zone': item.get('dns_zone'),  # 9.9
            'enabled': item.get('enabled'),
            'ip_address': item.get('ip', {}).get('address'),
            'ip_family': item.get('ip', {}).get('family'),
            'ip_netmask': item.get('ip', {}).get('netmask'),
            'ipspace_name': item.get('ipspace', {}).get('name'),
            'ipspace_uuid': item.get('ipspace', {}).get('uuid'),
            'location_auto_revert': item.get('location', {}).get('auto_revert'),
            'location_failover': item.get('location', {}).get('failover'),
            'location_home_node_name': item.get('location', {}).get('home_node', {}).get('name'),
            'location_home_node_uuid': item.get('location', {}).get('home_node', {}).get('uuid'),
            'location_home_port_name': item.get('location', {}).get('home_port', {}).get('name'),
            'location_home_port_node_name': item.get('location', {}).get('home_port', {}).get('node', {}).get('name'),
            'location_home_port_uuid': item.get('location', {}).get('home_port', {}).get('uuid'),
            'location_is_home': item.get('location', {}).get('is_home'),
            'location_node_name': item.get('location', {}).get('node', {}).get('name'),
            'location_node_uuid': item.get('location', {}).get('node', {}).get('uuid'),
            'location_port_name': item.get('location', {}).get('port', {}).get('name'),
            'location_port_node_name': item.get('location', {}).get('port', {}).get('node', {}).get('name'),
            'location_port_uuid': item.get('location', {}).get('port', {}).get('uuid'),
            'name': item.get('name'),
            'scope': item.get('scope'),
            'service_policy_name': item.get('service_policy', {}).get('name'),
            'service_policy_uuid': item.get('service_policy', {}).get('uuid'),
            'state': item.get('state'),
            'statistics_throughput_raw_read': item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_write': item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'uuid': item.get('uuid'),
            'vip': item.get('vip'),
        } for item in data['records']]
    }
