from libprobe.asset import Asset
from . import query


async def check_disk(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/disks?fields=*'
    data = await query(asset, asset_config, check_config, url)
    return {
        'disk': [{
            'bay': item['bay'],
            'bytes_per_sector': item.get('bytes_per_sector'),  # 9.9
            'class': item['class'],
            'container_type': item['container_type'],
            'effective_type': item.get('effective_type'),   # 9.9
            'fips_certified': item.get('fips_certified'),   # 9.7
            'firmware_version': item['firmware_version'],
            'home_node_name': item['home_node']['name'],
            'home_node_uuid': item['home_node']['uuid'],
            'local': item.get('local'),   # 9.9
            'model': item['model'],
            'name': item['name'],
            'node_name': item['node']['name'],
            'node_uuid': item['node']['uuid'],
            'pool': item['pool'],
            'rpm': item['rpm'],
            'sector_count': item.get('sector_count'),   # 9.9
            'self_encrypting': item.get('self_encrypting'),   # 9.7
            'serial_number': item['serial_number'],
            'state': item['state'],
            **({'stats_average_latency': item['stats']['average_latency'],
                'stats_iops_total': item['stats']['iops_total'],
                'stats_path_error_count': item['stats']['path_error_count'],
                'stats_power_on_hours': item['stats']['power_on_hours'],
                'stats_throughput': item['stats']['throughput'], } if 'stats' in item else {}),  # 9.9
            'type': item['type'],
            'uid': item['uid'],
            'usable_size': item['usable_size'],
            'vendor': item['vendor'],
        } for item in data['records']]
    }
