#
# spec file for package python-makefun
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-makefun
Version:        1.16.0
Release:        0
License:        BSD-3-Clause
Summary:        Small library to dynamically create python functions
URL:            https://github.com/smarie/python-makefun
Source:         https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#smarie/python-makefun#119
Patch0:         set-pytest-asyncio-mode.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
# /SECTION
BuildRequires:  fdupes
Suggests:       python-funcsigs
BuildArch:      noarch

%python_subpackages

%description
Small library to dynamically create python functions.

%prep
%autosetup -p1 -n makefun-%{version}
sed -i '/pytest-runner/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/makefun
%{python_sitelib}/makefun-%{version}.dist-info

%changelog
