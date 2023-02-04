from libprobe.asset import Asset
from ..netappquery import query
from ..utils import datetime_to_ts, duration_to_sec


async def check_snapmirror(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/snapmirror/relationships?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'snapmirror': [{
            'name': item.get('uuid'),
            'exported_snapshot': item.get('exported_snapshot'),
            'group_type': item.get('group_type'),  # 9.11
            'healthy': item.get('healthy'),
            'identity_preservation': item.get('identity_preservation'),  # 9.11
            'lag_time': duration_to_sec(item.get('lag_time')),
            'last_transfer_type': item.get('last_transfer_type'),  # 9.11
            'policy_name': item.get('policy', {}).get('name'),
            'policy_type': item.get('policy', {}).get('type'),
            'policy_uuid': item.get('policy', {}).get('uuid'),
            'preserve': item.get('preserve'),
            'quick_resync': item.get('quick_resync'),
            'recover_after_break': item.get('recover_after_break'),
            'restore': item.get('restore'),
            'restore_to_snapshot': item.get('restore_to_snapshot'),
            'state': item.get('state'),
            'throttle': item.get('throttle'),  # 9.12
            'transfer_bytes_transferred':
            item.get('transfer', {}).get('bytes_transferred'),
            'transfer_end_time':
            datetime_to_ts(item.get('transfer', {}).get('end_time')),
            'transfer_state':
            item.get('transfer', {}).get('state'),
            'transfer_total_duration':
            duration_to_sec(item.get('transfer', {}).get('total_duration')),
            'transfer_uuid':
            item.get('transfer', {}).get('uuid'),
            'transfer_schedule_name':
            item.get('transfer_schedule', {}).get('name'),
            'transfer_schedule_uuid':
            item.get('transfer_schedule', {}).get('uuid'),  # 9.11
        } for item in data['records']]
    }
