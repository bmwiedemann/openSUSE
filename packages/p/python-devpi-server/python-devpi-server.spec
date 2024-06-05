#
# spec file for package python-devpi-server
#
# Copyright (c) 2024 SUSE LLC
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


%define commands export fsck gen-config import init passwd server gen-secret

%{?sle15_python_module_pythons}
Name:           python-devpi-server
Version:        6.11.0
Release:        0
Summary:        Private PyPI caching server
License:        MIT
URL:            https://doc.devpi.net
Source:         https://files.pythonhosted.org/packages/source/d/devpi-server/devpi_server-%{version}.tar.gz
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-argon2-cffi >= 16.2
Requires:       python-attrs
Requires:       python-defusedxml
Requires:       python-devpi-common >= 3.3.0
Requires:       python-execnet >= 1.2
Requires:       python-httpx
Requires:       python-itsdangerous >= 0.24
Requires:       python-lazy
Requires:       python-passlib
Requires:       python-platformdirs
Requires:       python-pluggy >= 0.6.0
Requires:       python-py >= 1.4.23
Requires:       python-pyramid >= 2
Requires:       python-repoze.lru >= 0.6
Requires:       python-ruamel.yaml >= 0.15.94
Requires:       python-strictyaml
Requires:       python-waitress >= 1.0.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
# nginx tests failing when not skipped, likely due to rpmbuild environment
Suggests:       nginx
Suggests:       python-WebTest
Suggests:       python-beautifulsoup4
# https://github.com/devpi/devpi/issues/705
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module argon2-cffi >= 16.2}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module devpi-common >= 3.3.0}
BuildRequires:  %{python_module execnet >= 1.2}
BuildRequires:  %{python_module itsdangerous >= 0.24}
BuildRequires:  %{python_module lazy}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module pluggy >= 0.6.0}
BuildRequires:  %{python_module py >= 1.4.23}
BuildRequires:  %{python_module pyramid >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module repoze.lru >= 0.6}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.94}
BuildRequires:  %{python_module strictyaml}
BuildRequires:  %{python_module waitress >= 1.0.1}
# /SECTION
%python_subpackages

%description
A private PyPI caching server, providing user or team based indices which can
inherit packages from each other or from the pypi.org site.

%prep
%setup -q -n devpi_server-%{version}
sed -i "s/ruamel.yaml<=[^']*,/ruamel.yaml/g" setup.py
sed -i "s/--flake8//" tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
for c in %{commands}; do
  %python_clone -a %{buildroot}%{_bindir}/devpi-$c
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1

donttest="test_auth_mirror_url"

%{python_expand \
mkdir bin-%{$python_version}
for c in %{commands}; do
  ln -s %{buildroot}%{_bindir}/devpi-$c-%{$python_version} bin-%{$python_version}/devpi-$c
done
export PATH=$PATH:`pwd`/bin-%{$python_version}
export PYTHONPATH=:%{buildroot}%{$python_sitelib}
$python -m pytest --ignore test_devpi_server -k "not ($donttest)" %{buildroot}%{$python_sitelib}/test_devpi_server
}

%post
for c in %{commands}; do
  %python_install_alternative devpi-$c
done

%postun
for c in %{commands}; do
  %python_uninstall_alternative devpi-$c
done

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%python_alternative %{_bindir}/devpi-export
%python_alternative %{_bindir}/devpi-fsck
%python_alternative %{_bindir}/devpi-gen-config
%python_alternative %{_bindir}/devpi-import
%python_alternative %{_bindir}/devpi-init
%python_alternative %{_bindir}/devpi-passwd
%python_alternative %{_bindir}/devpi-server
%python_alternative %{_bindir}/devpi-gen-secret
%{python_sitelib}/devpi_server
%{python_sitelib}/test_devpi_server
%{python_sitelib}/pytest_devpi_server
%{python_sitelib}/devpi_server-%{version}.dist-info

%changelog
