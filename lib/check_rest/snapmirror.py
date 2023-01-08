from libprobe.asset import Asset
from . import query


async def check_snapmirror(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/snapmirror/relationships?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'snapmirror': [{
            'name': item['uuid'],
            'exported_snapshot': item['exported_snapshot'],
            'group_type': item.get('group_type'),  # 9.11
            'healthy': item['healthy'],
            'identity_preservation': item.get('identity_preservation'),  # 9.11
            'lag_time': item['lag_time'],
            'last_transfer_type': item.get('last_transfer_type'),  # 9.11
            'policy_name': item['policy']['name'],
            'policy_type': item['policy']['type'],
            'policy_uuid': item['policy']['uuid'],
            'preserve': item['preserve'],
            'quick_resync': item['quick_resync'],
            'recover_after_break': item['recover_after_break'],
            'restore': item['restore'],
            'restore_to_snapshot': item['restore_to_snapshot'],
            'state': item['state'],
            'throttle': item.get('throttle'),  # 9.12
            'transfer_bytes_transferred': item['transfer']['bytes_transferred'],
            'transfer_end_time': item['transfer']['end_time'],
            'transfer_state': item['transfer']['state'],
            'transfer_total_duration': item['transfer']['total_duration'],
            'transfer_uuid': item['transfer']['uuid'],
            **({'transfer_schedule_name': item['transfer_schedule']['name'],
                'transfer_schedule_uuid': item['transfer_schedule']['uuid'], } if 'transfer_schedule' in item else {}),  # 9.11
        } for item in data['records']]
    }
