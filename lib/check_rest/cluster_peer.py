from libprobe.asset import Asset
from . import query


async def check_cluster_peer(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/cluster/peers?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cluster_peer': [{
            'authentication_expiry_time': item['authentication']['expiry_time'],
            'authentication_generate_passphrase': item['authentication']['generate_passphrase'],
            'authentication_in_use': item['authentication']['in_use'],
            'authentication_passphrase': item['authentication']['passphrase'],
            'authentication_state': item['authentication']['state'],
            'encryption_proposed': item['encryption']['proposed'],
            'encryption_state': item['encryption']['state'],
            'ipspace_name': item['ipspace']['name'],
            'ipspace_uuid': item['ipspace']['uuid'],
            'local_network_broadcast_domain': item['local_network']['broadcast_domain'],
            'local_network_gateway': item['local_network']['gateway'],
            'local_network_netmask': item['local_network']['netmask'],
            'name': item['name'],
            'remote_name': item['remote']['name'],
            'remote_serial_number': item['remote']['serial_number'],
            'status_state': item['status']['state'],
            'status_update_time': item['status']['update_time'],
            'uuid': item['uuid'],
            **({'version_full': item['version']['full'],
                'version_generation': item['version']['generation'],
                'version_major': item['version']['major'],
                'version_minor': item['version']['minor'], } if 'version' in item else {}),  # 9.7
        } for item in data['records']]
    }
