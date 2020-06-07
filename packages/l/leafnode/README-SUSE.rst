This is package of the latest snapshot of the upstream git
repository on https://gitlab.com/leafnode-2/leafnode-2 . It seems 
strange to use git checkout for the stable server package, but 
the development has stalled (as of today 2019-11-18, the last 
commit is a year old and it is mine), but the upstream maintainer 
for whatever reasons doesn’t want to make official release.

There are no scripts or any method of converting the currently 
existed leafnode-1 instance to leafnode-2. This is `what I got`_ 
from the upstream maintainer:

    Leafnode-2 has some minor update aids in place, one of the 
    most important parts is running "texpire -r" to rebuild the 
    hashes, and "fetchnews -f" to re-fetch the active files. See 
    README.html for other migration information regarding 
    configuration settings.

.. _`what I got`:
    http://krusty.dt.e-technik.uni-dortmund.de/pipermail/leafnode-list/2018q1/002780.html

For better orientation the package changelog has interspersed 
records from leafnode-2 package in the originally leafnode-1 one. 
They are all from me (mcepl@something) and they are marked as 
``[leafnode-2]`` in the first line of the record.

There is a droplet for sudoers allowing an user in the group
``newsadmin`` to run without a password command::

    sudo -u news /usr/sbin/fetchnews -vvv -e
