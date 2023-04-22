#
# spec file for package python-typeguard
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
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-typeguard
Version:        2.13.3
Release:        0
Summary:        Library for runtime checking of Python types
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source0:        https://files.pythonhosted.org/packages/source/t/typeguard/typeguard-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 1.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library provides run-time type checking for functions defined with PEP 484 argument (and return) type annotations.

%prep
%setup -q -n typeguard-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No testsuite

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
