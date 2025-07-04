#
# spec file for package python-calmjs
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-calmjs
Version:        3.4.4
Release:        0
Summary:        A Python framework for working with the Node.js ecosystem
License:        GPL-2.0-or-later
URL:            https://github.com/calmjs/calmjs/
Source:         https://github.com/calmjs/calmjs/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support Python 3.13 argparse output changes
Patch0:         support-python-313.patch
BuildRequires:  %{python_module calmjs.parse >= 1.0.0}
BuildRequires:  %{python_module calmjs.types}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-calmjs.parse >= 1.0.0
Requires:       python-calmjs.types
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  nodejs-common
# /SECTION
%python_subpackages

%description
A Python framework for building toolchains and utilities for working
with the Node.js ecosystem from within a Python environment.

%prep
%autosetup -p1 -n calmjs-%{version}
# needs network and npm
rm src/calmjs/tests/test_npm.py
# we don't have yarn binary
rm src/calmjs/tests/test_yarn.py

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/calmjs
# see https://github.com/calmjs/calmjs/issues/65 for maintainer feedback
# regarding these two subpackages.
# %%python_expand rm -r %%{buildroot}%%{$python_sitelib}/calmjs/testing
# %%python_expand rm -r %%{buildroot}%%{$python_sitelib}/calmjs/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# DistLoggerTestCase is not working correctly in obs build environment
%pytest -v --pyargs calmjs.tests -k 'not DistLoggerTestCase'

%pre
%python_libalternatives_reset_alternative calmjs

%files %{python_files}
%license LICENSE
%doc CHANGES.rst
%python_alternative %{_bindir}/calmjs
%{python_sitelib}/calmjs
%{python_sitelib}/calmjs-%{version}*-nspkg.pth
%{python_sitelib}/calmjs-%{version}.dist-info

%changelog
