#
# spec file for package python-asynctest
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python38 1
%define skip_python39 1
Name:           python-asynctest
Version:        0.13.0
Release:        0
Summary:        Enhancement for the unittest with features from asyncio libraries
License:        Apache-2.0
URL:            https://github.com/Martiusweb/asynctest/
Source:         https://files.pythonhosted.org/packages/source/a/asynctest/asynctest-%{version}.tar.gz
Patch0:         asynctest-skip-permstest.patch
BuildRequires:  %{python_module base < 3.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package enhances the standard unittest package with features for
testing asyncio libraries.

%prep
%setup -q -n asynctest-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_basic - it is not supposed to be launched by pytest
%pytest -k "not (test_basic)"

%files %{python_files}
%license LICENSE.md
%doc README.rst
%{python_sitelib}/asynctest
%{python_sitelib}/asynctest-%{version}*-info

%changelog
