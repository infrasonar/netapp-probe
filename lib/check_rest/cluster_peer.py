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
            'authentication_expiry_time': item.get('authentication', {}).get('expiry_time'),
            'authentication_generate_passphrase': item.get('authentication', {}).get('generate_passphrase'),
            'authentication_in_use': item.get('authentication', {}).get('in_use'),
            'authentication_passphrase': item.get('authentication', {}).get('passphrase'),
            'authentication_state': item.get('authentication', {}).get('state'),
            'encryption_proposed': item.get('encryption', {}).get('proposed'),
            'encryption_state': item.get('encryption', {}).get('state'),
            'ipspace_name': item.get('ipspace', {}).get('name'),
            'ipspace_uuid': item.get('ipspace', {}).get('uuid'),
            'local_network_broadcast_domain': item.get('local_network', {}).get('broadcast_domain'),
            'local_network_gateway': item.get('local_network', {}).get('gateway'),
            'local_network_netmask': item.get('local_network', {}).get('netmask'),
            'name': item.get('name'),
            'remote_name': item.get('remote', {}).get('name'),
            'remote_serial_number': item.get('remote', {}).get('serial_number'),
            'status_state': item.get('status', {}).get('state'),
            'status_update_time': item.get('status', {}).get('update_time'),
            'uuid': item.get('uuid'),
            'version_full': item.get('version', {}).get('full'),
            'version_generation': item.get('version', {}).get('generation'),
            'version_major': item.get('version', {}).get('major'),
            'version_minor': item.get('version', {}).get('minor'),  # 9.7
        } for item in data['records']]
    }
