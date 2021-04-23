#
# spec file for package python-intake
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
%define         skip_python2 1
# NEP 29: packages in the dependency tree which droped Python 3.6 support in TW
%define         skip_python36 1
Name:           python-intake
Version:        0.6.0
Release:        0
Summary:        Data loading and cataloging system
License:        BSD-2-Clause
URL:            https://github.com/intake/intake
Source0:        https://files.pythonhosted.org/packages/source/i/intake/intake-%{version}.tar.gz
# Test data
Source1:        https://raw.githubusercontent.com/intake/intake/%{version}/intake/source/tests/data.zarr/.zarray#/tests-data.zarr.zarray
Source2:        https://raw.githubusercontent.com/intake/intake/%{version}/intake/source/tests/data.zarr/0#/tests-data.zarr.0
Source3:        https://raw.githubusercontent.com/intake/intake/%{version}/intake/source/tests/calvert_uk_filter.tar.gz
# PATCH-FIX-UPSTREAM intake-pr560-fix-category-ordering.patch gh#intake/intake#560
Patch0:         intake-pr560-fix-category-ordering.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-dask
Requires:       python-dask-bag
Requires:       python-entrypoints
Requires:       python-fsspec >= 0.7.4
Requires:       python-python-snappy
Requires:       python-tornado
Recommends:     python-hvplot
Recommends:     python-panel >= 0.7.0
Recommends:     python-bokeh
Recommends:     python-dask-dataframe
Recommends:     python-msgpack-numpy
Recommends:     python-pyarrow
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module dask-bag}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module fsspec >= 0.7.4}
BuildRequires:  %{python_module hvplot >= 0.5.2}
BuildRequires:  %{python_module msgpack-numpy}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module panel >= 0.8.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module zarr}
# /SECTION
%python_subpackages

%description
A plugin system for loading your data and making data catalogs.

%prep
%autosetup -p1 -n intake-%{version}
sed -i -e '/^#!\//, 1d' intake/catalog/tests/test_persist.py
sed -i -e '/^#!\//, 1d' intake/container/tests/__init__.py
sed -i -e '/^#!\//, 1d' intake/container/tests/test_generics.py
sed -i -e "/import os/ a import sys" -e "s/cmd = \['python'/cmd = \[sys.executable/" intake/conftest.py
mkdir -p intake/source/tests/data.zarr
cp %{SOURCE1} intake/source/tests/data.zarr/.zarray 
cp %{SOURCE2} intake/source/tests/data.zarr/0 
cp %{SOURCE3} intake/source/tests/calvert_uk_filter.tar.gz

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/intake
%python_clone -a %{buildroot}%{_bindir}/intake-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/intake-%{version}*-info/*

%check
%{python_expand # provide entrypoint for flavor
mkdir -p build/testbin
ln -s %{buildroot}%{_bindir}/intake-%{$python_bin_suffix} build/testbin/intake
ln -s %{buildroot}%{_bindir}/intake-server-%{$python_bin_suffix} build/testbin/intake-server
}
export PATH=$PWD/build/testbin:$PATH
# Looks for `which python`, which we don't have in TW
donttest+=" or test_which"
# test_discover_cli overrides the PYTHONPATH and thus doesn't find the package in buildroot
# test_discover does not find its own config because the registration does not work in our test env
donttest+=" or test_discover"
%pytest -ra -k "not (${donttest:4})"

%post
%python_install_alternative intake
%python_install_alternative intake-server

%postun
%python_uninstall_alternative intake
%python_uninstall_alternative intake-server

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/intake-server
%python_alternative %{_bindir}/intake
%{python_sitelib}/intake
%{python_sitelib}/intake-%{version}*-info

%changelog
