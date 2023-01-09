from libprobe.asset import Asset
from . import query


async def check_lun(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:
    url = '/api/storage/luns?fields=**'
    data = await query(asset, asset_config, check_config, url)
    return {
        'lun': [{
            # 'auto_delete': item['auto_delete'],
            'class': item['class'],
            'clone_source_name': item['clone']['source']['name'],
            'clone_source_uuid': item['clone']['source']['uuid'],
            'comment': item['comment'],
            **({'consistency_group_name': item['consistency_group']['name'],
                'consistency_group_uuid': item['consistency_group']['uuid'], } if 'consistency_group' in item else {}),  # 9.10
            **({'convert_namespace_name': item['convert']['namespace']['name'],
                'convert_namespace_uuid': item['convert']['namespace']['uuid'], } if 'convert' in item else {}),  # 9.11
            **({'copy_source_max_throughput': item['copy']['source']['max_throughput'],
                'copy_source_name': item['copy']['source']['name'],
                'copy_source_progress_elapsed': item['copy']['source']['progress']['elapsed'],
                'copy_source_progress_percent_complete': item['copy']['source']['progress']['percent_complete'],
                'copy_source_progress_state': item['copy']['source']['progress']['state'],
                'copy_source_progress_volume_snapshot_blocked': item['copy']['source']['progress']['volume_snapshot_blocked'],
                'copy_source_uuid': item['copy']['source']['uuid'], } if 'copy' in item else {}),  # 9.10
            'create_time': item.get('create_time'),  # 9.7
            'enabled': item['enabled'],
            'location_logical_unit': item['location']['logical_unit'],
            'location_node_name': item['location']['node']['name'],
            'location_node_uuid': item['location']['node']['uuid'],
            'location_qtree_id': item['location']['qtree']['id'],
            'location_qtree_name': item['location']['qtree']['name'],
            'location_volume_name': item['location']['volume']['name'],
            'location_volume_uuid': item['location']['volume']['uuid'],
            **({'metric_duration': item['metric']['duration'],
                'metric_iops_other': item['metric']['iops']['other'],
                'metric_iops_read': item['metric']['iops']['read'],
                'metric_iops_total': item['metric']['iops']['total'],
                'metric_iops_write': item['metric']['iops']['write'],
                'metric_latency_other': item['metric']['latency']['other'],
                'metric_latency_read': item['metric']['latency']['read'],
                'metric_latency_total': item['metric']['latency']['total'],
                'metric_latency_write': item['metric']['latency']['write'],
                'metric_status': item['metric']['status'],
                'metric_throughput_other': item['metric']['throughput']['other'],
                'metric_throughput_read': item['metric']['throughput']['read'],
                'metric_throughput_total': item['metric']['throughput']['total'],
                'metric_throughput_write': item['metric']['throughput']['write'],
                'metric_timestamp': item['metric']['timestamp'], } if 'metric' in item else {}),  # 9.7
            'movement_max_throughput': item['movement']['max_throughput'],
            'movement_paths_destination': item['movement']['paths']['destination'],
            'movement_paths_source': item['movement']['paths']['source'],
            'movement_progress_elapsed': item['movement']['progress']['elapsed'],
            'movement_progress_percent_complete': item['movement']['progress']['percent_complete'],
            'movement_progress_state': item['movement']['progress']['state'],
            'movement_progress_volume_snapshot_blocked': item['movement']['progress']['volume_snapshot_blocked'],
            'name': item['name'],
            'os_type': item['os_type'],
            'qos_policy_name': item['qos_policy']['name'],
            'qos_policy_uuid': item['qos_policy']['uuid'],
            'serial_number': item['serial_number'],
            'space_guarantee_requested': item['space']['guarantee']['requested'],
            'space_guarantee_reserved': item['space']['guarantee']['reserved'],
            'space_scsi_thin_provisioning_support_enabled': item['space']['scsi_thin_provisioning_support_enabled'],
            'space_size': item['space']['size'],
            'space_used': item['space']['used'],
            **({'statistics_iops_raw_other': item['statistics']['iops_raw']['other'],
                'statistics_iops_raw_read': item['statistics']['iops_raw']['read'],
                'statistics_iops_raw_total': item['statistics']['iops_raw']['total'],
                'statistics_iops_raw_write': item['statistics']['iops_raw']['write'],
                'statistics_latency_raw_other': item['statistics']['latency_raw']['other'],
                'statistics_latency_raw_read': item['statistics']['latency_raw']['read'],
                'statistics_latency_raw_total': item['statistics']['latency_raw']['total'],
                'statistics_latency_raw_write': item['statistics']['latency_raw']['write'],
                'statistics_status': item['statistics']['status'],
                'statistics_throughput_raw_other': item['statistics']['throughput_raw']['other'],
                'statistics_throughput_raw_read': item['statistics']['throughput_raw']['read'],
                'statistics_throughput_raw_total': item['statistics']['throughput_raw']['total'],
                'statistics_throughput_raw_write': item['statistics']['throughput_raw']['write'],
                'statistics_timestamp': item['statistics']['timestamp'], } if 'statistics' in item else {}),  # 9.7
            'status_container_state': item['status']['container_state'],
            'status_mapped': item['status']['mapped'],
            'status_read_only': item['status']['read_only'],
            'status_state': item['status']['state'],
            'svm_name': item['svm']['name'],
            'svm_uuid': item['svm']['uuid'],
            'uuid': item['uuid'],
            **({'vvol_is_bound': item['vvol']['is_bound'], } if 'vvol' in item else {}),  # 9.10
        } for item in data['records']]
    }
