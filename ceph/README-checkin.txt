Use the "checkin.sh" script to generate ceph.spec and tarball from a git repo
and branch.  For example:

    $ bash checkin.sh --repo https://github.com/foo/ceph --branch wip-foo

For more options, try "./checkin.sh --help"


FAQ
===

Q. What is the pre_checkin.sh script?

A. The "pre_checkin.sh" script generates ceph-test.spec from ceph.spec, and
ceph-test.changes from ceph.changes.

Q. Should I run it before running checkin.sh?

A. It doesn't hurt to run it, but no, you don't need to run it because
checkin.sh does that for you.
