from libprobe.asset import Asset
from ..netappquery import query


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/disks?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'disk': [{
            'bay': item.get('bay'),
            'bytes_per_sector': item.get('bytes_per_sector'),  # 9.9
            'class': item.get('class'),
            'container_type': item.get('container_type'),
            'effective_type': item.get('effective_type'),   # 9.9
            'fips_certified': item.get('fips_certified'),   # 9.7
            'firmware_version': item.get('firmware_version'),
            'home_node_name': item.get('home_node', {}).get('name'),
            'home_node_uuid': item.get('home_node', {}).get('uuid'),
            'local': item.get('local'),   # 9.9
            'model': item.get('model'),
            'name': item.get('name'),
            'node_name': item.get('node', {}).get('name'),
            'node_uuid': item.get('node', {}).get('uuid'),
            'pool': item.get('pool'),
            'rpm': item.get('rpm'),
            'sector_count': item.get('sector_count'),   # 9.9
            'self_encrypting': item.get('self_encrypting'),   # 9.7
            'serial_number': item.get('serial_number'),
            'state': item.get('state'),
            'stats_average_latency':
            item.get('stats', {}).get('average_latency'),
            'stats_iops_total': item.get('stats', {}).get('iops_total'),
            'stats_path_error_count':
            item.get('stats', {}).get('path_error_count'),
            'stats_power_on_hours':
            item.get('stats', {}).get('power_on_hours'),
            'stats_throughput': item.get('stats', {}).get('throughput'),  # 9.9
            'type': item.get('type'),
            'uid': item.get('uid'),
            'usable_size': item.get('usable_size'),
            'vendor': item.get('vendor'),
        } for item in data['records']]
    }
