#
# spec file for package python-fixtures
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
Name:           python-fixtures
Version:        3.0.0
Release:        0
Summary:        Fixtures, reusable state for writing clean tests and more
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/testing-cabal
Source:         https://files.pythonhosted.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fixtures-pr36-py39.patch -- gh#testing-cabal/fixtures#46
Patch0:         fixtures-pr36-py39.patch
BuildRequires:  %{python_module extras}
# explicitly wants to test the backport mock
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr >= 0.11}
BuildRequires:  %{python_module testtools >= 0.9.22}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-extras
Requires:       python-pbr >= 0.11
Requires:       python-testtools >= 0.9.22
BuildArch:      noarch
%python_subpackages

%description
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to make it
easy to write your own fixtures using the fixtures contract. Glue code is
provided that makes using fixtures that meet the Fixtures contract in unittest
compatible test cases easy and straight forward.

%prep
%autosetup -p1 -n fixtures-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m testtools.run fixtures.test_suite

%files %{python_files}
%license COPYING
%doc Apache-2.0 BSD NEWS README
%{python_sitelib}/fixtures
%{python_sitelib}/fixtures-%{version}-py%{python_version}.egg-info

%changelog
