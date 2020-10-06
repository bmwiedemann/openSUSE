#
# spec file for package linux-glibc-devel
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           linux-glibc-devel
Version:        5.8
Release:        0
Summary:        Linux headers for userspace development
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://www.kernel.org/
Source:         %{name}-%{version}.tar.xz
Source1:        install_all.sh
BuildRequires:  fdupes
BuildRequires:  xz
# rpm-build requires gettext-tools; ignore this, in order to shorten cycles (we have no translations)
#!BuildIgnore:  gettext-tools
# glibc-devel requires linux-kernel-headers, which we are in progress of building
#!BuildIgnore:  linux-kernel-headers
PreReq:         coreutils
Provides:       kernel-headers
Provides:       linux-kernel-headers = %{version}
Obsoletes:      linux-kernel-headers < %{version}
%global kernel_arch %_target_cpu
%ifarch x86_64 %ix86
%global kernel_arch x86
%endif
%ifarch ppc ppc64 ppc64le
%global kernel_arch powerpc
%endif
%ifarch %arm
%global kernel_arch arm
%endif
%ifarch aarch64
%global kernel_arch arm64
%endif
%ifarch riscv64
%global kernel_arch riscv
%endif
%ifarch s390x
%global kernel_arch s390
%endif
%ifarch hppa
%global kernel_arch parisc
%endif
%ifarch sparc64
%global kernel_arch sparc
%endif

%description
This package provides Linux kernel headers, the kernel API description
required for compilation of almost all programs. This is the userspace
interface; compiling external kernel modules requires
kernel-(flavor)-devel, or kernel-syms to pull in all kernel-*-devel,
packages, instead.

%prep
%setup -q -n linux-glibc-devel-%{version}

%build
cd %{kernel_arch}
cat > version.h <<\BOGUS
#ifdef __KERNEL__
#error "======================================================="
#error "You should not include %{_includedir}/{linux,asm}/ header"
#error "files directly for the compilation of kernel modules."
#error ""
#error "glibc now uses kernel header files from a well-defined"
#error "working kernel version (as recommended by Linus Torvalds)"
#error "These files are glibc internal and may not match the"
#error "currently running kernel. They should only be"
#error "included via other system header files - user space"
#error "programs should not directly include <linux/*.h> or"
#error "<asm/*.h> as well."
#error ""
#error "Since Linux 2.6, the kernel module build process has been"
#error "updated such that users building modules should not typically"
#error "need to specify additional include directories at all."
#error ""
#error "To build kernel modules, ensure you have the build environment "
#error "available either via the kernel-devel and kernel-<flavor>-devel "
#error "packages or a properly configured kernel source tree."
#error ""
#error "Then, modules can be built using:"
#error "make -C <path> M=$PWD"
#error ""
#error "For the currently running kernel there will be a symbolic "
#error "link pointing to the build environment located at "
#error "/lib/modules/$(uname -r)/build for use as <path>."
#error ""
#error "If you are seeing this message, your environment is "
#error "not configured properly. "
#error ""
#error "Please adjust the Makefile accordingly."
#error "======================================================="
#else
BOGUS
# Get LINUX_VERSION_CODE and KERNEL_VERSION directly from kernel
cat usr/include/linux/version.h >> version.h
cat >> version.h <<\BOGUS
#endif
BOGUS
cat version.h

%install
cd %{kernel_arch}
cp -a usr %{buildroot}/
cp -a version.h %{buildroot}%{_includedir}/linux/
# resolve file conflict with glibc for now
rm -fv   %{buildroot}/%{_includedir}/scsi/scsi.h
%fdupes %{buildroot}%{_includedir}

%pre
if test -L %{_includedir}/asm; then
  rm -f %{_includedir}/asm
fi

%files
%defattr(-,root,root)
%{_includedir}/*

%changelog
