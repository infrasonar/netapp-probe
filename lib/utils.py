from datetime import datetime
from typing import Optional


def datetime_to_ts(ds: Optional[str]) -> int:
    if ds is None:
        return
    try:
        return int(datetime.strptime(ds, "%Y-%m-%dT%H:%M:%S%z").timestamp())
    except Exception:
        return
