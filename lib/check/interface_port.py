from libprobe.asset import Asset
from ..netappquery import query


async def check_interface_port(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    # use fields=** for compatibilty with older versions
    url = '/api/network/ethernet/ports?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'port': [{
            'broadcast_domain_ipspace_name':
            item.get('broadcast_domain', {}).get('ipspace', {}).get('name'),
            'broadcast_domain_name':
            item.get('broadcast_domain', {}).get('name'),
            'broadcast_domain_uuid':
            item.get('broadcast_domain', {}).get('uuid'),
            'enabled': item.get('enabled'),
            'mac_address': item.get('mac_address'),
            'mtu': item.get('mtu'),
            'name': item.get('name'),
            'node_name': item.get('node', {}).get('name'),
            'node_uuid': item.get('node', {}).get('uuid'),
            'reachability': item.get('reachability'),  # 9.8
            'speed': int(item['speed']) if 'speed' in item else None,  # this
            # is because v9.7 devices return string
            'state': item.get('state'),
            'statistics_device_link_down_count_raw':
            item.get('statistics', {}).get('device', {}).get(
                'link_down_count_raw'),
            'statistics_device_receive_raw_discards':
            item.get('statistics', {}).get('device', {}).get(
                'receive_raw', {}).get('discards'),
            'statistics_device_receive_raw_errors':
            item.get('statistics', {}).get('device', {}).get(
                'receive_raw', {}).get('errors'),
            'statistics_device_receive_raw_packets':
            item.get('statistics', {}).get('device', {}).get(
                'receive_raw', {}).get('packets'),
            'statistics_device_transmit_raw_discards':
            item.get('statistics', {}).get('device', {}).get(
                'transmit_raw', {}).get('discards'),
            'statistics_device_transmit_raw_errors':
            item.get('statistics', {}).get('device', {}).get(
                'transmit_raw', {}).get('errors'),
            'statistics_device_transmit_raw_packets':
            item.get('statistics', {}).get('device', {}).get(
                'transmit_raw', {}).get('packets'),
            'statistics_throughput_raw_read':
            item.get('statistics', {}).get('throughput_raw', {}).get('read'),
            'statistics_throughput_raw_write':
            item.get('statistics', {}).get('throughput_raw', {}).get('write'),
            'type': item.get('type'),
            'uuid': item.get('uuid'),
        } for item in data['records']]
    }
