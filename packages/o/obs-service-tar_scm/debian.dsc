Format: 1.0
Source: obs-service-tar-scm
Version: 0.10.16.1590752286.5c27247
Provides: obs-service-obs_scm, obs-service-tar
Binary: obs-service-tar_scm
Maintainer: Adrian Schroeter <adrian@suse.de>
Architecture: all
Standards-Version: 3.7.2
Build-Depends: debhelper (>= 8.0.0), python (>= 2.6), python-argparse | python (>= 2.7), python-dateutil

Package: obs-service-tar-scm
Architecture: all
Provides: obs-service-obs-scm, obs-service-tar
Depends: ${misc:Depends}, ${python:Depends}, bzr, git, subversion, cpio, python-dateutil, python-yaml
Recommends: mercurial
Description: An OBS source service: fetches SCM tarballs
 This is a source service for openSUSE Build Service.
 It supports downloading from svn, git, hg and bzr repositories.

