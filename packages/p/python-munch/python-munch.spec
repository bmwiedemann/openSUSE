#
# spec file for package python-munch
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-munch
Version:        4.0.0
Release:        0
Summary:        A dot-accessible dictionary
License:        MIT
URL:            https://github.com/Infinidat/munch
Source:         https://files.pythonhosted.org/packages/source/m/munch/munch-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - gh/Infinidat/munch#104 - Adjust tests for Python 3.13
Patch:          https://patch-diff.githubusercontent.com/raw/Infinidat/munch/pull/104.patch#/adjust-tests-for-python3.13.patch
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A dot-accessible dictionary (a la JavaScript objects).

%prep
%autosetup -p1 -n munch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/munch
%{python_sitelib}/munch-%{version}.dist-info

%changelog
