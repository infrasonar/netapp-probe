from libprobe.asset import Asset
from . import query


async def check_interface_ports(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/network/ethernet/ports?fields=statistics,metric,*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'port': [{
            'broadcast_domain_ipspace_name': item['broadcast_domain']['ipspace']['name'],
            'broadcast_domain_name': item['broadcast_domain']['name'],
            'broadcast_domain_uuid': item['broadcast_domain']['uuid'],
            'enabled': item['enabled'],
            'mac_address': item['mac_address'],
            'metric_duration': item['metric']['duration'],
            'metric_status': item['metric']['status'],
            'metric_throughput_read': item['metric']['throughput']['read'],
            'metric_throughput_total': item['metric']['throughput']['total'],
            'metric_throughput_write': item['metric']['throughput']['write'],
            'metric_timestamp': item['metric']['timestamp'],
            'mtu': item['mtu'],
            'name': item['name'],
            'node_name': item['node']['name'],
            'node_uuid': item['node']['uuid'],
            'reachability': item['reachability'],
            'speed': item['speed'],
            'state': item['state'],
            'statistics_device_link_down_count_raw': item['statistics']['device']['link_down_count_raw'],
            'statistics_device_receive_raw_discards': item['statistics']['device']['receive_raw']['discards'],
            'statistics_device_receive_raw_errors': item['statistics']['device']['receive_raw']['errors'],
            'statistics_device_receive_raw_packets': item['statistics']['device']['receive_raw']['packets'],
            'statistics_device_timestamp': item['statistics']['device']['timestamp'],
            'statistics_device_transmit_raw_discards': item['statistics']['device']['transmit_raw']['discards'],
            'statistics_device_transmit_raw_errors': item['statistics']['device']['transmit_raw']['errors'],
            'statistics_device_transmit_raw_packets': item['statistics']['device']['transmit_raw']['packets'],
            'statistics_status': item['statistics']['status'],
            'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
            'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
            'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
            'statistics_timestamp': item['statistics']['timestamp'],
            'type': item['type'],
            'uuid': item['uuid'],
        } for item in data['records']]
    }
