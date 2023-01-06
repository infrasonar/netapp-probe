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
            'aggregates_delegated': item['aggregates_delegated'],
            'anti_ransomware_default_volume_state': item['anti_ransomware_default_volume_state'],
            'certificate_uuid': item['certificate']['uuid'],
            'cifs_allowed': item['cifs']['allowed'],
            'cifs_enabled': item['cifs']['enabled'],
            'comment': item['comment'],
            'fcp_allowed': item['fcp']['allowed'],
            'fcp_enabled': item['fcp']['enabled'],
            'ipspace_name': item['ipspace']['name'],
            'ipspace_uuid': item['ipspace']['uuid'],
            'iscsi_allowed': item['iscsi']['allowed'],
            'iscsi_enabled': item['iscsi']['enabled'],
            'language': item['language'],
            'ldap_enabled': item['ldap']['enabled'],
            'max_volumes': item['max_volumes'],
            'name': item['name'],
            'ndmp_allowed': item['ndmp']['allowed'],
            'nfs_allowed': item['nfs']['allowed'],
            'nfs_enabled': item['nfs']['enabled'],
            'nis_enabled': item['nis']['enabled'],
            'nvme_allowed': item['nvme']['allowed'],
            'nvme_enabled': item['nvme']['enabled'],
            'retention_period': item['retention_period'],
            's3_enabled': item['s3']['enabled'],
            'snapshot_policy_name': item['snapshot_policy']['name'],
            'snapshot_policy_uuid': item['snapshot_policy']['uuid'],
            'state': item['state'],
            'subtype': item['subtype'],
            'uuid': item['uuid'],
        } for item in data['records']]
    }
