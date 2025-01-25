#
# spec file for package pgvector
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
%define         ext_name   pgvector
%if "%{pg_name}" == ""
%global main_build 1
%else
%global main_build 0
%{pg_version_from_name}
%endif

%if %{main_build}
Name:           %{ext_name}
BuildRequires:  postgresql-server-devel
%else
Name:           %{pg_name}-%{ext_name}
BuildRequires:  %{pg_name}-server-devel
%pg_server_requires
%endif
Version:        0.8.0
Release:        0
Summary:        Open-source vector similarity search for Postgres
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            https://github.com/pgvector/pgvector
Source:         https://github.com/pgvector/%{ext_name}/archive/refs/tags/v%{version}.tar.gz#/%{ext_name}-%{version}.tar.gz
Patch0:         https://github.com/pgvector/pgvector/pull/764.patch#/reproducible.patch

%description
Store your vectors with the rest of your data. Supports:

exact and approximate nearest neighbor search
L2 distance, inner product, and cosine distance
any language with a Postgres client
Plus ACID compliance, point-in-time recovery, JOINs, and all of the other great features of Postgres

%package devel
Summary:        Development files for pgvector

%description devel
This package holds the development files to build other extensions to support pgvector.

%prep
%autosetup -p1 -n %{ext_name}-%{version}

%build
%make_pgxs

%install
%make_install
%if %{main_build}
rm -rv %{buildroot}%{pg_config_pkglibdir}/vector* %{buildroot}%{pg_config_sharedir}/extension/vector*
%else
rm -rv %{buildroot}%{pg_config_pkgincludedir}/server/extension/vector/
%endif

%if %{main_build}
%files devel
%{pg_config_pkgincludedir}/server/extension/vector/

%else

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{pg_config_pkglibdir}/vector*.so
%{pg_config_sharedir}/extension/vector*

%endif

%changelog
