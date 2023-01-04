from libprobe.asset import Asset
from ..netappquery import query
from ..utils import flatten


async def check_cifs_options(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    tree = await query(asset, asset_config, check_config, '<cifs-options-get-iter />')
    rows = flatten(tree)
    return {
        'cifs_options': rows,
    }
