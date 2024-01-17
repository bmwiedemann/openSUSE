#
# spec file for package python-click-command-tree
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
Name:           python-click-command-tree
Version:        1.1.1
Release:        0
Summary:        Plugin for click to show the command tree of your CLI
License:        MIT
URL:            https://github.com/whwright/click-command-tree
# pypi tarball does not contain tests directory
Source:         https://github.com/whwright/click-command-tree/archive/%{version}.tar.gz#/click-command-tree-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module click}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
BuildArch:      noarch
%python_subpackages

%description
click-command-tree is a click plugin to show the command tree of your CLI

%prep
%setup -q -n click-command-tree-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/click_command_tree.py
%{python_sitelib}/click_command_tree-%{version}.dist-info/
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
