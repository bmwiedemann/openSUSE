#
# spec file for package python3-seccomp
#
# Copyright (c) 2025 SUSE LLC
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


%global pname libseccomp
%global lname   libseccomp2
%global flavor @BUILD_FLAVOR@%nil

%if "%flavor" == "python3"
Name:           python3-seccomp
Summary:        Python 3 bindings for seccomp
Group:          Development/Tools/Debuggers
%else
Name:           libseccomp
Summary:        A Seccomp (mode 2) helper library
Group:          Development/Libraries/C and C++
%endif
Version:        2.6.0
Release:        0
License:        LGPL-2.1-only
URL:            https://github.com/seccomp/libseccomp
Source:         https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz
Source2:        https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz.asc
Source3:        %pname.keyring
Source99:       baselibs.conf
Patch1:         make-python-build.patch
BuildRequires:  autoconf
BuildRequires:  automake >= 1.11
BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
%if "%flavor" == "python3"
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython >= 0.29
BuildRequires:  python3-setuptools
%endif

%description
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

%if "%flavor" == "python3"
This subpackage contains the python3 bindings for seccomp.
%endif

%package -n %lname
Summary:        An enhanced Seccomp (mode 2) helper library
Group:          System/Libraries

%description -n %lname
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
%autosetup -p1 -n %pname-%version

%if 0%{?qemu_user_space_build}
# The qemu linux-user emulation does not allow executing
# prctl(PR_SET_SECCOMP), which breaks these tests.  Stub them out.
echo 'int main () { return 0; }' >tests/11-basic-basic_errors.c
echo 'int main () { return 0; }' >tests/52-basic-load.c
%endif

%build
autoreconf -fiv
%configure \
	 --includedir="%_includedir/%pname" \
%if "%flavor" == "python3"
	 --enable-python \
%endif
	 --disable-static \
	 --disable-silent-rules \
	 GPERF=/bin/true
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete
rm -fv %buildroot/%python3_sitearch/install_files.txt
%if "%flavor" == "python3"
rm %buildroot/%_libdir/%pname.so*
rm -r %buildroot/%_mandir/
rm -r %buildroot/%_includedir/%pname/
rm -r %buildroot/%_libdir/pkgconfig
rm -r %buildroot/%_bindir/
%endif
%fdupes %buildroot/%_prefix

%if "%flavor" != "python3"
%check
export LD_LIBRARY_PATH="$PWD/src/.libs"
make check
%endif

%ldconfig_scriptlets -n %lname

%if "%flavor" == "python3"
%files
%python3_sitearch/seccomp*
%else

%files -n %lname
%_libdir/%pname.so.2*
%license LICENSE

%files devel
%_mandir/man3/seccomp_*.3*
%_includedir/%pname/
%_libdir/%pname.so
%_libdir/pkgconfig/%pname.pc

%files tools
%_bindir/scmp_sys_resolver
%_mandir/man1/scmp_sys_resolver.1*
%endif

%changelog
