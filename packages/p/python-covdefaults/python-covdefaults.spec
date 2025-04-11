#
# spec file for package python-covdefaults
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


%{?sle15_python_module_pythons}
Name:           python-covdefaults
Version:        2.3.0
Release:        0
Summary:        Python coverage plugin to provide default settings
License:        MIT
URL:            https://github.com/asottile/covdefaults
Source:         https://github.com/asottile/covdefaults/archive/v%{version}.tar.gz#/covdefaults-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#asottile/covdefaults#164
Patch0:         support-coverage-7.7.patch
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage
BuildArch:      noarch
%python_subpackages

%description
Python coverage plugin to provide default settings.

%prep
%autosetup -p1 -n covdefaults-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m coverage run -m pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/covdefaults.py
%pycache_only %{python_sitelib}/__pycache__/covdefaults.*.pyc
%{python_sitelib}/covdefaults-%{version}.dist-info

%changelog
