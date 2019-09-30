#
# spec file for package python-devpi-server
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-devpi-server
Version:        5.1.0
Release:        0
Summary:        Private PyPI caching server
License:        MIT
Group:          Development/Languages/Python
URL:            https://doc.devpi.net
Source:         https://files.pythonhosted.org/packages/source/d/devpi-server/devpi-server-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires:       python-argon2-cffi >= 16.2
Requires:       python-devpi-common >= 3.3.0
Requires:       python-execnet >= 1.2
Requires:       python-itsdangerous >= 0.24
Requires:       python-passlib
Requires:       python-pluggy >= 0.6.0
Requires:       python-py >= 1.4.23
Requires:       python-pyramid >= 1.8
Requires:       python-repoze.lru >= 0.6
Requires:       python-ruamel.yaml >= 0.15.94
Requires:       python-strictyaml
Requires:       python-waitress >= 1.0.1
# nginx tests failing when not skipped, likely due to rpmbuild environment
Suggests:       nginx
Suggests:       python-WebTest
Suggests:       python-beautifulsoup4
# https://github.com/devpi/devpi/issues/705
Suggests:       python-mock
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module argon2-cffi >= 16.2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module devpi-common >= 3.3.0}
BuildRequires:  %{python_module execnet >= 1.2}
BuildRequires:  %{python_module itsdangerous >= 0.24}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pluggy >= 0.6.0}
BuildRequires:  %{python_module py >= 1.4.23}
BuildRequires:  %{python_module pyramid >= 1.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module repoze.lru >= 0.6}
BuildRequires:  %{python_module strictyaml}
BuildRequires:  %{python_module waitress >= 1.0.1}
# /SECTION
%python_subpackages

%description
A private PyPI caching server, providing user or team based indices which can
inherit packages from each other or from the pypi.org site.

%prep
%setup -q -n devpi-server-%{version}
sed -i "s/ruamel.yaml<=[^']*,/ruamel.yaml/g" setup.py
sed -i "s/--flake8//" tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PATH=$PATH:%{buildroot}/%{_bindir}
%pytest --slow --ignore test_devpi_server %{buildroot}%{$python_sitelib}/test_devpi_server

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%python3_only %{_bindir}/devpi-server
%{python_sitelib}/*

%changelog
