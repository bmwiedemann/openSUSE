#
# spec file for package python-sqlite3-to-mysql
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-sqlite3-to-mysql
Version:        1.4.16
Release:        0
Summary:        A Python tool to transfer data from SQLite 3 to MySQL
License:        MIT
URL:            https://github.com/techouse/sqlite3-to-mysql
Source:         https://files.pythonhosted.org/packages/source/s/sqlite3-to-mysql/sqlite3-to-mysql-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  docker
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-SQLAlchemy
BuildRequires:  python3-SQLAlchemy-Utils
BuildRequires:  python3-docker
BuildRequires:  python3-factory_boy
BuildRequires:  python3-pytest-timeout
Requires:       python-click >= 7.0
Requires:       python-mysql-connector-python >= 8.0.18
Requires:       python-packaging >= 20.3
Requires:       python-pytimeparse >= 1.1.8
Requires:       python-simplejson >= 3.16.0
Requires:       python-six >= 1.12.0
Requires:       python-tabulate
Requires:       python-tqdm >= 4.35.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module mysql-connector-python >= 8.0.18}
BuildRequires:  %{python_module packaging >= 20.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytimeparse >= 1.1.8}
BuildRequires:  %{python_module simplejson >= 3.16.0}
BuildRequires:  %{python_module six >= 1.12.0}
BuildRequires:  %{python_module sphinxcontrib-programoutput}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tqdm >= 4.35.0}
# /SECTION
%python_subpackages

%description
A Python tool to transfer data from SQLite 3 to MySQL

%prep
%autosetup -p1 -n sqlite3-to-mysql-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sqlite3mysql
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative sqlite3mysql

%postun
%python_uninstall_alternative sqlite3mysql

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sqlite3mysql
%{python_sitelib}/sqlite3_to_mysql-%{version}*-info
%{python_sitelib}/sqlite3_to_mysql

%changelog
