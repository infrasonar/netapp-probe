import aiohttp
import asyncio
import base64
import xml.etree.ElementTree as ET
from libprobe.asset import Asset
from typing import List, Dict


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        request_xml: str) -> List[Dict]:
    address = check_config.get('address')
    if not address:
        address = asset.name
    assert asset_config, 'missing credentials'
    username = asset_config['username']
    password = asset_config['password']

    url = f'{address}/servlets/netapp.servlets.admin.XMLrequest_filer'
    data = (
        '<!DOCTYPE netapp SYSTEM \'file:/etc/netapp_filer.dtd\'>'
        '<netapp version="1.3" xmlns="http://www.netapp.com/filer/admin"'
        ' nmsdk_version="5.3" nmsdk_language="Python">'
        f'{request_xml}'
        '</netapp>'
    )

    auth_str = base64.encodebytes(
        f'{username}:{password}'.encode()).decode().replace('\n', '')
    headers = {
        'authorization': f'Basic {auth_str}',
        'content-type': 'text/xml; charset="UTF-8"',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url,
                                data=data,
                                headers=headers,
                                ssl=False) as resp:
            xml = await resp.text()
            tree = ET.fromstring(xml)
            return tree


def query_perf_objects(
    asset: Asset,
    asset_config: dict,
    check_config: dict,
    object_name: str,
) -> asyncio.Future:
    rt = ET.Element('perf-object-instance-list-info-iter')
    e = ET.SubElement(rt, 'objectname')
    e.text = object_name

    request_xml = ET.tostring(rt, encoding='unicode')
    return query(asset, asset_config, check_config, request_xml)


def query_perf_counters(
    asset: Asset,
    asset_config: dict,
    check_config: dict,
    object_name: str,
) -> asyncio.Future:
    rt = ET.Element('perf-object-counter-list-info')
    e = ET.SubElement(rt, 'objectname')
    e.text = object_name

    request_xml = ET.tostring(rt, encoding='unicode')
    return query(asset, asset_config, check_config, request_xml)


def query_perf(
    asset: Asset,
    asset_config: dict,
    check_config: dict,
    object_name: str,
    counters: List[str],
    instance_uuids: List[str],
) -> asyncio.Future:
    rt = ET.Element('perf-object-get-instances')
    e = ET.SubElement(rt, 'objectname')
    e.text = object_name

    e = ET.SubElement(rt, 'counters')
    for name in counters:
        e1 = ET.SubElement(e, 'counter')
        e1.text = name

    e = ET.SubElement(rt, 'instance-uuids')
    for instance_uuid in instance_uuids:
        e1 = ET.SubElement(e, 'instance-uuid')
        e1.text = instance_uuid

    request_xml = ET.tostring(rt, encoding='unicode')
    return query(asset, asset_config, check_config, request_xml)
