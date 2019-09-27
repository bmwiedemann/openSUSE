#
# spec file for package python-devpi-client
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
Name:           python-devpi-client
Version:        5.0.0
Release:        0
Summary:        Client for devpi
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/devpi/devpi
Source:         https://files.pythonhosted.org/packages/source/d/devpi-client/devpi-client-%{version}.tar.gz
Patch0:         test_sys_executable.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-check-manifest >= 0.28
Requires:       python-devpi-common >= 3.4.0
Requires:       python-pkginfo >= 1.4.2
Requires:       python-pluggy >= 0.6.0
Requires:       python-py >= 1.4.31
Requires:       python-tox >= 3.1.0
Requires:       python-wheel
Recommends:     git-core
Recommends:     python-Sphinx
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module check-manifest >= 0.28}
BuildRequires:  %{python_module devpi-common >= 3.4.0}
BuildRequires:  %{python_module devpi-server}
BuildRequires:  %{python_module pkginfo >= 1.4.2}
BuildRequires:  %{python_module pluggy >= 0.6.0}
BuildRequires:  %{python_module py >= 1.4.31}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module tox >= 3.1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
devpi upload/install/... workflow commands for Python developers.

%prep
%setup -q -n devpi-client-%{version}
rm tox.ini
%patch0 -p1

sed -i 's/"python \(setup.py[^"]*\)"/(sys.executable + " \1")/' testing/test_upload.py
sed -i 's/"python", "setup.py"/sys.executable, "setup.py"/' testing/test_test.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
export PATH=$PATH:%{buildroot}/%{_bindir}
# Unknown failures https://github.com/devpi/devpi/issues/706
%pytest -k 'not (test_simple_install_new_venv_workflow or test_simple_install_activated_venv_workflow)'

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%python3_only %{_bindir}/devpi
%{python_sitelib}/*

%changelog
