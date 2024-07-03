#
# spec file for package timescaledb
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


%define         pg_name  @BUILD_FLAVOR@%{nil}
%define         ext_name   timescaledb
%{pg_version_from_name}

Name:           %{pg_name}-%{ext_name}
Version:        2.15.3
Release:        0
Summary:        A time-series database extension for PostgreSQL
License:        Apache-2.0
Group:          Productivity/Databases/Tools
URL:            https://www.timescale.com/
Source:         https://github.com/timescale/%{ext_name}/archive/%{version}/%{ext_name}-%{version}.tar.gz
Source1:        series

BuildRequires:  %{pg_name}-server-devel
BuildRequires:  cmake >= 3.11
%pg_server_requires
%if "%{pg_name}" == ""
ExclusiveArch:  do_not_build
Name:           %{ext_name}
%endif

%description
TimescaleDB is a database for making SQL more scalable for
time-series data. It is engineered up from PostgreSQL, providing
automatic partitioning across time and space (partitioning key), as
well as full SQL support.

TimescaleDB is packaged as a PostgreSQL extension.

This build includes only Apache2 modules;
TSL (timescale licenced modules are not built).

%prep
%autosetup -p1 -n %{ext_name}-%{version}

%build
%cmake -DAPACHE_ONLY=1 -DSEND_TELEMETRY_DEFAULT=OFF -DREGRESS_CHECKS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE-APACHE NOTICE LICENSE
%doc README.md CONTRIBUTING.md CHANGELOG.md
%{pg_config_pkglibdir}/%{ext_name}*.so
%{pg_config_sharedir}/extension/%{ext_name}*

%changelog
