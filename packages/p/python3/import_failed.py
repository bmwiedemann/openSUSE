import sys, os
from sysconfig import get_path

failed_map_path = os.path.join(get_path('stdlib'), '_import_failed', 'import_failed.map')

if __spec__:
    failed_name = __spec__.name
else:
    failed_name = __name__

for line in open(failed_map_path):
    words = line.strip().split()
    if not words or words[0][0] == '#':
        continue
    assert words[0][-1] == ':'
    package = words[0][:-1]

    if failed_name in words[1:]:
        raise ImportError("""Module '{}' is not installed.
Use:
  sudo zypper install {}
to install it.""".format(failed_name, package))

raise ImportError("""Module '{}' is not installed.
It is supposed to be part of python3 distribution, but missing from failed import map.
Please file a bug on the SUSE Bugzilla.""".format(failed_name))
