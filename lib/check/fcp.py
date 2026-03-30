from libprobe.asset import Asset
from libprobe.check import Check
from ..netappquery import query


class CheckFcp(Check):
    key = 'fcp'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/api/network/fc/ports?fields=*'
        data = await query(asset, local_config, config, url)
        return {
            'fcp': [{
                'description': item.get('description'),
                'enabled': item.get('enabled'),
                'fabric_connected': item.get('fabric', {}).get('connected'),
                'fabric_connected_speed':
                item.get('fabric', {}).get('connected_speed'),
                'fabric_port_address': item.get('fabric', {}).get(
                    'port_address'),
                'fabric_switch_port': item.get('fabric', {}).get(
                    'switch_port'),
                'name': item.get('name'),
                'node_name': item.get('node', {}).get('name'),
                'node_uuid': item.get('node', {}).get('uuid'),
                'physical_protocol': item.get('physical_protocol'),
                'speed_configured': item.get('speed', {}).get('configured'),
                'speed_maximum': item.get('speed', {}).get('maximum'),
                'state': item.get('state'),
                'transceiver_form_factor':
                item.get('transceiver', {}).get('form_factor'),  # 9.8
                'transceiver_manufacturer':
                item.get('transceiver', {}).get('manufacturer'),
                'transceiver_part_number':
                item.get('transceiver', {}).get('part_number'),
                'uuid': item.get('uuid'),
                'wwnn': item.get('wwnn'),
                'wwpn': item.get('wwpn'),
            } for item in data['records']]
        }
