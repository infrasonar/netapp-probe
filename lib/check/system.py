from libprobe.asset import Asset
from libprobe.check import Check
from ..netappquery import query


class CheckSystem(Check):
    key = 'system'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/api/private/cli/system?fields=health'
        data = await query(asset, local_config, config, url)
        system = [{
            'name': item['node'],
            'health': item['health'],
        } for item in data['records']]

        url = '/api/private/cli/system/health/subsystem?fields=health'
        data = await query(asset, local_config, config, url)
        subsystem = [{
            'name': item['subsystem'],
            'health': item['health'],
        } for item in data['records']]

        return {
            'system': system,
            'subsystem': subsystem,
        }
