import asyncio
from libprobe.asset import Asset
from . import query
from ..utils import datetime_to_ts

THROTTLE = .2


async def check_snapshot(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/volumes'
    res = await query(asset, asset_config, check_config, url)
    snapshots = []
    for item in res['records']:
        await asyncio.sleep(THROTTLE)
        url = item['_links']['self']['href'] + '/snapshots?order_by=create_time'
        snapshots_res = await query(asset, asset_config, check_config, url)
        if snapshots_res['num_records'] == 0:
            continue
        snapshots_ts = [
            datetime_to_ts(a['create_time']) for a in snapshots_res['records']]
        max_diff = max(a - b for a, b in zip(snapshots_ts[1:], snapshots_ts)) \
            if len(snapshots_ts) > 1 else None
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
