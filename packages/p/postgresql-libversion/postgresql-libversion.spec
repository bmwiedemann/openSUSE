#
# spec file for package postgresql-libversion
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define pg_name @BUILD_FLAVOR@%{nil}
%define ext_name libversion
%define __provides_exclude ^lib.*\\.so.*$
Name:           %{pg_name}-%{ext_name}
Version:        2.0.1
Release:        0
Summary:        PostgreSQL extension for version string comparison
License:        MIT
URL:            https://github.com/repology/postgresql-libversion
Source:         https://github.com/repology/postgresql-libversion/archive/refs/tags/%{version}.tar.gz#/postgresql-%{ext_name}-%{version}.tar.gz
BuildRequires:  %{pg_name}-server-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libversion)
%if "%{pg_name}" == ""
Name:           postgresql-%{ext_name}
ExclusiveArch:  do_not_build
%endif

%description
PostgreSQL extension with support for version string comparison through libversion.

%prep
%autosetup -p1 -n postgresql-%{ext_name}-%{version}

%build
%make_build

%install
%make_install

%check
# https://github.com/repology/postgresql-libversion/blob/master/.github/workflows/ci.yml
# incolves running a server, not implementing that for testing

%files
%license COPYING
%{pg_config_pkglibdir}/%{ext_name}.so
%{pg_config_sharedir}/extension/%{ext_name}*

%changelog
