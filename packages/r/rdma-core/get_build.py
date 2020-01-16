#!/usr/bin/python

import rpm

spec = rpm.spec("rdma-core.spec")
print '%s' % (getattr(spec, "build"),)
