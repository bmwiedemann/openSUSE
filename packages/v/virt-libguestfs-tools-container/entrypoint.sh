#!/bin/bash -xe

# KubeVirt will provide LIBGUESTFS_PATH via the pod environemnt. Unset it so the
# default search paths are used.
unset LIBGUESTFS_PATH

/bin/bash
