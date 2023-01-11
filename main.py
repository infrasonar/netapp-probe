from libprobe.probe import Probe
from lib.check_rest.aggregate import check_aggregate
from lib.check_rest.autosupport import check_autosupport
from lib.check_rest.cifs import check_cifs
from lib.check_rest.cifs_service import check_cifs_service
from lib.check_rest.cluster_node import check_cluster_node
from lib.check_rest.cluster_peer import check_cluster_peer
from lib.check_rest.disk import check_disk
from lib.check_rest.fcp import check_fcp
from lib.check_rest.interface import check_interface
from lib.check_rest.interface_port import check_interface_port
from lib.check_rest.lun import check_lun
from lib.check_rest.qtree import check_qtree
from lib.check_rest.snapmirror import check_snapmirror
from lib.check_rest.volume import check_volume
from lib.check_rest.volume_snapshot import check_volume_snapshot
from lib.check_rest.vserver import check_vserver
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'aggregate': check_aggregate,
        'autosupport': check_autosupport,
        'cifs': check_cifs,
        'cifs_service': check_cifs_service,
        'cluster_node': check_cluster_node,
        'cluster_peer': check_cluster_peer,
        'disk': check_disk,
        'fcp': check_fcp,
        'interface': check_interface,
        'interface_port': check_interface_port,
        'lun': check_lun,
        'qtree': check_qtree,
        'snapmirror': check_snapmirror,
        'volume': check_volume,
        'volume_snapshot': check_volume_snapshot,
        'vserver': check_vserver,
    }

    probe = Probe("netapp", version, checks)

    probe.start()
