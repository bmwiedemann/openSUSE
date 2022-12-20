#
# spec file for package python-calmjs
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


%define skip_python2 1
Name:           python-calmjs
Version:        3.4.2
Release:        0
Summary:        A Python framework for working with the Node.js ecosystem
License:        GPL-2.0-or-later
URL:            https://github.com/calmjs/calmjs/
Source:         https://github.com/calmjs/calmjs/archive/%{version}.tar.gz
BuildRequires:  %{python_module calmjs.parse >= 1.0.0}
BuildRequires:  %{python_module calmjs.types}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-calmjs.parse >= 1.0.0
Requires:       python-calmjs.types
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/calmjs
# %%python_expand rm -r %%{buildroot}%%{$python_sitelib}/calmjs/testing
# %%python_expand rm -r %%{buildroot}%%{$python_sitelib}/calmjs/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# DistLoggerTestCase is not working correctly in obs build environment
%pytest -v --pyargs calmjs.tests -k 'not DistLoggerTestCase'

%post
%python_install_alternative calmjs

%postun
%python_uninstall_alternative calmjs

%files %{python_files}
%license LICENSE
%doc CHANGES.rst
%python_alternative %{_bindir}/calmjs
%{python_sitelib}/calmjs
%{python_sitelib}/calmjs-%{version}*-nspkg.pth
%{python_sitelib}/calmjs-%{version}*-info

%changelog
