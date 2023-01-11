from libprobe.asset import Asset
from . import query
from ..utils import datetime_to_ts
from hashlib import md5


async def check_autosupport(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/support/autosupport?fields=issues,*'
    data = await query(asset, asset_config, check_config, url)

    autosupport = {
        'name': 'autosupport',
        'contact_support': data.get('contact_support'),
        'enabled': data.get('enabled'),
        'from': data.get('from'),
        'is_minimal': data.get('is_minimal'),
        'mail_hosts': data.get('mail_hosts'),
        'proxy_url': data.get('proxy_url'),
        'transport': data.get('transport'),
    }

    issues = [{
        'name': md5((item['node']['uuid'] + item['issue']['message']).encode()).hexdigest(),
        'corrective_action_code': item.get('corrective_action', {}).get('code'),
        'corrective_action_message': item.get('corrective_action', {}).get('message'),
        'issue_code': item.get('issue', {}).get('code'),
        'issue_message': item.get('issue', {}).get('message'),
        'node_name': item.get('node', {}).get('name'),
        'node_uuid': item.get('node', {}).get('uuid'),
    } for item in data['issues']]

    url = '/api/support/autosupport/messages?fields=*'
    data = await query(asset, asset_config, check_config, url)

    history = [{
        'name': f"{item['destination']}/{item['index']}",
        'destination': item.get('destination'),
        'index': item.get('index'),
        'generated_on': datetime_to_ts(item.get('generated_on')),
        'node_name': item.get('node', {}).get('name'),
        'node_uuid': item.get('node', {}).get('uuid'),
    } for item in data['records']]

    return {
        'autosupport': autosupport,
        'issues': issues,
        'history': history,
    }
