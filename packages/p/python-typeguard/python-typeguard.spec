#
# spec file for package python-typeguard
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        4.5.2
Release:        0
Summary:        Library for runtime checking of Python types
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source0:        https://github.com/agronholm/typeguard/archive/refs/tags/%{version}.tar.gz#/typeguard-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM gh#agronholm/typeguard#554
Patch0:         support-python-315.patch
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.10.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-typing-extensions >= 4.10.0
%python_subpackages

%description
This library provides run-time type checking for functions defined with PEP 484 argument (and return) type annotations.

%prep
%autosetup -p1 -n typeguard-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/typeguard
%{python_sitelib}/typeguard-%{version}.dist-info/

%changelog
