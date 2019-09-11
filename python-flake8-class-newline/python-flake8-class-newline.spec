#
# spec file for package python-flake8-class-newline
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flake8-class-newline
Version:        1.6.0
Release:        0
License:        MIT
Summary:        Flake8 lint for newline after class definitions
Url:            https://github.com/AlexanderVanEck/flake8-class-newline
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/flake8-class-newline/flake8-class-newline-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module flake8}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8
BuildArch:      noarch

%python_subpackages

%description
Flake8 Extension to lint for a method newline after a Class definition

%prep
%setup -q -n flake8-class-newline-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
