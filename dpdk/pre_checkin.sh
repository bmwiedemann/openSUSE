#!/bin/sh

# Start fresh
for f in spec changes; do
    cp dpdk.$f dpdk-thunderx.$f || exit 1
done

#
#- Add comment about generated file
#- Fix {,sub-}package name, description, summary
#- Enable the dpdk conditional build
sed -i -e "/^Name:.*dpdk$/i \
# Do NOT edit this auto generated file! Edit dpdk.spec instead\n\
# and run 'pre_checkin.sh' before committing" \
-e "/^#\s*spec file/s/dpdk$/&-thunderx/" \
-e "/^Name:/s/dpdk/&-thunderx/g" \
-e "/^Summary:/s/^.*$/&\ \(thunderx\)/g" \
-e "/^%define machine2 armv8a/s/armv8a/thunderx/g" \
-e "/ExclusiveArch/c\ExclusiveArch:  aarch64" \
dpdk-thunderx.spec || exit 1
