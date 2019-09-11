#!/bin/bash
# This script is called automatically during autobuild checkin.

version=$(grep '^Version:.*' kdelibs4.spec)
for change in kdelibs4-apidocs; do
    cp -f kdelibs4.changes $change.changes
    sed -i -e "s,Version:.*,$version," ${change}.spec
done
