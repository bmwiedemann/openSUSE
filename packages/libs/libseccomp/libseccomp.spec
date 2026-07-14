#
# spec file for package libseccomp
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%if "%flavor" == "python"
%bcond_without python
%define namesuf -%flavor
%else
%bcond_with python
%define namesuf %nil
%endif

Name:           libseccomp%namesuf
Summary:        A Seccomp (mode 2) helper library
Group:          Development/Libraries/C and C++
Version:        2.6.1
Release:        0
License:        LGPL-2.1-only
URL:            https://github.com/seccomp/libseccomp
Source:         https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz
Source2:        https://github.com/seccomp/libseccomp/releases/download/v%version/libseccomp-%version.tar.gz.asc
Source3:        %pname.keyring
Source99:       baselibs.conf
Patch0:         python-pip-packages.patch
Patch1:         make-python-build.patch
Patch3:         modernize-python-build.patch
BuildRequires:  autoconf
BuildRequires:  automake >= 1.11
BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
%if %{with python}
BuildRequires:  %python_module Cython >= 0.29
BuildRequires:  %python_module build
BuildRequires:  %python_module pip
BuildRequires:  %python_module setuptools
BuildRequires:  %python_module wheel
BuildRequires:  ca-certificates-mozilla-prebuilt
BuildRequires:  python-rpm-macros
%define python_subpackage_only 1
%python_subpackages
%endif

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

%if %{with python}
%package -n python-seccomp
Summary:        Python bindings for seccomp
Group:          Development/Tools/Debuggers

%description -n python-seccomp
The libseccomp library provides an interface to the Linux Kernel's
syscall filtering mechanism, seccomp. The libseccomp API abstracts
away the underlying BPF-based syscall filter language and presents a
more conventional function-call based filtering interface.

This subpackage contains the python3 bindings for seccomp.
%endif

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
export LD_LIBRARY_PATH="$PWD/src/.libs${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
%if %{with python}
%{python_expand \
  %configure \
    --includedir="%_includedir/%pname" \
    --enable-python \
    --disable-static \
    --disable-silent-rules \
    GPERF=/bin/true \
    PYTHON=$python
%make_build all python-wheel
}
%else
%configure \
    --includedir="%_includedir/%pname" \
    --disable-static \
    --disable-silent-rules \
    GPERF=/bin/true
%make_build
%endif

%install
%if %{with python}
%{python_expand \
  %make_install PYTHON=$python pyexecdir=%$python_sitearch
}
b="%buildroot"
rm -Rf "$b/%_bindir" "$b/%_libdir"/libsec* "$b/%_libdir/pkgconfig" \
	"$b/%_includedir" "$b/%_datadir"
%else
%make_install
%endif
find "%buildroot/%_libdir" -type f -name "*.la" -delete
%if %{with python}
%python_expand rm -fv %buildroot/%$python_sitearch/install_files.txt
%endif
%fdupes %buildroot/%_prefix

%check
%if %{with python}
export LD_LIBRARY_PATH="$PWD/src/.libs"
%{python_expand \
  make PYTHON=$python PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}%buildroot%{$python_sitearch}" PYTHONDONTWRITEBYTECODE=1 check
}
%endif

%ldconfig_scriptlets -n %lname

%if "%flavor" == ""
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

%if %{with python}
%files %{python_files seccomp}
%python_sitearch/seccomp*.so
%python_sitearch/seccomp-%{version}*-info
%endif

%changelog
