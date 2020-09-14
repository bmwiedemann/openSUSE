#
# spec file for package libseccomp
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


%define lname   libseccomp2
Name:           libseccomp
Version:        2.5.0
Release:        0
Summary:        A Seccomp (mode 2) helper library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/seccomp/libseccomp
Source:         https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz
Source2:        https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz.asc
Source3:        %name.keyring
Source99:       baselibs.conf
Patch:          testsuite-riscv64-missing-syscalls.patch
BuildRequires:  autoconf
BuildRequires:  automake >= 1.11
BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig

%description
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

%package -n %lname
Summary:        An enhanced Seccomp (mode 2) helper library
Group:          System/Libraries

%description -n %lname
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

%package -n python-%name
Summary:        Python bindings for Seccomp (mode 2)
Group:          Development/Languages/Python

%description -n python-%name
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

%package devel
Summary:        Development files for libseccomp, an enhanced Seccomp (mode 2) helper library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

This package contains the development files for libseccomp.

%package tools
Summary:        Utilities for the seccomp API
Group:          Development/Tools/Debuggers

%description tools
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp.

This subpackage contains debug utilities for the seccomp interface.

%prep
%autosetup -p1

%if 0%{?qemu_user_space_build}
# The qemu linux-user emulation does not allow executing
# prctl(PR_SET_SECCOMP), which breaks this test.  Stub it out.
echo 'int main () { return 0; }' >tests/52-basic-load.c
%endif

%build
if [ ! -f configure ]; then
	perl -i -pe 's{\QAC_INIT([libseccomp], [0.0.0])\E}{AC_INIT([libseccomp], [%version])}' configure.ac
fi
autoreconf -fiv
%configure \
    --includedir="%_includedir/%name" \
    --disable-static \
    --disable-silent-rules \
    GPERF=/bin/true
make %{?_smp_mflags}

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete
%fdupes %buildroot/%_prefix

%check
make check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/%name.so.2*
%license LICENSE

%files devel
%_mandir/man3/seccomp_*.3*
%_includedir/%name/
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%files tools
%_bindir/scmp_sys_resolver
%_mandir/man1/scmp_sys_resolver.1*

%changelog
