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


%if 0%{?suse_version} >= 1500
%bcond_without googletest
%else
%bcond_with googletest
%endif

%define so_ver  1
Name:           uriparser
Version:        1.0.0
Release:        0
Summary:        A strictly RFC 3986 compliant URI parsing library
License:        Apache-2.0 AND BSD-3-Clause AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://uriparser.github.io
Source:         https://github.com/uriparser/uriparser/releases/download/uriparser-%{version}/uriparser-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  pkg-config
BuildRequires:  qt6-tools
BuildRequires:  xz
BuildRequires:  pkgconfig(libxdot)
%if %{with googletest}
BuildRequires:  gtest >= 1.8.1
%endif
Provides:       uriparse = %{version}-%{release}
Obsoletes:      uriparse < %{version}-%{release}

%description
uriparser is a strictly RFC 3986 compliant URI parsing library
and supports Unicode.

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

%package        doc
Summary:        Documentation files for the uriparser URI parsing library
License:        BSD-3-Clause
Group:          Documentation/Other

%description    doc
uriparser is a strictly RFC 3986 compliant URI parsing library
and supports Unicode.

This subpackage contains the documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DURIPARSER_BUILD_CHAR:BOOL=ON \
    -DURIPARSER_BUILD_DOCS:BOOL=ON \
%if %{with googletest}
    -DURIPARSER_BUILD_TESTS:BOOL=ON \
%else
    -DURIPARSER_BUILD_TESTS:BOOL=OFF \
%endif
    -DURIPARSER_BUILD_TOOLS:BOOL=ON \
    -DURIPARSER_BUILD_WCHAR:BOOL=ON \
    -DQHG_LOCATION:PATH=%{_libexecdir}/qt6/qhelpgenerator
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_docdir}/%{name}/html/

%if %{with googletest}
%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
%ctest
unset MALLOC_CHECK_ MALLOC_PERTURB_
%endif

%post -n liburiparser%{so_ver} -p /sbin/ldconfig
%postun -n liburiparser%{so_ver} -p /sbin/ldconfig

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
%{_includedir}/%{name}/
%{_libdir}/liburiparser.so
%{_libdir}/cmake/uriparser-%{version}/
%{_libdir}/pkgconfig/liburiparser.pc

%files doc
%license COPYING.BSD-3-Clause
%doc doc/Mainpage.txt
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/%{name}-%{version}-doc.qch

%changelog
