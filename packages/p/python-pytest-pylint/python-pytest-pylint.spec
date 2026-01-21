#
# spec file for package python-pytest-pylint
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
Name:           python-pytest-pylint
Version:        0.21.0
Release:        0
Summary:        A pytest plugin to check source code with pylint
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/carsongee/pytest-pylint
Source:         https://files.pythonhosted.org/packages/source/p/pytest-pylint/pytest-pylint-%{version}.tar.gz
# Remove archived https://github.com/pytest-dev/pytest-runner from setup_requires
Patch0:         rm-pytest-runner.patch
# PATCH-FIX-OPENSUSE pytest9.patch
Patch1:         pytest9.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pylint >= 2.15.0
Requires:       python-pytest >= 7.0
Suggests:       python-tomli >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module pylint >= 2.15.0}
BuildRequires:  %{python_module pytest >= 7.0}
# /SECTION
%python_subpackages

%description
pytest plugin to check source code with pylint. Run pylint with pytest and have
configurable rule types (i.e. Convention, Warn, and Error) fail the build. You
can also specify a pylintrc file.

%prep
%autosetup -p1 -n pytest-pylint-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_pylint
%{python_sitelib}/pytest_pylint-%{version}.dist-info

%changelog
