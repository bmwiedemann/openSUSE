#
# spec file for package python-pylint-venv
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


%{?sle15_python_module_pythons}
Name:           python-pylint-venv
Version:        3.0.4
Release:        0
Summary:        Use the same Pylint installation with different virtual environments
License:        MIT
URL:            https://github.com/jgosmann/pylint-venv/
Source:         https://files.pythonhosted.org/packages/source/p/pylint-venv/pylint_venv-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-pylint_venv = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
pylint-venv provides a Pylint init-hook to use the same Pylint installation with different virtual environments.

%prep
%autosetup -p1 -n pylint_venv-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# upstream has no tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pylint_venv.py*
%pycache_only %{python_sitelib}/__pycache__/pylint_venv*.pyc
%{python_sitelib}/pylint_venv-%{version}.dist-info

%changelog
