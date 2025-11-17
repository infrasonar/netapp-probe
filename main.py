from libprobe.probe import Probe
from lib.check.aggregate import CheckAggregate
from lib.check.autosupport import CheckAutosupport
from lib.check.cifs import CheckCifs
from lib.check.cifs_service import CheckCifsService
from lib.check.cluster_node import CheckClusterNode
from lib.check.cluster_peer import CheckClusterPeer
from lib.check.disk import CheckDisk
from lib.check.fcp import CheckFcp
from lib.check.interface import CheckInterface
from lib.check.interface_port import CheckInterfacePort
from lib.check.lun import CheckLun
from lib.check.qtree import CheckQtree
from lib.check.snapmirror import CheckSnapmirror
from lib.check.system import CheckSystem
from lib.check.volume import CheckVolume
from lib.check.volume_snapshot import CheckVolumeSnapshot
from lib.check.vserver import CheckVserver
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckAggregate,
        CheckAutosupport,
        CheckCifs,
        CheckCifsService,
        CheckClusterNode,
        CheckClusterPeer,
        CheckDisk,
        CheckFcp,
        CheckInterface,
        CheckInterfacePort,
        CheckLun,
        CheckQtree,
        CheckSnapmirror,
        CheckSystem,
        CheckVolume,
        CheckVolumeSnapshot,
        CheckVserver,
    )

    probe = Probe("netapp", version, checks)

    probe.start()
