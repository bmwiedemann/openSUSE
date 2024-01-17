#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%global pname gflags

%if "%{flavor}" == "static"
%define psuffix -%{flavor}
%bcond_with    build_shared
%bcond_without build_static
%else
%define psuffix %{nil}
%bcond_without build_shared
%bcond_with    build_static
%endif

%define soversion 2_2

Name:           gflags%{psuffix}
Version:        2.2.2
Release:        0
Summary:        Library for commandline flag processing
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/gflags/gflags
Source0:        https://github.com/%{pname}/%{pname}/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
Requires:       libgflags%{soversion} = %{version}

%description
The gflags package contains a library that implements commandline
flags processing. As such, it is a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package -n libgflags%{soversion}
Summary:        Library for commandline flag processing
Conflicts:      libgflags2

%description -n libgflags%{soversion}
The gflags package contains a library that implements commandline
flags processing. As such, it is a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package devel
Summary:        Development files for the dynamic gflags library
Requires:       libgflags%{soversion} = %{version}

%description devel
This package contains all necessary include files and the dynamic libraries
needed for developing applications.

%package -n gflags-devel-static
Summary:        Development files for the static gflags library
# CMake config for static and shared differ, but use the same export file name
Conflicts:      %{pname}-devel

%description -n gflags-devel-static
This package contains all necessary include files and the static libraries
needed for developing applications.

%prep
%autosetup -n gflags-%{version}
# Fix prefix duplication, _libdir is absolute
sed -i -e 's@libdir=.*@libdir=%{_libdir}@' cmake/package.pc.in

%build
%if %{with build_static}
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif
%cmake \
    -DBUILD_STATIC_LIBS:BOOL=%{?with_build_static:ON}%{!?with_build_static:OFF} \
    -DBUILD_SHARED_LIBS:BOOL=%{?with_build_shared:ON}%{!?with_build_shared:OFF} \
    -DBUILD_TESTING:BOOL=ON \
    %{nil}

%cmake_build

%install
%cmake_install

%if "%{flavor}" == "static"
rm %{buildroot}%{_bindir}/%{pname}_completions.sh
mv %{buildroot}%{_libdir}/pkgconfig/%{pname}{,_static}.pc
%endif

# Installs a file on $HOME, remove it
rm -rf %{buildroot}/home/

%check
export LD_LIBRARY_PATH=`pwd`/%{__builddir}/lib
%ctest

%post -n libgflags%{soversion} -p /sbin/ldconfig
%postun -n libgflags%{soversion} -p /sbin/ldconfig

%if "%{flavor}" == ""
%files
%license COPYING.txt
%doc AUTHORS.txt ChangeLog.txt README.md
%{_bindir}/%{pname}_completions.sh

%files -n libgflags%{soversion}
%license COPYING.txt
%{_libdir}/libgflags.so.*
%{_libdir}/libgflags_nothreads.so.*

%files devel
%{_includedir}/%{pname}/
%{_libdir}/libgflags.so
%{_libdir}/libgflags_nothreads.so
%{_libdir}/cmake/%{pname}/
%{_libdir}/pkgconfig/%{pname}.pc
%endif

%if "%{flavor}" == "static"
%files -n gflags-devel-static
%{_includedir}/%{pname}/
%{_libdir}/cmake/%{pname}/
%{_libdir}/pkgconfig/%{pname}_static.pc
%{_libdir}/libgflags.a
%{_libdir}/libgflags_nothreads.a
%endif

%changelog
