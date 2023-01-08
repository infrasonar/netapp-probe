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
            **({'certificate_uuid': item['certificate']['uuid'], } if 'certificate' in item else {}),  # 9.7
            'cifs_allowed': item['cifs'].get('allowed'),  # 9.9
            'cifs_enabled': item['cifs']['enabled'],
            'comment': item['comment'],
            'fcp_allowed': item['fcp'].get('allowed'),  # 9.9
            'fcp_enabled': item['fcp']['enabled'],
            'ipspace_name': item['ipspace']['name'],
            'ipspace_uuid': item['ipspace']['uuid'],
            'iscsi_allowed': item['iscsi'].get('allowed'),  # 9.9
            'iscsi_enabled': item['iscsi']['enabled'],
            'language': item['language'],
            'ldap_enabled': item['ldap']['enabled'],
            'max_volumes': item.get('max_volumes'),  # 9.9
            'name': item['name'],
            **({'ndmp_allowed': item['ndmp']['allowed'], } if 'ndmp' in item else {}),  # 9.10
            'nfs_allowed': item['nfs'].get('allowed'),  # 9.9
            'nfs_enabled': item['nfs']['enabled'],
            'nis_enabled': item['nis']['enabled'],
            'nvme_allowed': item['nvme'].get('allowed'),  # 9.9
            'nvme_enabled': item['nvme']['enabled'],
            'retention_period': item['retention_period'],
            **({'s3_enabled': item['s3']['enabled'], } if 's3' in item else {}),  # 9.7
            'snapshot_policy_name': item['snapshot_policy']['name'],
            'snapshot_policy_uuid': item['snapshot_policy']['uuid'],
            'state': item['state'],
            'subtype': item['subtype'],
            'uuid': item['uuid'],
        } for item in data['records']]
    }
