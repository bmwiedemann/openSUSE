#
# spec file for package liborcus
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%define libname liborcus-0_20-0
%if 0%{?gcc_version} < 13
%define with_gcc 13
%endif
%bcond_without tests
Name:           liborcus
Version:        0.20.2
Release:        0
Summary:        Spreadsheet file processing library
License:        MPL-2.0
URL:            https://gitlab.com/orcus/orcus/
Source:         https://gitlab.com/api/v4/projects/orcus%%2Forcus/packages/generic/source/%{version}/%{name}-%{version}.tar.xz
Patch2:         0003-Allow-running-tests-with-python-3.4.patch
# PATCH-FIX-UPSTREAM
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc%{?with_gcc}
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(libixion-0.20) >= 0.20.0
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
%if 0%{?suse_version} <= 1550
BuildRequires:  libboost_system-devel
%endif
%else
BuildRequires:  boost-devel
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
%ifarch %{ix86}
%global optflags %{optflags} -ffloat-store
%endif

NOCONFIGURE=indeed ./autogen.sh
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
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
