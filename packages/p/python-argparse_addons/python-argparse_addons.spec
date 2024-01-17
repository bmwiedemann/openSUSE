#
# spec file for package python-argparse_addons
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


%{?sle15_python_module_pythons}
Name:           python-argparse_addons
Version:        0.12.0
Release:        0
Summary:        Additional argparse types and actions
License:        MIT
URL:            https://github.com/eerimoq/argparse_addons
Source:         https://files.pythonhosted.org/packages/source/a/argparse_addons/argparse_addons-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Additional argparse types and actions.

%prep
%setup -q -n argparse_addons-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/argparse_addons.py
%{python_sitelib}/argparse_addons-%{version}.dist-info/
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
