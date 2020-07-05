#
# spec file for package pgsql-ogr-fdw
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


%define         pgversion @BUILD_FLAVOR@
%define         sname pgsql-ogr-fdw
%define         pg_bindir %(pg_config --bindir)
%define         pg_libdir %(pg_config --pkglibdir)
%define         pg_share %(pg_config --sharedir)
%if 0%{?is_opensuse} && ("%{pgversion}" == "postgresql11" || "%{pgversion}" == "postgresql12") && 0%{?suse_version} >= 1550
%bcond_without  llvm
%else
%bcond_with     llvm
%endif
Version:        1.0.12
Release:        0
Summary:        PostgreSQL OGR Foreign Data Wrapper
License:        MIT
Group:          Productivity/Databases/Tools
URL:            https://github.com/pramsey/pgsql-ogr-fdw
Source0:        https://codeload.github.com/pramsey/pgsql-ogr-fdw/tar.gz/v%{version}#/%{sname}-%{version}.tar.gz
BuildRequires:  %{pgversion}-server
%if "%{pgversion}" == "postgresql11" || "%{pgversion}" == "postgresql12"
BuildRequires:  %{pgversion}-server-devel
%endif
BuildRequires:  %{pgversion}-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  pkgconfig
%requires_eq    %{pgversion}-server
%requires_eq    %{pgversion}-server-llvmjit
%if "%{pgversion}" == "" || "%{pgversion}" == "postgresql"
Name:           %{sname}
ExclusiveArch:  do_not_build
%else
Name:           %{pgversion}-%{sname}
%endif
# Build for pg11&12 but not for Leap 15.1 (due to lack of maintenance)
%if (0%{?is_opensuse} && 0%{?sle_version} == 150100) && ("%{pgversion}" == "postgresql11" || "%{pgversion}" == "postgresql12")
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} < 1315 && %{pgversion} == "postgresql10"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} == 1500 && %{pgversion} == "postgresql95"
ExclusiveArch:  do_not_build
%endif
%if "%{pgversion}" == ""
Name:           %{sname}
ExclusiveArch:  do_not_build
%endif

%description
OGR is the vector half of the GDAL spatial data access library.
It allows access to a large number of GIS data formats using a simple C API for data reading and writing.
Since OGR exposes a simple table structure and PostgreSQL foreign data wrappers allow access to table structures, the fit seems pretty perfect.

%if %{with llvm}
%package llvmjit
Summary:        Just-in-time compilation support for PostgreSQL %{sname} extension
Group:          Productivity/Databases/Tools
Requires:       %{pgversion}-%{sname} = %{version}-%{release}
Requires:       %{pgversion}-llvmjit
Requires:       %{pgversion}-server
Supplements:    (%{pgversion}-llvmjit and %{name})

%description llvmjit
This package contains support for just-in-time compiling parts of
PostgreSQL queries. Using LLVM it compiles e.g. expressions and tuple
deforming into native code, with the goal of accelerating analytics
queries.
%endif

%prep
%setup -q -n %{sname}-%{version}

%build
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
export PATH="$PATH:%{pg_bindir}"
make V=1 USE_PGXS=1 %{?_smp_mflags}

%install
export PATH="$PATH:%{pg_bindir}"
# Needed upstream think it is present
mkdir -p %{buildroot}/%{pg_bindir}
make V=1 USE_PGXS=1 install DESTDIR=%{buildroot}

%post
%{_datadir}/postgresql/install-alternatives %pgversion

%postun
%{_datadir}/postgresql/install-alternatives %pgversion

%files
%defattr(-, root, root)
%license LICENSE.md
%doc README.md FAQ.md
%{pg_bindir}/ogr_fdw_info
%{pg_libdir}/ogr_fdw.so
%dir %{pg_share}/extension/
%{pg_share}/extension/ogr_fdw--1.0.sql
%{pg_share}/extension/ogr_fdw.control

%if %{with llvm}
%files llvmjit
%{pg_libdir}/bitcode/*
%endif

%changelog
