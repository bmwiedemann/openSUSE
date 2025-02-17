#
# spec file for package pgsql-ogr-fdw
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


%define         pg_name  @BUILD_FLAVOR@%{nil}
%define         ext_name pgsql-ogr-fdw
%{pg_version_from_name}

Name:           %{pg_name}-%{ext_name}
Version:        1.1.5
Release:        0
Summary:        PostgreSQL OGR Foreign Data Wrapper
License:        MIT
Group:          Productivity/Databases/Tools
URL:            https://github.com/pramsey/pgsql-ogr-fdw
Source0:        https://codeload.github.com/pramsey/pgsql-ogr-fdw/tar.gz/v%{version}#/%{ext_name}-%{version}.tar.gz
BuildRequires:  %{pg_name}-llvmjit-devel
BuildRequires:  %{pg_name}-server-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  pkgconfig
%pg_server_requires
%if "%{pg_name}" == ""
Name:           %{ext_name}
ExclusiveArch:  do_not_build
%endif

%description
OGR is the vector half of the GDAL spatial data access library.
It allows access to a large number of GIS data formats using a simple C API for data reading and writing.
Since OGR exposes a simple table structure and PostgreSQL foreign data wrappers allow access to table structures, the fit seems pretty perfect.

%prep
%setup -q -n %{ext_name}-%{version}

%build
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
export PATH="$PATH:%{pg_config_bindir}"
make V=1 USE_PGXS=1 %{?_smp_mflags}

%install
export PATH="$PATH:%{pg_config_bindir}"
# Needed upstream think it is present
mkdir -p %{buildroot}/%{pg_config_bindir}
make V=1 USE_PGXS=1 install DESTDIR=%{buildroot}

%post
%{_datadir}/postgresql/install-alternatives %pg_version

%postun
%{_datadir}/postgresql/install-alternatives %pg_version

%files
%defattr(-, root, root)
%license LICENSE.md
%doc README.md FAQ.md
%{pg_config_bindir}/ogr_fdw_info
%{pg_config_pkglibdir}/ogr_fdw.so
%if %{postgresql_has_llvm}
%{pg_config_pkglibdir}/bitcode/*
%endif
%dir %{pg_config_sharedir}/extension/
%{pg_config_sharedir}/extension/ogr_fdw--1.0--1.1.sql
%{pg_config_sharedir}/extension/ogr_fdw--1.1.sql
%{pg_config_sharedir}/extension/ogr_fdw.control

%changelog
