#!/bin/bash
if [ -e %{_sysconfdir}/spack/no_rpm_trigger ] ; then
  exit 0
fi
if [ "x$(id -u)" != "x0" ] ; then
  echo "Must run as root, in order to copy back the configuration files and use sudo"
  exit 0
fi

echo "Create /etc/spack/no_rpm_trigger to stop spack to search for new packages after a rpm install"
# save old packages.yml, it has to be removed as when not
# the new and old packages.yaml files would have to be 
# combined
test -e  /etc/spack/packages.yaml && mv /etc/spack/packages.yaml /etc/spack/packages.yaml.old
# prepare the path
mypath=/usr/lib64/mpi/gcc/openmpi4/bin
mypath=/usr/lib64/mpi/gcc/openmpi3/bin:${mypath}
mypath=/usr/lib64/mpi/gcc/openmpi2/bin:${mypath}
mypath=/usr/lib64/mpi/gcc/openmpi1/bin:${mypath}
mypath=/usr/lib64/mpi/gcc/mvapich2/bin:${mypath}
mypath=/usr/lib64/mpi/gcc/mpich/bin:${mypath}
# test if we can run as nobody
getent passwd nobody &> /dev/null
if [ "x$?" == "x0" ] ; then
# drop all root rights, when calling external find
  sudo -u nobody PATH=${mypath}:${PATH} spack external find --scope user --exclude 'installdbgsymbols' 
  if [ -e /var/lib/nobody/.spack/packages.yaml ] ; then
    mv -v /var/lib/nobody/.spack/packages.yaml /etc/spack/packages.yaml
    chown root:root /etc/spack/packages.yaml
    rm -r /var/lib/nobody/.spack
  fi
else
  # May run in a container...
  PATH=${mypath}:${PATH} spack external find --scope system --exclude 'installdbgsymbols' 
fi
