#
# spec file for package pgaudit
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


# name_pg uses --keep-name-conditionals (argument of spec_query)
# loophole
%define         name_pg  @BUILD_FLAVOR@%{nil}
# the name_pg define is needed internally by pg_* macros - but we can't use it in conditions
%define         pg_name %name_pg
%define         ext_name    pgaudit
%{pg_version_from_name}

%if "%{name_pg}" == ""
# nill flavour
Name:           pgaudit
ExclusiveArch:  do_not_build
%else
Name:           %{name_pg}-pgaudit
%endif
%if "%{name_pg}" == "postgresql13"
Version:        1.5.2
%endif
# you need to update both the Version: field and the define below for the factory check
%if "%{name_pg}" == "postgresql14"
Version:        1.6.2
%endif
%if "%{name_pg}" == "postgresql15"
Version:        1.7.0
%endif
%if "%{name_pg}" == "postgresql16"
Version:        16.0
%endif
%if "%{name_pg}" == "postgresql17"
Version:        17.0
%endif
Release:        0
Summary:        An auditing module for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            https://github.com/pgaudit/pgaudit
%if "%{name_pg}" != ""
# not nill flavour
Source:         %https://github.com/pgaudit/pgaudit/archive/refs/tags/%{version}.tar.gz#/%{ext_name}-%{version}.tar.gz
%else
# Track the existance of get-tars
Source99:       get-tars
%endif

BuildRequires:  %{pg_name}-llvmjit-devel
%pg_server_requires
%if "%{name_pg}" == ""
ExclusiveArch:  do_not_build
%endif

%description
This is the initial version of an auditing module for Postgres.

It collects audit events from various sources and logs them in CSV format
including a timestamp, user information, details of objects affected (if any),
and the fully-qualified command text (whenever available).

All DDL, DML (including SELECT), and utility commands are supported. These
are categorised as described below, and audit logging for each group of
commands may be enabled or disabled by the superuser. Once enabled, however,
audit logging may not be disabled by a user.

%prep
%autosetup -p1 -n %{ext_name}-%{version}

%build
%make_pgxs

%install
%make_pgxs_install

%files
%doc README.md LICENSE sql/
%{pg_config_pkglibdir}/%{ext_name}.so
%{pg_config_sharedir}/extension/%{ext_name}*
%if %{postgresql_has_llvm}
%{pg_config_pkglibdir}/bitcode/*
%endif

%changelog
