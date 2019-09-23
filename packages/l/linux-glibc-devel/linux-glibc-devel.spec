#
# spec file for package linux-glibc-devel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        5.2
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
BuildArch:      noarch

%description
This package provides Linux kernel headers, the kernel API description
required for compilation of almost all programs. This is the userspace
interface; compiling external kernel modules requires
kernel-(flavor)-devel, or kernel-syms to pull in all kernel-*-devel,
packages, instead.

%prep
%setup -q -n linux-glibc-devel-%{version}

%build
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
cp -a usr %{buildroot}/
cp -a version.h %{buildroot}%{_includedir}/linux/
# resolve file conflict with glibc for now
rm -fv   %{buildroot}/%{_includedir}/scsi/scsi.h
# Replace the directory /usr/include/asm with a symlink.
# libc contained a symlink /usr/include/asm into kernel-source up to 7.0 (2.1.3)
# glibc-devel contained a symlink /usr/include/asm into kernel-source in 7.1 (2.2)
# glibc-devel contained a directory /usr/include/asm from 7.2 (2.2.2) up to 10.1/SLES10 (2.4)
# The directory moved from glibc-devel to linux-kernel-headers in 10.2 (2.6.18.2)
# The directory turned into a symlink in 10.3 (2.6.22)
# rpm will remove obsolete files after the post install scripts
# A trigger will run after the /usr/include/asm was removed
# Create a dummy symlink now for rpmlint happiness, we %%ghost this and create
# a proper symlink during %%post:
ln -sfn asm-dummy %{buildroot}%{_includedir}/asm
%fdupes %{buildroot}%{_includedir}

%postun
if test "$1" = 0
then
	rm -f %{_includedir}/asm
fi
exit 0

%post
asm_link=
case "$(uname -m)" in
	alpha*)  asm_link=alpha      ;;
	ppc*)    asm_link=powerpc    ;;
	s390*)   asm_link=s390       ;;
	ia64)    asm_link=ia64       ;;
	*arm*)   asm_link=arm        ;;
	parisc)  asm_link=parisc     ;;
	*mips*)  asm_link=mips       ;;
	sparc*)  asm_link=sparc      ;;
	aarch64) asm_link=arm64      ;;
	m68k)    asm_link=m68k       ;;
	riscv*)  asm_link=riscv      ;;
	*)       asm_link=x86  ;;
esac
if test -L %{_includedir}/asm
then
	case "$(readlink %{_includedir}/asm)" in
		*../src/linux/include*)
		echo "%{_includedir}/asm points to kernel-source, waiting for triggerpostun to symlink to arch-$asm_link/asm"
		rm -fv %{_includedir}/asm
		exit 0
		;;
	esac
	# symlink is ok, update it below in case of an arch change
elif test -d %{_includedir}/asm
then
	echo "%{_includedir}/asm is a directory, waiting for triggerpostun to symlink to arch-$asm_link/asm"
	exit 0
fi
ln -sfn arch-$asm_link/asm %{_includedir}/asm
exit 0

%triggerpostun -- linux-kernel-headers, glibc-devel < 2.5, libc < 2.2
asm_link=
case "$(uname -m)" in
	alpha*)  asm_link=alpha      ;;
	ppc*)    asm_link=powerpc    ;;
	s390*)   asm_link=s390       ;;
	ia64)    asm_link=ia64       ;;
	*arm*)   asm_link=arm        ;;
	parisc)  asm_link=parisc     ;;
	*mips*)  asm_link=mips       ;;
	sparc*)  asm_link=sparc      ;;
	aarch64) asm_link=arm64      ;;
	m68k)    asm_link=m68k       ;;
	riscv*)  asm_link=riscv      ;;
	*)       asm_link=x86  ;;
esac
ln -sfn arch-$asm_link/asm %{_includedir}/asm
exit 0

%files
%defattr(-,root,root)
%{_includedir}/*
%ghost %{_includedir}/asm

%changelog
