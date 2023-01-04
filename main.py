from libprobe.probe import Probe
from lib.check.aggregate import check_aggregate
from lib.check.api import check_api
from lib.check.cf import check_cf
from lib.check.cifs import check_cifs
from lib.check.cifs_options import check_cifs_options
from lib.check.cluster_node import check_cluster_node
from lib.check.cluster_peer import check_cluster_peer
from lib.check.cluster_peer_ping import check_cluster_peer_ping
from lib.check.disk import check_disk
from lib.check.disk_perf import check_disk_perf
from lib.check.fcp import check_fcp
from lib.check.interface import check_interface
from lib.check.interface_ports import check_interface_ports
from lib.check.license_v2 import check_license_v2
from lib.check.license_v2_status import check_license_v2_status
from lib.check.lun import check_lun
from lib.check.ontapi_version import check_ontapi_version
from lib.check.options import check_options
from lib.check.processor_perf import check_processor_perf
from lib.check.qtree import check_qtree
from lib.check.resource_perf import check_resource_perf
from lib.check.snapmirror import check_snapmirror
from lib.check.snapshot import check_snapshot
from lib.check.system_health import check_system_health
from lib.check.system_node import check_system_node
from lib.check.system_perf import check_system_perf
from lib.check.system_version import check_system_version
from lib.check.uptime import check_uptime
from lib.check.volume import check_volume
from lib.check.volume_perf import check_volume_perf
from lib.check.vserver import check_vserver
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'API': check_api,
        'Aggregates': check_aggregate,
        'Cf': check_cf,
        'Cifs': check_cifs,
        'CifsOptions': check_cifs_options,
        'ClusterNode': check_cluster_node,
        'ClusterPeer': check_cluster_peer,
        'FCP': check_fcp,
        'Interface': check_interface,
        'InterfacePorts': check_interface_ports,
        'Luns': check_lun,
        'OntapApiVersion': check_ontapi_version,
        'Options': check_options,
        'PingCluster': check_cluster_peer_ping,
        'ProcessorPerf': check_processor_perf,
        'QTree': check_qtree,
        'ResourcePerf': check_resource_perf,
        'SnapMirror': check_snapmirror,
        'Snapshot': check_snapshot,
        'StorageDisk': check_disk,
        'StorageDiskPerf': check_disk_perf,
        'SystemHealth': check_system_health,
        'SystemNodeInfo': check_system_node,
        'SystemPerf': check_system_perf,
        'SystemVersion': check_system_version,
        'Uptime': check_uptime,
        'V2ClusterLicense': check_license_v2_status,
        'V2License': check_license_v2,
        'VServer': check_vserver,
        'VolumePerf': check_volume_perf,
        'Volumes': check_volume,
    }

    probe = Probe("netapp", version, checks)

    probe.start()
