#
# spec file for package liborcus
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


%define libname liborcus-0_16-0
Name:           liborcus
Version:        0.16.1
Release:        0
Summary:        Spreadsheet file processing library
License:        MPL-2.0
URL:            https://gitlab.com/orcus/orcus/
Source:         http://kohei.us/files/orcus/src/%{name}-%{version}.tar.xz
BuildRequires:  coreutils
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(libixion-0.16)
BuildRequires:  pkgconfig(mdds-1.5)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc8
BuildRequires:  gcc8-c++
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
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
%setup -q

%build
%if 0%{?suse_version} < 1500
export CC=gcc-8
export CXX=g++-8
%endif
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-debug \
	--disable-werror \
	--docdir=%{_docdir}/%{name}
%make_build

%check
%if 0%{?suse_version} >= 1500
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
