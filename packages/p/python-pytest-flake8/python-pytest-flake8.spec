#
# spec file for package python-pytest-flake8
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pytest-flake8
Version:        1.0.6
Release:        0
Summary:        Plugin for pytest to check FLAKE8 requirements
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tholo/pytest-flake8
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flake8/pytest-flake8-%{version}.tar.gz
BuildRequires:  %{python_module flake8 >= 3.5}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3.5
Requires:       python-pytest >= 3.5
BuildArch:      noarch
%python_subpackages

%description
Plugin for py.test for efficiently checking PEP8 compliance.

%prep
%setup -q -n pytest-flake8-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%{python_sitelib}/*

%changelog
