from datetime import datetime
from typing import Optional


def datetime_to_ts(ds: Optional[str]) -> int:
    if ds is None:
        return
    try:
        return int(datetime.strptime(ds, "%Y-%m-%dT%H:%M:%S%z").timestamp())
    except Exception:
        return


def duration_to_sec(ds: Optional[str]):
    '''
    iso 8601 duration string

    we dont parse durations with Y(ear) and (M)onth
    (in the netapp specification these cases are not mentioned)

    PT15S
    PT4M
    PT30M
    PT2H
    P1D
    PT5M
    '''
    if ds is None:
        return
    try:
        assert ds.startswith('P')
        ds = ds[1:]
        value = 0
        if 'T' in ds:
            before_t, ds = ds.split('T')
            assert 'Y' not in before_t
            assert 'M' not in before_t
            if 'D' in before_t:
                d, _ = before_t.split('D')
                value += int(d) * 86400

        if 'H' in ds:
            h, ds = ds.split('H')
            value += int(h) * 3600
        if 'M' in ds:
            m, ds = ds.split('M')
            value += int(m) * 60
        if 'S' in ds:
            s, _ = ds.split('S')
            value += int(s)
        return value
    except Exception:
        return
