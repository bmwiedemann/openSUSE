#
# spec file for package python-makefun
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-makefun
Version:        1.11.3
Release:        0
License:        BSD-3-Clause
Summary:        Small library to dynamically create python functions
Url:            https://github.com/smarie/python-makefun
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
Suggests:       python-funcsigs
BuildArch:      noarch

%python_subpackages

%description
Small library to dynamically create python functions.

%prep
%setup -q -n makefun-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests, as tests require pytest-cases, which requires makefun
#%%check
#%%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
