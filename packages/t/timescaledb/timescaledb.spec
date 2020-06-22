#
# spec file for package timescaledb
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


%define         pgname  @BUILD_FLAVOR@%{nil}
%define         sname   timescaledb
%define         priority    %{pgname}
Version:        1.7.1
Release:        0
Summary:        A time-series database extension for PostgreSQL
License:        Apache-2.0
Group:          Productivity/Databases/Tools
URL:            https://www.timescale.com/
Source:         https://github.com/timescale/%{sname}/archive/%{version}/%{sname}-%{version}.tar.gz
Patch0:         clang-format9_support.diff
BuildRequires:  %{pgname}-server
BuildRequires:  %{pgname}-server-devel
BuildRequires:  clang
BuildRequires:  cmake >= 3.4
BuildRequires:  fdupes
BuildRequires:  update-alternatives
%requires_eq    %{pgname}-server
%if "%{pgname}" == ""
Name:           %{sname}
ExclusiveArch:  do_not_build
%else
Name:           %{pgname}-%{sname}
%endif

%description
TimescaleDB is a database for making SQL more scalable for
time-series data. It is engineered up from PostgreSQL, providing
automatic partitioning across time and space (partitioning key), as
well as full SQL support.

TimescaleDB is packaged as a PostgreSQL extension.

This build includes only Apache2 modules;
TSL (timescale licenced modules are not built).

This build only Apache2 modules,
TSL (timescale licenced modules are not build)

%prep
%setup -q -n %{sname}-%{version}
# Remove static .so
rm -fv %{sname}.so
%autopatch -p1

%build
export PATH="$PATH:%{_prefix}/lib/%{pgname}/bin"
# No-as-needed is mandatory for Build on Leap42/SLE12
# Force build of only Apache2(community)
%cmake -DAPACHE_ONLY=1 \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--no-as-needed -Wl,--no-undefined -Wl,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--no-as-needed" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-as-needed -Wl,--no-undefined -Wl,-z,now" \
    -DREGRESS_CHECKS=OFF \
  ..

make USE_PGXS=1 %{?_smp_mflags}

%install
export PATH="$PATH:%{_prefix}/lib/%{pgname}/bin"
%cmake_install USE_PGXS=1 install DESTDIR=%{buildroot}

%fdupes %{buildroot}/%{_datadir}/%{pgname}/extension

#%%check
# Need to be finished when we found pg_regress

%files
%defattr(-,root,root)
%license LICENSE-APACHE NOTICE
%doc README.md CONTRIBUTING.md CHANGELOG.md docs
%{_prefix}/lib/%{pgname}/%{_lib}/%{sname}*.so
%{_datadir}/%{pgname}/extension/%{sname}*

%changelog
