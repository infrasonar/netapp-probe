from libprobe.probe import Probe
# from lib.check.aggregate import check_aggregate
# from lib.check.api import check_api
# from lib.check.cf import check_cf
# from lib.check.cifs import check_cifs
# from lib.check.cifs_options import check_cifs_options
# from lib.check.cluster_node import check_cluster_node
# from lib.check.cluster_peer import check_cluster_peer
# from lib.check.cluster_peer_ping import check_cluster_peer_ping
# from lib.check.disk import check_disk
# from lib.check.disk_perf import check_disk_perf
# from lib.check.fcp import check_fcp
# from lib.check.interface import check_interface
# from lib.check.interface_ports import check_interface_ports
# from lib.check.license_v2 import check_license_v2
# from lib.check.license_v2_status import check_license_v2_status
# from lib.check.lun import check_lun
# from lib.check.ontapi_version import check_ontapi_version
# from lib.check.options import check_options
# from lib.check.processor_perf import check_processor_perf
# from lib.check.qtree import check_qtree
# from lib.check.resource_perf import check_resource_perf
# from lib.check.snapmirror import check_snapmirror
# from lib.check.snapshot import check_snapshot
# from lib.check.system_health import check_system_health
# from lib.check.system_node import check_system_node
# from lib.check.system_perf import check_system_perf
# from lib.check.system_version import check_system_version
# from lib.check.uptime import check_uptime
# from lib.check.volume import check_volume
# from lib.check.volume_perf import check_volume_perf
# from lib.check.vserver import check_vserver
from lib.version import __version__ as version

from lib.check_rest.aggregate import check_aggregate
from lib.check_rest.cifs import check_cifs
from lib.check_rest.cifs_options import check_cifs_options
from lib.check_rest.cluster_node import check_cluster_node
from lib.check_rest.cluster_peer import check_cluster_peer
from lib.check_rest.disk import check_disk
from lib.check_rest.fcp import check_fcp
from lib.check_rest.interface import check_interface
from lib.check_rest.interface_ports import check_interface_ports
from lib.check_rest.lun import check_lun
from lib.check_rest.qtree import check_qtree
from lib.check_rest.snapmirror import check_snapmirror
from lib.check_rest.snapshot import check_snapshot
from lib.check_rest.volume import check_volume
from lib.check_rest.vserver import check_vserver


if __name__ == '__main__':
    checks = {
        # 'api': check_api,
        'aggregate': check_aggregate,
        # 'cf': check_cf,
        'cifs': check_cifs,
        'cifsOptions': check_cifs_options,
        'clusterNode': check_cluster_node,
        'clusterPeer': check_cluster_peer,
        'fcp': check_fcp,
        'interface': check_interface,
        'interfacePorts': check_interface_ports,
        'lun': check_lun,
        # 'ontapApiVersion': check_ontapi_version,
        # 'options': check_options,
        # 'clusterPeerPing': check_cluster_peer_ping,
        # 'processorPerf': check_processor_perf,
        'qtree': check_qtree,
        # 'resourcePerf': check_resource_perf,
        'snapmirror': check_snapmirror,
        'snapshot': check_snapshot,
        'disk': check_disk,
        # 'diskPerf': check_disk_perf,
        # 'systemHealth': check_system_health,
        # 'systemNodeInfo': check_system_node,
        # 'systemPerf': check_system_perf,
        # 'systemVersion': check_system_version,
        # 'uptime': check_uptime,
        # 'v2ClusterLicense': check_license_v2_status,
        # 'v2License': check_license_v2,
        'vserver': check_vserver,
        # 'volumePerf': check_volume_perf,
        'volume': check_volume,
    }

    probe = Probe("netapp", version, checks)

    probe.start()
