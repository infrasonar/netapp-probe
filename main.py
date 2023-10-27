from libprobe.probe import Probe
from lib.check.aggregate import check_aggregate
from lib.check.autosupport import check_autosupport
from lib.check.cifs import check_cifs
from lib.check.cifs_service import check_cifs_service
from lib.check.cluster_node import check_cluster_node
from lib.check.cluster_peer import check_cluster_peer
from lib.check.disk import check_disk
from lib.check.disk_wear import check_disk_wear
from lib.check.fcp import check_fcp
from lib.check.interface import check_interface
from lib.check.interface_port import check_interface_port
from lib.check.lun import check_lun
from lib.check.qtree import check_qtree
from lib.check.snapmirror import check_snapmirror
from lib.check.system import check_system
from lib.check.volume import check_volume
from lib.check.volume_snapshot import check_volume_snapshot
from lib.check.vserver import check_vserver
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
        'disk_wear': check_disk_wear,
        'fcp': check_fcp,
        'interface': check_interface,
        'interface_port': check_interface_port,
        'lun': check_lun,
        'qtree': check_qtree,
        'snapmirror': check_snapmirror,
        'system': check_system,
        'volume': check_volume,
        'volume_snapshot': check_volume_snapshot,
        'vserver': check_vserver,
    }

    probe = Probe("netapp", version, checks)

    probe.start()
