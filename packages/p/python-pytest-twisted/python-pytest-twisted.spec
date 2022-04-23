#
# spec file for package python-pytest-twisted
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
Name:           python-pytest-twisted
Version:        1.13.4
Release:        0
Summary:        Pytest Plugin for Twisted
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-twisted
Source:         https://github.com/pytest-dev/pytest-twisted/archive/v%{version}.tar.gz#/pytest-twisted-%{version}-gh.tar.gz
# PATCH-FIX-OPENSUSE pytest-twisted-ignorepy310DeprecationWarnings.patch -- upstream wants this fixed in twisted itself -- gh#pytest-dev/pytest-twisted/146
Patch0:         pytest-twisted-ignorepy310DeprecationWarnings.patch
# PATCH-FIX-UPSTREAM pytest-twisted-pr148-pytest7.patch -- gh#pytest-dev/pytest-twisted#148
Patch1:         https://github.com/pytest-dev/pytest-twisted/pull/148.patch#/pytest-twisted-pr148-pytest7.patch
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module pytest >= 2.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-Twisted
Requires:       python-decorator
Requires:       python-greenlet
Requires:       python-pytest >= 2.3
BuildArch:      noarch
%python_subpackages

%description
pytest-twisted is a plugin for pytest, which allows to test code,
which uses the twisted framework. test functions can return Deferred
objects and pytest will wait for their completion with this plugin.

%prep
%autosetup -p1 -n pytest-twisted-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_twisted.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_twisted.*
%{python_sitelib}/pytest_twisted-%{version}*-info

%changelog
