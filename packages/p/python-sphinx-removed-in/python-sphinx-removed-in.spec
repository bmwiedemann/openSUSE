#
# spec file for package python-sphinx-removed-in
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-sphinx-removed-in
Version:        0.2.1
Release:        0
Summary:        Sphinx directives versionremoved and removed-in
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/MrSenko/sphinx-removed-in
Source:         https://github.com/MrSenko/sphinx-removed-in/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-sphinx-testing.patch -- based on PR
# gh#mrsenko/sphinx-removed-in#9
Patch0:         remove-sphinx-testing.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Sphinx Removed In Extension

%prep
%autosetup -p1 -n sphinx-removed-in-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
