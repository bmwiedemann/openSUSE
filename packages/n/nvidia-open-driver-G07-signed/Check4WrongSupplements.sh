#!/bin/sh

if [ $# -ne 1 ]; then
  echo "$0 <rpmdir>"
  exit 1
fi

rpmdir=$1
shift

for rpm in $(find "${rpmdir}" -type f -name "*.rpm"); do
  rpm --supplements -qp $rpm | grep ':pci:v000010DEd\*sv'
  if [ $? -eq 0 ]; then
    echo "*** Wrong supplements in $rpm; again all NVIDIA PCI IDs! ***"
    exit 1
  fi
done

