ceph-test.spec apologia
=======================

The ceph-test.spec file is generated automatically by running pre_checkin.sh

Originally, the ceph-test RPM was built by ceph.spec as a subpackage.

When ceph was first included in Ring1, the build time was too long and ceph
was blocking Factory builds. The ceph-test RPM - a non-user-facing subpackage
that is only used by CI tests - accounted for a significant portion of that
excessive build time. By spinning the ceph-test RPM off to a standalone spec
file spec file, the build time of ceph.spec was reduced and it was no longer
a problem to have ceph in Ring1.

A script, pre_checkin.sh, which is run before every commit, automatically
generates ceph-test.spec from ceph.spec. Thus, ceph-test.spec should be seen
as a "build artifact" whose purpose is to build the ceph-test RPM as it would
have been built had the original ceph.spec not been split.

Although this workflow results in a "not-pretty" ceph-test.spec, it has an
advantage in that ceph-test.spec is maintenance-free. Maintaining *two* spec
files for Ceph would be tricky, error-prone, and labor-intensive.

Nathan Cutler
April 17, 2017
