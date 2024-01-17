#
# spec file for package python-click-default-group
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
Name:           python-click-default-group
Version:        1.2.4
Release:        0
Summary:        Extends clickGroup to invoke a command without explicit subcommand name
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sublee/click-default-group/
Source:         https://github.com/click-contrib/click-default-group/archive/v%{version}.tar.gz#/click-default-group-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Extends click.Group to invoke a command without explicit subcommand name.

%prep
%autosetup -p1 -n click-default-group-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
