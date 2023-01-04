from libprobe.probe import Probe
from lib.check.netapp import check_netapp
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'netapp': check_netapp
    }

    probe = Probe("netapp", version, checks)

    probe.start()
