#
# spec file for package python-devpi-client
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


Name:           python-devpi-client
Version:        6.0.4
Release:        0
Summary:        Client for devpi
License:        MIT
URL:            https://github.com/devpi/devpi
Source:         https://files.pythonhosted.org/packages/source/d/devpi-client/devpi-client-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#devpi/devpi#966
Patch0:         switch-to-build-module.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-build
Requires:       python-check-manifest >= 0.28
Requires:       python-devpi-common >= 3.6.0
Requires:       python-pkginfo >= 1.4.2
Requires:       python-pluggy >= 0.6.0
Requires:       python-py >= 1.4.31
Requires:       python-tox >= 3.1.0
Requires:       python-wheel
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     git-core
Recommends:     python-Sphinx
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module check-manifest >= 0.28}
BuildRequires:  %{python_module devpi-common >= 3.6.0}
BuildRequires:  %{python_module devpi-server}
BuildRequires:  %{python_module pkginfo >= 1.4.2}
BuildRequires:  %{python_module pluggy >= 0.6.0}
BuildRequires:  %{python_module py >= 1.4.31}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox >= 3.1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
devpi-client is a command line tool with sub commands for creating users, using
indexes, uploading to and installing from indexes, as well as a "test" command
for invoking tox.

%prep
%setup -q -n devpi-client-%{version}
rm tox.ini
%autopatch -p1

sed -i 's/"python \(setup.py[^"]*\)"/(sys.executable + " \1")/' testing/test_upload.py
sed -i 's/"python", "setup.py"/sys.executable, "setup.py"/' testing/test_test.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/devpi
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
export PATH=$PATH:%{buildroot}/%{_bindir}
# Unknown failures gh#devpi/devpi#706
# test_help: devpi binary is not available (update-alternatives)
donttest="test_simple_install_new_venv_workflow or test_simple_install_activated_venv_workflow or test_help"
# test_upload: requires network to work
donttest+=" or test_upload"
donttest+=" or test_main_example_with_basic_auth"
# No module named 'pypitoken'
donttest+=" or test_derive_devpi_token or test_derive_legacy_token or test_derive_token"
# error deleting VIRTUAL_ENV
donttest+=" or test_simple_install_missing_venvdir"
%pytest -k "not ($donttest)"

%post
%python_install_alternative devpi

%postun
%python_uninstall_alternative devpi

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%python_alternative %{_bindir}/devpi
%{python_sitelib}/devpi
%{python_sitelib}/devpi_client-%{version}*-info

%changelog
