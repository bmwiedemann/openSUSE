#
# spec file for package python-typeguard
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
Name:           python-typeguard
Version:        4.3.0
Release:        0
Summary:        Library for runtime checking of Python types
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source0:        https://github.com/agronholm/typeguard/archive/refs/tags/%{version}.tar.gz#/typeguard-%{version}-gh.tar.gz
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.10.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-importlib-metadata >= 3.6
Requires:       python-typing-extensions >= 4.10.0
%python_subpackages

%description
This library provides run-time type checking for functions defined with PEP 484 argument (and return) type annotations.

%prep
%setup -q -n typeguard-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/typeguard
%{python_sitelib}/typeguard-*.dist-info/

%changelog
