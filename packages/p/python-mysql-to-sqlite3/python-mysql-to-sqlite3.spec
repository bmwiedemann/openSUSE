#
# spec file for package python-mysql-to-sqlite3
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


%define short_name mysql-to-sqlite3
%define skip_python2 1
Name:           python-mysql-to-sqlite3
Version:        v1.4.3
Release:        0
Summary:        A simple Python tool to transfer data from MySQL to SQLite 3
License:        MIT
URL:            https://github.com/techouse/mysql-to-sqlite3
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  docker
BuildRequires:  python-rpm-macros
BuildRequires:  python3-SQLAlchemy
BuildRequires:  python3-SQLAlchemy-Utils
BuildRequires:  python3-docker
BuildRequires:  python3-factory_boy
BuildRequires:  python3-pytest
# SECTION test requirements
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module mysql-connector-python >= 8.0.18}
BuildRequires:  %{python_module python-slugify >= 3.0.3}
BuildRequires:  %{python_module pytimeparse >= 1.1.8}
BuildRequires:  %{python_module simplejson >= 3.16.0}
BuildRequires:  %{python_module six >= 1.12.0}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tqdm >= 4.35.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 7.0
Requires:       python-mysql-connector-python >= 8.0.18
Requires:       python-python-slugify >= 3.0.3
Requires:       python-pytimeparse >= 1.1.8
Requires:       python-simplejson >= 3.16.0
Requires:       python-six >= 1.12.0
Requires:       python-tabulate
Requires:       python-tqdm >= 4.35.0
BuildArch:      noarch
%python_subpackages

%description
A simple Python tool to transfer data from MySQL to SQLite 3

%prep
%setup -q -n mysql-to-sqlite3-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mysql2sqlite
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative mysql2sqlite

%postun
%python_uninstall_alternative mysql2sqlite

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/mysql2sqlite
%{python_sitelib}/*

%changelog
