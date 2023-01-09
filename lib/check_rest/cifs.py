from libprobe.asset import Asset
from . import query


async def check_cifs(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/protocols/cifs/shares?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'cifs': [{
            'access_based_enumeration': item.get('access_based_enumeration'),
            'allow_unencrypted_access': item.get('allow_unencrypted_access'),  # 9.11
            'change_notify': item.get('change_notify'),
            'comment': item.get('comment'),
            'continuously_available': item.get('continuously_available'),  # 9.10
            'dir_umask': item.get('dir_umask'),  # 9.10
            'encryption': item.get('encryption'),
            'file_umask': item.get('file_umask'),  # 9.10
            'force_group_for_create': item.get('force_group_for_create'),  # 9.10
            'home_directory': item.get('home_directory'),
            'name': item.get('name'),
            'namespace_caching': item.get('namespace_caching'),  # 9.10
            'no_strict_security': item.get('no_strict_security'),  # 9.9
            'offline_files': item.get('offline_files'),  # 9.10
            'oplocks': item.get('oplocks'),
            'path': item.get('path'),
            'show_snapshot': item.get('show_snapshot'),  # 9.10
            'svm_name': item.get('svm', {}).get('name'),
            'svm_uuid': item.get('svm', {}).get('uuid'),
            'unix_symlink': item.get('unix_symlink'),
            'volume_name': item.get('volume', {}).get('name'),
            'volume_uuid': item.get('volume', {}).get('uuid'),
            'vscan_profile': item.get('vscan_profile'),  # 9.10
        } for item in data['records']]
    }
