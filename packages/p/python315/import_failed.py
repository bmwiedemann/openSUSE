import sys, os
from sysconfig import get_path

failed_map_path = os.path.join(get_path('stdlib'), '_import_failed', 'import_failed.map')

if __spec__:
    failed_name = __spec__.name
else:
    failed_name = __name__

with open(failed_map_path) as fd:
    for line in fd:
        package = line.split(':')[0]
        imports = line.split(':')[1]
        if failed_name in imports:
            raise ImportError(f"""Module '{failed_name}' is not installed.
Use:
  sudo zypper install {package}
to install it.""")

raise ImportError(f"""Module '{failed_name}' is not installed.
It is supposed to be part of python3 distribution, but missing from failed import map.
Please file a bug on the SUSE Bugzilla.""")
