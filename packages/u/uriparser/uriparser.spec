#
# spec file for package uriparser
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -doc
%else
%define psuffix %{nil}
%endif

%if 0%{?suse_version} >= 1500
%bcond_without googletest
%else
%bcond_with googletest
%endif

%define so_ver  1
Name:           uriparser%{psuffix}
Version:        1.0.2
Release:        0
%if "%{flavor}" == "doc"
Summary:        Documentation files for the uriparser URI parsing library
License:        BSD-3-Clause
Group:          Documentation/Other
%else
Summary:        A strictly RFC 3986 compliant URI parsing library
License:        Apache-2.0 AND BSD-3-Clause AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
%endif
URL:            https://uriparser.github.io
Source:         https://github.com/uriparser/uriparser/releases/download/uriparser-%{version}/uriparser-%{version}.tar.xz
Patch1:         cmake_fixes.patch
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  xz
%if "%{flavor}" == "doc"
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  qt6-tools
BuildRequires:  pkgconfig(libxdot)
%else
BuildRequires:  pkg-config
%if %{with googletest}
BuildRequires:  gtest >= 1.8.1
%endif
Provides:       uriparse = %{version}-%{release}
Obsoletes:      uriparse < %{version}-%{release}
%endif

%description
uriparser is a strictly RFC 3986 compliant URI parsing library
and supports Unicode.

%if "%{flavor}" == "doc"
This package contains the documentation for uriparser.
%else
There is a command line tool, uriparse, which allows parsing URIs and
show how the liburiparser splits it into components.

%package     -n liburiparser%{so_ver}
Summary:        A strictly RFC 3986 compliant URI parsing library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n liburiparser%{so_ver}
uriparser is a strictly RFC 3986 compliant URI parsing library
and supports Unicode.

This package contains the shared library for %{name}.

%package        devel
Summary:        Development files for the uriparser URL parsing library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       liburiparser%{so_ver} = %{version}
Provides:       liburiparser-devel = %{version}-%{release}
Obsoletes:      liburiparser-devel < %{version}-%{release}

%description    devel
uriparser is a strictly RFC 3986 compliant URI parsing library
and supports Unicode.

This subpackage contains the headers and other developments
files needed to build packagesfor that depend on %{name}.
%endif

%prep
%autosetup -p1 -n uriparser-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/uriparser \
    -DCMAKE_CXX_STANDARD=17 \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DURIPARSER_BUILD_CHAR:BOOL=ON \
%if "%{flavor}" == "doc"
    -DURIPARSER_BUILD_DOCS:BOOL=ON \
%else
    -DURIPARSER_BUILD_DOCS:BOOL=OFF \
%if %{with googletest}
    -DURIPARSER_BUILD_TESTS:BOOL=ON \
%else
    -DURIPARSER_BUILD_TESTS:BOOL=OFF \
%endif
%endif
    -DURIPARSER_BUILD_TOOLS:BOOL=ON \
    -DURIPARSER_BUILD_WCHAR:BOOL=ON \
    -DQHG_LOCATION:PATH=%{_libexecdir}/qt6/qhelpgenerator
%cmake_build

%install
%cmake_install
%if "%{flavor}" == "doc"
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_docdir}/uriparser/html/
%else
rm -rf %{buildroot}%{_docdir}/uriparser
%endif

%if "%{flavor}" != "doc"
%if %{with googletest}
%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
%ctest
unset MALLOC_CHECK_ MALLOC_PERTURB_
%endif

%post -n liburiparser%{so_ver} -p /sbin/ldconfig
%postun -n liburiparser%{so_ver} -p /sbin/ldconfig
%endif

%if "%{flavor}" == "doc"
%files
%license COPYING.BSD-3-Clause
%doc doc/Mainpage.txt
%dir %{_docdir}/uriparser/
%{_docdir}/uriparser/html/
%{_docdir}/uriparser/uriparser-%{version}-doc.qch
%else

%files
%license COPYING.BSD-3-Clause
%{_bindir}/uriparse

%files -n liburiparser%{so_ver}
%license COPYING.BSD-3-Clause
%{_libdir}/liburiparser.so.%{so_ver}
%{_libdir}/liburiparser.so.%{so_ver}.*

%files devel
%license COPYING.BSD-3-Clause
%doc ChangeLog THANKS AUTHORS
%{_includedir}/uriparser/
%{_libdir}/liburiparser.so
%{_libdir}/cmake/uriparser-%{version}/
%{_libdir}/pkgconfig/liburiparser.pc
%endif

%changelog
