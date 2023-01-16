from libprobe.asset import Asset
from . import query


async def check_system(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    url = '/api/private/cli/system?fields=health,uptime'
    data = await query(asset, asset_config, check_config, url)
    system = [{
        'name': item['node'],
        'health': item['health'],
        'uptime': item['uptime'],
    } for item in data['records']]

    url = '/api/private/cli/system/health/subsystem?fields=health'
    data = await query(asset, asset_config, check_config, url)
    subsystem = [{
        'name': item['subsystem'],
        'health': item['health'],
    } for item in data['records']]

    return {
        'system': system,
        'subsystem': subsystem,
    }
