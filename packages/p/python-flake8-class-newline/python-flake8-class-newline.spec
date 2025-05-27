#
# spec file for package python-flake8-class-newline
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flake8-class-newline
Version:        1.6.0
Release:        0
Summary:        Flake8 lint for newline after class definitions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/AlexanderVanEck/flake8-class-newline
Source:         https://files.pythonhosted.org/packages/source/f/flake8-class-newline/flake8-class-newline-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Flake8 Extension to lint for a method newline after a Class definition

%prep
%setup -q -n flake8-class-newline-%{version}

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
%{python_sitelib}/flake8[-_]class[-_]newline
%{python_sitelib}/flake8[-_]class[-_]newline-%{version}*-info

%changelog
