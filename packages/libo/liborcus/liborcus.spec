#
# spec file for package liborcus
#
# Copyright (c) 2024 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%bcond_without tests
%define libname liborcus-0_18-0
Name:           liborcus
Version:        0.19.2
Release:        0
Summary:        Spreadsheet file processing library
License:        MPL-2.0
URL:            https://gitlab.com/orcus/orcus/
Source:         http://kohei.us/files/orcus/src/%{name}-%{version}.tar.xz
Patch2:         0003-Allow-running-tests-with-python-3.4.patch
# PATCH-FIX-UPSTREAM
Patch3:         liborcus-0.19.2-gcc15-cstdint.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(libixion-0.18) >= 0.19.0
BuildRequires:  pkgconfig(mdds-2.1) >= 2.0.99
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc >= 7
BuildRequires:  gcc-c++ >= 7
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif

%package -n %{libname}
Summary:        Spreadsheet file processing library

%description -n %{libname}
Standalone file import filter library for spreadsheet documents. Currently
under development are ODS, XLSX and CSV import filters.

%description
Standalone file import filter library for spreadsheet documents. Currently
under development are ODS, XLSX and CSV import filters.

%package devel
Summary:        Spreadsheet file processing library
Requires:       %{libname} = %{version}
Requires:       pkgconfig(zlib)

%description devel
Standalone file import filter library for spreadsheet documents. Currently
under development are ODS, XLSX and CSV import filters.

%package tools
Summary:        Spreadsheet file processing library
Requires:       %{libname} = %{version}

%description tools
Tools to work with various xml streams.

%package -n python3-%{name}
Summary:        Python bindings for liborcus
Provides:       %{name}-python3 = %{version}

%description -n python3-%{name}
Python 3 bindings for %{name}.

%prep
%autosetup -p1

%build
%global optflags %{optflags} -fexcess-precision=fast

# The test-suite of the package expects the precision of FP operations
# to be lower than that of internal representation of 80387.  Use
# option -ffloat-store to mitigate that.
%ifarch i386 i486 i586 i686
%global optflags %{optflags} -ffloat-store
%endif

NOCONFIGURE=indeed ./autogen.sh
%if 0%{?suse_version} < 1500
export CC=gcc-7
export CXX=g++-7
%endif
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-debug \
	--disable-werror \
	--docdir=%{_docdir}/%{name}
%make_build

%if %{with tests}
%check
%make_build check
%endif

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/*

%files -n python3-%{name}
%dir %{python3_sitelib}/orcus/
%{python3_sitelib}/orcus/*
%{python3_sitearch}/_orcus.so
%{python3_sitearch}/_orcus_json.so

%changelog
