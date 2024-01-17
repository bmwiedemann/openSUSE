#
# spec file for package python-circuitbreaker
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
%define modname circuitbreaker
Name:           python-circuitbreaker
Version:        1.3.2
Release:        0
Summary:        Python implementation of the "Circuit Breaker" Pattern
License:        BSD-3-Clause
URL:            https://github.com/fabfuel/circuitbreaker
Source:         https://files.pythonhosted.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use_stdlib_mock.patch bugno mcepl@suse.com
# Don't depend on the external mock
Patch0:         use_stdlib_mock.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-typing
BuildArch:      noarch
%python_subpackages

%description
Python implementation of the "Circuit Breaker" Pattern

%prep
%autosetup -p1 -n circuitbreaker-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
