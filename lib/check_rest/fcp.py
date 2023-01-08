from libprobe.asset import Asset
from . import query


async def check_fcp(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/network/fc/ports?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'fcp': [{
            'description': item['description'],
            'enabled': item['enabled'],
            'fabric_connected': item['fabric']['connected'],
            'fabric_connected_speed': item['fabric']['connected_speed'],
            'fabric_port_address': item['fabric']['port_address'],
            'fabric_switch_port': item['fabric']['switch_port'],
            'name': item['name'],
            'node_name': item['node']['name'],
            'node_uuid': item['node']['uuid'],
            'physical_protocol': item['physical_protocol'],
            'speed_configured': item['speed']['configured'],
            'speed_maximum': item['speed']['maximum'],
            'state': item['state'],
            # 'transceiver_form_factor': item['transceiver'].get('form_factor'),  # 9.8
            # 'transceiver_manufacturer': item['transceiver']['manufacturer'],
            # 'transceiver_part_number': item['transceiver']['part_number'],
            'uuid': item['uuid'],
            'wwnn': item['wwnn'],
            'wwpn': item['wwpn'],
        } for item in data['records']]
    }
