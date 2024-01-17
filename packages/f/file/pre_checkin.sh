#!/bin/bash
# This script is called automatically during autobuild checkin.
version=$(grep '^Version:.*' file.spec)
sed -ri "s,^Version:.*,$version," python-magic.spec
