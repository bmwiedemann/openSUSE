#
# spec file for package python-pytest_check
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pytest-check
Version:        1.0.5
Release:        0
Summary:        A pytest plugin that allows multiple failures per test
License:        MIT
URL:            https://github.com/okken/pytest-check
Source:         https://files.pythonhosted.org/packages/source/p/pytest-check/pytest_check-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  fdupes
Requires:       python-pytest >= 6
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin that allows multiple failures per test. A rewrite of pytest-expect


%prep
%setup -q -n pytest_check-%{version}

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
%{python_sitelib}/pytest_check
%{python_sitelib}/pytest_check-%{version}*-info

%changelog
