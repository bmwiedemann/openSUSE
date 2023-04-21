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


%define         pg_flavor @BUILD_FLAVOR@
%define         sname pgsql-ogr-fdw
%define         pg_bindir %(pg_config --bindir)
%define         pg_libdir %(pg_config --pkglibdir)
%define         pg_share %(pg_config --sharedir)
%if 0%{?is_opensuse} && ("%{pg_flavor}" == "postgresql11" || "%{pg_flavor}" == "postgresql12" || "%{pg_flavor}" == "postgresql13")
%bcond_without  llvm
%else
%bcond_with     llvm
%endif
Version:        1.1.0
Release:        0
Summary:        PostgreSQL OGR Foreign Data Wrapper
License:        MIT
Group:          Productivity/Databases/Tools
URL:            https://github.com/pramsey/pgsql-ogr-fdw
Source0:        https://codeload.github.com/pramsey/pgsql-ogr-fdw/tar.gz/v%{version}#/%{sname}-%{version}.tar.gz
BuildRequires:  %{pg_flavor}-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  pkgconfig
%requires_eq    %{pg_flavor}-server
BuildRequires:  %{pg_flavor}-server
%if "%{pg_flavor}" == "postgresql11" || "%{pg_flavor}" == "postgresql12" || "%{pg_flavor}" == "postgresql13"
BuildRequires:  %{pg_flavor}-server-devel
%if %{with llvm}
BuildRequires:  %{pg_flavor}-llvmjit
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
%endif
%endif
%if "%{pg_flavor}" == "" || "%{pg_flavor}" == "postgresql"
Name:           %{sname}
ExclusiveArch:  do_not_build
%else
Name:           %{pg_flavor}-%{sname}
%endif
# Build for pg11&12 but not for Leap 15.1 (due to lack of maintenance)
%if (0%{?is_opensuse} && 0%{?sle_version} == 150100) && ("%{pg_flavor}" == "postgresql11" || "%{pg_flavor}" == "postgresql12")
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} < 1315 && "%{pg_flavor}" == "postgresql10"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} >= 1500 && "%{pg_flavor}" == "postgresql95"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version} >= 1550 && "%{pg_flavor}" == "postgresql96"
ExclusiveArch:  do_not_build
%endif
%if "%{pg_flavor}" == ""
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
Requires:       %{pg_flavor}-%{sname} = %{version}-%{release}
Requires:       %{pg_flavor}-llvmjit
Requires:       %{pg_flavor}-server
Supplements:    (%{pg_flavor}-llvmjit and %{name})

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
%{_datadir}/postgresql/install-alternatives %pg_flavor

%postun
%{_datadir}/postgresql/install-alternatives %pg_flavor

%files
%defattr(-, root, root)
%license LICENSE.md
%doc README.md FAQ.md
%{pg_bindir}/ogr_fdw_info
%{pg_libdir}/ogr_fdw.so
%dir %{pg_share}/extension/
%{pg_share}/extension/ogr_fdw--1.0--1.1.sql
%{pg_share}/extension/ogr_fdw--1.1.sql
%{pg_share}/extension/ogr_fdw.control

%if %{with llvm}
%files llvmjit
%{pg_libdir}/bitcode/*
%endif

%changelog
