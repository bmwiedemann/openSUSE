#
# spec file for package kernel-installation-tapeipl
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kernel-installation-tapeipl
BuildRequires:  kernel-source
Version:        MACRO
Release:        0
Summary:        Installation Kernel for IPL from Tape
License:        GPL-2.0
Group:          System/Kernel
AutoReqProv:    off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  s390 s390x

%description
Installation kernel with IPL record for IPL from tape usually for
installation of SLES to LPAR without IPL from CD-ROM or server
available and no z/VM available that can be used do the installation
for LPAR. Only suitable for booting into RAM disks and only used
internally to provide the kernel image with tape IPL record for the
installation CD.

%define current_package_name %{name}
%define kernel_source        `rpm -qf /usr/src/linux --qf '%%{name}'`

%prep
# Nothing to do here.

%build
# Set make options to allow build in build dir of read-only sources
MAKE_OPTS="-C /usr/src/linux O=$(pwd)"
# Initialize the build area
make ${MAKE_OPTS} distclean
# Properly prepare the .config file to built the Tape IPL
sed 's/# \(CONFIG_IPL_TAPE\) is not set/\1=y/;s/CONFIG_IPL_VM=y/# CONFIG_IPL_VM is not set/' /usr/src/linux/arch/s390/defconfig >.config
make ${MAKE_OPTS} oldconfig
# Add some comments to identify the source of this kernel build
{
    echo "
#
# Latest changes in the kernel source used for building 
# (source package: kernel-source):
#"
    rpm -qi --changelog kernel-source | sed 's/^/# /'
} >> .config
# Find the number of CPUs in order to optimize the build
let GCCMEM="15*1024*1024"
set -- `cat /proc/meminfo | head -2 | tail -1`
# 1GB of memory is enough and bash cannot use nums >2^31 (singed int)
if [ ${#2} -gt 9 ] ; then
    PARALLEL_BY_RAM=32
else
    let MEM="$2-60*1024*1024"
    let PARALLEL_BY_RAM="$MEM/$GCCMEM"
fi
if [ $PARALLEL_BY_RAM -lt 1 ] ; then
    PARALLEL_BY_RAM=1
fi
PARALLEL_BY_CPU=$(sed -n 's/# processors    : //p' /proc/cpuinfo)
PARALLEL=-j$(($PARALLEL_BY_RAM < $PARALLEL_BY_CPU ? 
              $PARALLEL_BY_RAM : $PARALLEL_BY_CPU))
# Build the kernel
make $PARALLEL ${MAKE_OPTS} image

%install
# %include %{SOURCE2}
install -m 755 -d ${RPM_BUILD_ROOT}/boot/%{name}
install -m 755 arch/s390/boot/image ${RPM_BUILD_ROOT}/boot/%{name}
install -m 644 .config              ${RPM_BUILD_ROOT}/boot/%{name}/config
install -m 644 System.map           ${RPM_BUILD_ROOT}/boot/%{name}/System.map-%{version}
# These files will be placed in the documentation directory
bzip2 -9 < vmlinux > vmlinux.bz2
rpm -qil --changelog kernel-source > kernel-source.changes

%files
%defattr(-,root,root)
%doc vmlinux.bz2 *.changes
/boot/%{name}
# rdripl contains the /lib/modules:

%changelog
