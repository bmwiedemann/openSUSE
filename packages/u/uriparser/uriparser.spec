#
# spec file for package uriparser
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with googletest

%define so_ver  1
Name:           uriparser
Version:        0.9.3
Release:        0
Summary:        A strictly RFC 3986 compliant URI parsing library
License:        BSD-3-Clause AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://uriparser.github.io
Source:         https://github.com/uriparser/uriparser/releases/download/uriparser-%{version}/uriparser-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libqt5-qttools
BuildRequires:  pkg-config
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
%make_jobs

%install
%cmake_install
%fdupes %{buildroot}%{_docdir}/%{name}/html/

%if %{with googletest}
%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
make %{?_smp_mflags} check
unset MALLOC_CHECK_ MALLOC_PERTURB_
%endif

%post -n liburiparser%{so_ver} -p /sbin/ldconfig
%postun -n liburiparser%{so_ver} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/uriparse

%files -n liburiparser%{so_ver}
%license COPYING
%{_libdir}/liburiparser.so.%{so_ver}
%{_libdir}/liburiparser.so.%{so_ver}.*

%files devel
%license COPYING
%doc ChangeLog THANKS AUTHORS
%{_includedir}/%{name}/
%{_libdir}/liburiparser.so
%{_libdir}/cmake/uriparser-%{version}/
%{_libdir}/pkgconfig/liburiparser.pc

%files doc
%license COPYING
%doc doc/Mainpage.txt
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/uriparser-%{version}.qch

%changelog
