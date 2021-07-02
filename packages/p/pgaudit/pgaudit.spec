#
# spec file for package pgaudit
#
# Copyright (c) 2021 SUSE LLC
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


%define         pg_libdir %(pg_config --pkglibdir)

# name_pg uses --keep-name-conditionals (argument of spec_query)
# loophole
%define         name_pg  @BUILD_FLAVOR@%{nil}
%define         sname    pgaudit

%if ("%{name_pg}" == "postgresql11" || "%{name_pg}" == "postgresql12" || "%{name_pg}" == "postgresql13") && 0%{?suse_version} >= 1500
%bcond_without  llvm
%else
%bcond_with     llvm
%endif

%if ("%{name_pg}" == "postgresql95" || "%{name_pg}" == "postgresql96") && 0%{?suse_version} >= 1550
ExclusiveArch:  do_not_build
%endif

%if "%{name_pg}" == ""
# nill flavour
Name:           pgaudit
ExclusiveArch:  do_not_build
%else
Name:           %{name_pg}-pgaudit
%endif
%if "%{name_pg}" == "postgresql95"
Version:        1.0.8
%endif
%if "%{name_pg}" == "postgresql96"
Version:        1.1.3
%endif
%if "%{name_pg}" == "postgresql10"
Version:        1.2.2
%endif
%if "%{name_pg}" == "postgresql11"
Version:        1.3.2
%endif
%if "%{name_pg}" == "postgresql12"
Version:        1.4.1
%endif
%if "%{name_pg}" == "postgresql13"
Version:        1.5.0
%endif
Release:        0
Summary:        An auditing module for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
URL:            https://github.com/pgaudit/pgaudit
%if "%{name_pg}" != ""
# not nill flavour
Source:         %{sname}-%{version}.tar.gz
%endif
BuildRequires:  %{name_pg}-devel
BuildRequires:  %{name_pg}-server
BuildRequires:  %{name_pg}-server-devel
Requires:       %{name_pg}-server
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the initial version of an auditing module for Postgres.

It collects audit events from various sources and logs them in CSV format
including a timestamp, user information, details of objects affected (if any),
and the fully-qualified command text (whenever available).

All DDL, DML (including SELECT), and utility commands are supported. These
are categorised as described below, and audit logging for each group of
commands may be enabled or disabled by the superuser. Once enabled, however,
audit logging may not be disabled by a user.


%if %{with llvm}
%package llvmjit
Summary:        Just-in-time compilation support for PostgreSQL %{sname} extension
Group:          Productivity/Databases/Servers
Requires:       %{name_pg}-%{sname} = %{version}-%{release}
Requires:       %{name_pg}-llvmjit
Requires:       %{name_pg}-server
Supplements:    packageand(%{name_pg}-llvmjit:%{name})

%description llvmjit
This package contains support for just-in-time compiling parts of
PostgreSQL queries. Using LLVM it compiles e.g. expressions and tuple
deforming into native code, with the goal of accelerating analytics
queries.
%endif

%prep
%setup -q -n %{sname}-%{version}

%build
export PATH="$PATH:/usr/lib/%{name_pg}/bin"
make USE_PGXS=1 %{?_smp_mflags}

%install
export PATH="$PATH:/usr/lib/%{name_pg}/bin"
make USE_PGXS=1 install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc README.md LICENSE sql/
%{_prefix}/lib/%{name_pg}/%{_lib}/%{sname}.so
%{_datadir}/%{name_pg}/extension/%{sname}*

%if %{with llvm}
%files llvmjit
%{pg_libdir}/bitcode/*
%endif

%changelog
