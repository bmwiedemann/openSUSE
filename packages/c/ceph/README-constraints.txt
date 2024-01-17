2023-06-13 - Tim Serong <tserong@suse.com>

Ceph needs plenty of disk space and RAM in order to build.  To set
minimum requirements for these, we're using #!BuildConstraint directives
in ceph.spec and ceph-test.spec.  We were previously using a _constraints
file, but this was shown to not always work correctly with _multibuild.
For more information about #!BuildConstraint directives see
https://github.com/openSUSE/obs-docu/pull/285, and in particular Darix's
comment that you shouldn't mix _constraints and #!BuildConstraint.

The #!BuildConstraint directives are added to the spec files automatically
by the pre_checkin.sh script.  If the disk and memory constraints need to
be changed in future, adjust the variables in the pre_checkin.env file and
re-run pre_checkin.sh.

The current constraints are based on builds of ceph 16.2.7 on build.suse.de,
which showed the following resource usage (in MB):

ceph aarch64      max disk: 41568  max mem: 13698 (on ibs-centriq-6:3 disk:  65536 mem: 18432)
ceph x86_64       max disk: 41621  max mem:  9852 (on sheep74:2       disk:  51200 mem: 12500)
ceph ppc64le      max disk: 42005  max mem:  8754 (on ibs-power9-10:1 disk:  61440 mem: 20480)
ceph s390x        max disk: 40698  max mem:  8875 (on s390zl36:1      disk:  51200 mem: 10240)
ceph-test x86_64  max disk: 51760  max mem: 16835 (on sheep94:2       disk: 112640 mem: 16384)

Based on the above, and to hopefully provide a little wiggle room for
the future while at the same time not being too demanding of workers,
the minimum disk size is 50GB for ceph and 60GB for ceph-test.  Memory
requirements remain at 8GB and 10GB respectively as they were before I
did the above tests - despite the memory usage shown above, AFAIK we
haven't run out of memory during builds, and this keeps the pool of
possible workers noticeably larger than it would be if we required 16GB.
