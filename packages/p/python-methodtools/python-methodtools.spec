#
# spec file for package python-methodtools
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


Name:           python-methodtools
Version:        0.4.7
Release:        0
Summary:        Expand Standard Functools to Methods
License:        BSD-2-Clause
URL:            https://github.com/youknowone/methodtools
Source0:        https://github.com/youknowone/methodtools/archive/%{version}.tar.gz#/methodtools-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.6.7}
BuildRequires:  %{python_module pytest-cov >= 2.6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wirerope >= 0.4.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wirerope >= 0.4.7
BuildArch:      noarch
%python_subpackages

%description
Expand functools features to methods, classmethods,
staticmethods and even for (unofficial) hybrid methods.

%prep
%setup -q -n methodtools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/methodtools.py
%{python_sitelib}/methodtools-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/methodtools*

%changelog
