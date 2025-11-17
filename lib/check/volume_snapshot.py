import asyncio
from libprobe.asset import Asset
from libprobe.check import Check
from ..netappquery import query
from ..utils import datetime_to_ts

THROTTLE = .2


class CheckVolumeSnapshot(Check):
    key = 'volume_snapshot'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        url = '/api/storage/volumes'
        res = await query(asset, local_config, config, url)
        snapshots = []
        for item in res['records']:
            await asyncio.sleep(THROTTLE)
            volume_url = item['_links']['self']['href']
            url = f'{volume_url}/snapshots?order_by=create_time'
            snapshots_res = await query(asset, local_config, config, url)
            if snapshots_res['num_records'] == 0:
                continue
            snapshots_ts = [
                datetime_to_ts(a['create_time'])
                for a in snapshots_res['records']]
            try:
                max_diff = max(
                    a - b
                    for a, b in zip(snapshots_ts[1:], snapshots_ts)
                    if a is not None and b is not None)
            except ValueError:
                max_diff = None
            snapshots.append({
                'name': item['name'],
                'newest_create_time': snapshots_ts[-1],
                'newest_name': snapshots_res['records'][-1]['name'],
                'oldest_create_time': snapshots_ts[0],
                'oldest_name': snapshots_res['records'][0]['name'],
                'max_snapshot_diff': max_diff,
            })
        return {
            'snapshot': snapshots
        }
