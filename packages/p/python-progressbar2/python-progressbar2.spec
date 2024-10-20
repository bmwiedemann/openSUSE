#
# spec file for package python-progressbar2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-progressbar2
Version:        4.3.2
Release:        0
Summary:        Python library to provide visual text-based progress to long running operations
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/WoLpH/python-progressbar
Source:         https://files.pythonhosted.org/packages/source/p/progressbar2/progressbar2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-utils >= 2.3.0
Conflicts:      python-progressbar
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-utils >= 2.3.0}
# /SECTION
%python_subpackages

%description
A Python Progressbar library to provide visual (yet text based) progress to long running operations.

%prep
%setup -q -n progressbar2-%{version}
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove problematic section from pytest.ini
export PYTEST_ADDOPTS="--doctest-modules"
export PYTHONPATH=$PWD
rm -v progressbar/terminal/os_specific/windows.py
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/progressbar
%{python_sitelib}/progressbar2-%{version}.dist-info

%changelog
