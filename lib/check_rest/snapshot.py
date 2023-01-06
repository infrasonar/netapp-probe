from libprobe.asset import Asset
from ..netappquery import query, query2
from ..utils import flatten


def on_item(item: dict) -> dict:
    item['snapshot_Name'] = item['name']
    item['name'] = item['vserver'].lower() + '/' + item['volume'] + ' ' + item['name']
    return item


async def check_snapshot(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/volumes'
    res = await query2(asset, asset_config, check_config, url)
    snapshots = []
    for item in res['records']:
        url = item['_links']['self']['href'] + '/snapshots?fields=*'
        snapshots_res = await query2(asset, asset_config, check_config, url)
        snapshots.extend({
            'create_time': snapshot['create_time'],
            'name': snapshot['name'],  # TODO
            'size': snapshot['size'],
            'svm_name': snapshot['svm']['name'],
            'svm_uud': snapshot['svm']['uuid'],
            'volume_name': snapshot['volume']['name'],
            'volume_uuid': snapshot['volume']['uuid'],
        } for snapshot in snapshots_res['records'])
    return {
        'snapshot': snapshots
    }
