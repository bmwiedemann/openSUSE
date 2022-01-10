#
# spec file for package python-pytest-flakes
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-flakes
Version:        4.0.5
Release:        0
Summary:        Pytest plugin to check source code with pyflakes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asmeurer/pytest-flakes
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flakes/pytest-flakes-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module pytest >= 2.8.0}
# End of test requirements
BuildRequires:  fdupes
Requires:       python-pyflakes
Requires:       python-pytest >= 2.8.0
BuildArch:      noarch

%python_subpackages

%description
py.test plugin for efficiently checking python source with pyflakes.

%prep
%setup -q -n pytest-flakes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test_flakes.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_flakes.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_flakes.*
%{python_sitelib}/pytest_flakes-%{version}-py*.egg-info

%changelog
