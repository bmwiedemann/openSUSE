#
# spec file for package python-flake8-quotes
#
# Copyright (c) 2023 SUSE LLC
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
%global skip_python2 1
Name:           python-flake8-quotes
Version:        3.3.2
Release:        0
Summary:        Flake8 lint for quotes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/zheller/flake8-quotes/
Source:         https://files.pythonhosted.org/packages/source/f/flake8-quotes/flake8-quotes-%{version}.tar.gz
BuildRequires:  %{python_module flake8 >= 3.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3.3.0
BuildArch:      noarch
%python_subpackages

%description
Flake8 Extension to lint for quotes.

%prep
%setup -q -n flake8-quotes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests require access to stdin
%pytest -s -k "not test_stdin" test

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/flake8_quotes
%{python_sitelib}/flake8_quotes/*
%dir %{python_sitelib}/flake8_quotes-%{version}-py*.egg-info
%{python_sitelib}/flake8_quotes-%{version}-py*.egg-info

%changelog
