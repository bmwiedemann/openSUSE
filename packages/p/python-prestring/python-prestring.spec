#
# spec file for package python-prestring
#
# Copyright (c) 2021 SUSE LLC
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
# evilunit is failing on py3
%define skip_python2 1
Name:           python-prestring
Version:        0.9.0
Release:        0
Summary:        Python source code generation library
License:        MIT
URL:            https://github.com/podhmo/prestring
Source:         https://github.com/podhmo/prestring/archive/%{version}.tar.gz#/prestring-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/podhmo/prestring/commit/55165f7b1a622577801f8d6c2bd3d0f16555be4b Fix test for py39 (#75)
Patch0:         py39.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module evilunit}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
Python source code generation library (with overuse with-syntax).

%prep
%setup -q -n prestring-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
