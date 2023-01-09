from libprobe.asset import Asset
from . import query


async def check_vserver(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/svm/svms?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'vserver': [{
            'aggregates_delegated': item.get('aggregates_delegated'),  # 9.7
            'anti_ransomware_default_volume_state': item.get('anti_ransomware_default_volume_state'),  # 9.10
            'certificate_uuid': item.get('certificate', {}).get('uuid'),  # 9.7
            'cifs_allowed': item.get('cifs', {}).get('allowed'),  # 9.9
            'cifs_enabled': item.get('cifs', {}).get('enabled'),
            'comment': item.get('comment'),
            'fcp_allowed': item.get('fcp', {}).get('allowed'),  # 9.9
            'fcp_enabled': item.get('fcp', {}).get('enabled'),
            'ipspace_name': item.get('ipspace', {}).get('name'),
            'ipspace_uuid': item.get('ipspace', {}).get('uuid'),
            'iscsi_allowed': item.get('iscsi', {}).get('allowed'),  # 9.9
            'iscsi_enabled': item.get('iscsi', {}).get('enabled'),
            'language': item.get('language'),
            'ldap_enabled': item.get('ldap', {}).get('enabled'),
            'max_volumes': item.get('max_volumes'),  # 9.9
            'name': item.get('name'),
            'ndmp_allowed': item.get('ndmp', {}).get('allowed'),  # 9.10
            'nfs_allowed': item.get('nfs', {}).get('allowed'),  # 9.9
            'nfs_enabled': item.get('nfs', {}).get('enabled'),
            'nis_enabled': item.get('nis', {}).get('enabled'),
            'nvme_allowed': item.get('nvme', {}).get('allowed'),  # 9.9
            'nvme_enabled': item.get('nvme', {}).get('enabled'),
            'retention_period': item.get('retention_period'),
            's3_enabled': item.get('s3', {}).get('enabled'),  # 9.7
            'snapshot_policy_name': item.get('snapshot_policy', {}).get('name'),
            'snapshot_policy_uuid': item.get('snapshot_policy', {}).get('uuid'),
            'state': item.get('state'),
            'subtype': item.get('subtype'),
            'uuid': item.get('uuid'),
        } for item in data['records']]
    }
