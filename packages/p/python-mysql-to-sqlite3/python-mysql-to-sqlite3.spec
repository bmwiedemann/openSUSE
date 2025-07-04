#
# spec file for package python-mysql-to-sqlite3
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


%define short_name mysql-to-sqlite3
%define skip_python2 1
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-mysql-to-sqlite3
Version:        2.4.1
Release:        0
Summary:        A simple Python tool to transfer data from MySQL to SQLite 3
License:        MIT
URL:            https://github.com/techouse/mysql-to-sqlite3
Source:         %{short_name}-%{version}.tar.gz
# libalternative
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# Package Requirements
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module SQLAlchemy-Utils}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  docker
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.1.3}
BuildRequires:  %{python_module mysql-connector-python >= 9.0.0}
BuildRequires:  %{python_module python-slugify >= 7.0.0}
BuildRequires:  %{python_module pytimeparse >= 1.1.8}
BuildRequires:  %{python_module simplejson >= 3.19.0}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tqdm >= 4.65.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.1.3
Requires:       python-mysql-connector-python >= 9.0.0
Requires:       python-python-dateutil
Requires:       python-python-slugify >= 7.0.0
Requires:       python-pytimeparse2
Requires:       python-simplejson >= 3.19.0
Requires:       python-tabulate
Requires:       python-tqdm >= 4.65.0
Requires:       python-types-python-dateutil
Requires:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
A simple Python tool to transfer data from MySQL to SQLite 3

%prep
%setup -q -n mysql-to-sqlite3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mysql2sqlite
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# We cannot execute the tests here due to python-mysql-connector-python missing
# the C-extension.

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative mysql2sqlite

%post
%python_install_alternative mysql2sqlite

%postun
%python_uninstall_alternative mysql2sqlite

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mysql2sqlite
%{python_sitelib}/mysql_to_sqlite3
%{python_sitelib}/mysql_to_sqlite3-%{version}*-info

%changelog
