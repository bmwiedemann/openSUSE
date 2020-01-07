#
# spec file for package python-calmjs
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-calmjs
Version:        3.4.1
Release:        0
Summary:        A Python framework for working with the Node.js ecosystem
License:        GPL-2.0-or-later
URL:            https://github.com/calmjs/calmjs/
Source:         https://github.com/calmjs/calmjs/archive/%{version}.tar.gz
BuildRequires:  %{python_module calmjs.parse >= 1.0.0}
BuildRequires:  %{python_module calmjs.types}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-calmjs.parse >= 1.0.0
Requires:       python-calmjs.types
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python framework for building toolchains and utilities for working
with the Node.js ecosystem from within a Python environment.

%prep
%setup -q -n calmjs-%{version}
# needs network and npm
rm src/calmjs/tests/test_npm.py
# we don't have yarn binary
rm src/calmjs/tests/test_yarn.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/calmjs
%python_expand rm -r %{buildroot}%{$python_sitelib}/calmjs/testing
%python_expand rm -r %{buildroot}%{$python_sitelib}/calmjs/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#export LANG=en_US.UTF8
#%%{python_expand #first link the stuff for the weird layout
#ln -s %{$python_sitelib}/calmjs/types src/calmjs/
#ln -s %{$python_sitelib}/calmjs/parse src/calmjs/
#pushd src
#$python -m unittest calmjs.tests.make_suite -v
#popd
#}

%post
%python_install_alternative calmjs

%postun
%python_uninstall_alternative calmjs

%files %{python_files}
%license LICENSE
%doc CHANGES.rst
%python_alternative %{_bindir}/calmjs
%{python_sitelib}/*

%changelog
