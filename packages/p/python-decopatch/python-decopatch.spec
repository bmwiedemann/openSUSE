#
# spec file for package python-decopatch
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
Name:           python-decopatch
Version:        1.4.10
Release:        0
Summary:        python decorators made easy.
License:        BSD-3-Clause
URL:            https://github.com/smarie/python-decopatch
Source0:        https://files.pythonhosted.org/packages/source/d/decopatch/decopatch-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module makefun}
# /SECTION
BuildRequires:  fdupes

# https://github.com/smarie/python-decopatch/blob/main/setup.cfg#L36
Requires:       python-makefun >= 1.5.0
BuildArch:      noarch
%python_subpackages

%description
Because of a tiny oddity in the python language, writing decorators without
help can be a pain because you have to handle the no-parenthesis usage
explicitly. decopatch provides a simple way to solve this issue so that writing
decorators is simple and straightforward.

%prep
%autosetup -p1 -n decopatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# checks require pytest-cases, for whose checks this package is required
# hence checks are disabled

%files %{python_files}
%{python_sitelib}/decopatch/
%pycache_only %{python_sitelib}/decopatch/__pycache__/
%{python_sitelib}/decopatch-%{version}.dist-info/

%changelog
