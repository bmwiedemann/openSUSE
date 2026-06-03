#!/bin/bash
set -euxo pipefail

# Set ownership for the KubeVirt containerdisk artifact to the expected uid:gid.
if [[ "$kiwi_profiles" =~ (^|,)KubeVirt-Cloud(,|$) ]]; then
    chown 107:107 "$1"
fi
