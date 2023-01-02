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


%define         pg_name @BUILD_FLAVOR@%{nil}
%define         ext_name pg_cron
%{pg_version_from_name}

Name:           %{pg_name}-%{ext_name}
Version:        1.4.2
Release:        0
Summary:        PostgreSQL module for simple job schedule
License:        PostgreSQL
Group:          Productivity/Databases/Servers
URL:            https://github.com/citusdata/pg_cron
Source:         https://github.com/citusdata/pg_cron/archive/refs/tags/v%{version}.tar.gz#/%{ext_name}-%{version}.tar.gz
BuildRequires:  %{pg_name}-llvmjit-devel
%pg_server_requires
%if "%{pg_name}" == ""
Name:           %{ext_name}
ExclusiveArch:  do_not_build
%endif

%description
%{ext_name} is a simple cron-based job scheduler for PostgreSQL (9.5 or higher)
that runs inside the database as an extension. It uses the same syntax as
regular cron, but it allows you to schedule PostgreSQL commands directly from
the database.

%prep
%autosetup -p1 -n %{ext_name}-%{version}

%build
%make_pgxs

%install
%make_install

%post
%{_datadir}/postgresql/install-alternatives %{pg_version}

%postun
%{_datadir}/postgresql/install-alternatives %{pg_version}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{pg_config_sharedir}/extension/%{ext_name}*
%{pg_config_pkglibdir}/%{ext_name}.so
%if %{postgresql_has_llvm}
%{pg_config_pkglibdir}/bitcode/*
%endif

%changelog
