#
# spec file for package pg_cron
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
%define         priority %{pgversion}
%define         sname pg_cron
%define         pg_libdir %(pg_config --pkglibdir)
%define         pg_share %(pg_config --sharedir)
%if 0%{?is_opensuse} && ("%{pgversion}" == "postgresql11" || "%{pgversion}" == "postgresql12" || "%{pgversion}" == "postgresql13") && 0%{?suse_version} >= 1500
%bcond_without  llvm
%else
%bcond_with     llvm
%endif
Name:           %{pgversion}-%{sname}
Version:        1.3.0
Release:        0
Summary:        PostgreSQL module for simple job schedule
License:        PostgreSQL
Group:          Productivity/Databases/Servers
URL:            https://github.com/citusdata/pg_cron
Source:         %{sname}-%{version}.tar.gz
BuildRequires:  %{pgversion}-server
BuildRequires:  %{pgversion}-server-devel
%requires_eq    %{pgversion}-server
%if "%{pgversion}" == ""
Name:           %{sname}
ExclusiveArch:  do_not_build
%endif

%description
%{sname} is a simple cron-based job scheduler for PostgreSQL (9.5 or higher)
that runs inside the database as an extension. It uses the same syntax as
regular cron, but it allows you to schedule PostgreSQL commands directly from
the database.

%if %{with llvm}
%package llvmjit
Summary:        Just-in-time compilation support for PostgreSQL %{sname} extension
Group:          Productivity/Databases/Servers
Requires:       %{pgversion}-%{sname} = %{version}-%{release}
Requires:       %{pgversion}-llvmjit
Requires:       %{pgversion}-server
Supplements:    packageand(%{pgversion}-llvmjit:%{name})

%description llvmjit
This package contains support for just-in-time compiling parts of
PostgreSQL queries. Using LLVM it compiles e.g. expressions and tuple
deforming into native code, with the goal of accelerating analytics
queries.
%endif

%prep
%setup -q -n %{sname}-%{version}

%build
export PATH="$PATH:%{_libexecdir}/%{pgname}/bin"
make %{?_smp_mflags}

%install
%make_install

%post
%{_datadir}/postgresql/install-alternatives %{priority}

%postun
%{_datadir}/postgresql/install-alternatives %{priority}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/%{pgversion}/extension/%{sname}*
%{pg_libdir}/%{sname}.so

%if %{with llvm}
%files llvmjit
%{pg_libdir}/bitcode/*
%endif

%changelog
