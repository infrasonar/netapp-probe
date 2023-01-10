from datetime import datetime
from typing import Callable, Optional, List
from xml.etree.ElementTree import Element


def datetime_to_ts(ds: str) -> int:
    return int(datetime.fromisoformat(ds).timestamp())


def _flatten(node: Element, path: Optional[List[str]] = []):
    for child in node:
        _, has_namespace, postfix = child.tag.partition('}')
        tag_ = postfix if has_namespace else child.tag

        if child.text:
            metric_name = '-'.join(path + [tag_])
            yield metric_name, child.text

        for tag, value in _flatten(child, path + [tag_]):
            yield tag, value


def flatten(
        tree: Element,
        on_item: Optional[Callable[[dict], dict]] = lambda item: item
) -> list:
    return [
        on_item(dict(_flatten(a)))
        for results in tree
        for attributes_list in results
        for a in attributes_list
    ]


def flatten_one(
    tree: Element
) -> dict:
    assert tree
    return dict(_flatten(tree[0]))


def on_counterinfos(item, counterinfos):
    for m in set(item) & set(counterinfos):
        properties = counterinfos[m].get('properties')
        mbase = counterinfos[m].get('base-counter')
        if properties and 'percent' in properties:
            try:
                item[m] = item[m] / item[mbase] * 100
            except Exception:
                item[m] = None
        if properties and 'average' in properties:
            try:
                item[m] = item[m] / item[mbase]
            except Exception:
                item[m] = None
