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
            'bytes_per_sector': item['bytes_per_sector'],
            'class': item['class'],
            'container_type': item['container_type'],
            'effective_type': item['effective_type'],
            'fips_certified': item['fips_certified'],
            'firmware_version': item['firmware_version'],
            'home_node_name': item['home_node']['name'],
            'home_node_uuid': item['home_node']['uuid'],
            'local': item['local'],
            'model': item['model'],
            'name': item['name'],
            'node_name': item['node']['name'],
            'node_uuid': item['node']['uuid'],
            'pool': item['pool'],
            'rpm': item['rpm'],
            'sector_count': item['sector_count'],
            'self_encrypting': item['self_encrypting'],
            'serial_number': item['serial_number'],
            'state': item['state'],
            'stats_average_latency': item['stats']['average_latency'],
            'stats_iops_total': item['stats']['iops_total'],
            'stats_path_error_count': item['stats']['path_error_count'],
            'stats_power_on_hours': item['stats']['power_on_hours'],
            'stats_throughput': item['stats']['throughput'],
            'type': item['type'],
            'uid': item['uid'],
            'usable_size': item['usable_size'],
            'vendor': item['vendor'],
        } for item in data['records']]
    }
