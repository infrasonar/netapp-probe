from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


# TODO
# def ignoreSdwCl(typeDct):
#     for ky in list(typeDct):
#         if ky.lower().startswith('sdw_cl_'):
#             del typeDct[ky]
#     return typeDct

# def fmtCVolumes(dct):
#     dct['name'] = dct['volume-id-attributes-owning-vserver-name'] + '/' + dct['volume-id-attributes-name']

#     if 'grow' in dct.get('volume-autosize-attributes-mode', '') and 'volume-autosize-attributes-maximum-size' in dct:
#         dct['grownPercentage'] = dct['volume-space-attributes-size'] / dct['volume-autosize-attributes-maximum-size'] * 100 if dct['volume-autosize-attributes-maximum-size'] else 0
#         dct['growBytesFree'] = dct['volume-autosize-attributes-maximum-size'] - dct['volume-space-attributes-size']
#     return dct


def on_item(item: dict) -> dict:
    item['name'] = item['volume-id-attributes-owning-vserver-name'] + '/' + item['volume-id-attributes-name']
    return item


async def check_volume(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<volume-get-iter />')
    rows = flatten(tree, on_item)
    return {
        'volume': rows,
    }
