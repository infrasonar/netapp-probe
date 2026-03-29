from hashlib import md5
from libprobe.asset import Asset
from libprobe.check import Check
from ..netappquery import query


class CheckAutosupport(Check):
    key = 'autosupport'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/api/support/autosupport?fields=issues,*'
        data = await query(asset, local_config, config, url)

        autosupport = [{
            'name': 'autosupport',
            'contact_support': data.get('contact_support'),
            'enabled': data.get('enabled'),
            'from': data.get('from'),
            'is_minimal': data.get('is_minimal'),
            'mail_hosts': data.get('mail_hosts'),
            'proxy_url': data.get('proxy_url'),
            'transport': data.get('transport'),
        }]

        issues = [{
            'name': md5((item['node']['uuid'] + item['issue']['message']
                         ).encode()).hexdigest(),
            'corrective_action_code':
            item.get('corrective_action', {}).get('code'),
            'corrective_action_message':
            item.get('corrective_action', {}).get('message'),
            'issue_code': item.get('issue', {}).get('code'),
            'issue_message': item.get('issue', {}).get('message'),
            'node_name': item.get('node', {}).get('name'),
            'node_uuid': item.get('node', {}).get('uuid'),
        } for item in data.get('issues', [])]

        return {
            'autosupport': autosupport,
            'issues': issues,
        }
