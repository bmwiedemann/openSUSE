#
# spec file for package python-intake
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


Name:           python-intake
Version:        0.6.6
Release:        0
Summary:        Data loading and cataloging system
License:        BSD-2-Clause
URL:            https://github.com/intake/intake
Source:         https://github.com/intake/intake/archive/refs/tags/%{version}.tar.gz#/intake-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-dask
Requires:       python-dask-bag
Requires:       python-entrypoints
Requires:       python-fsspec >= 2021.7.0
Requires:       python-msgpack
Recommends:     python-bokeh
Recommends:     python-dask-dataframe
Recommends:     python-hvplot
Recommends:     python-msgpack-numpy
Recommends:     python-panel >= 0.8.0
Recommends:     python-pyarrow
Recommends:     python-python-snappy
Recommends:     python-requests
Recommends:     python-tornado
Suggests:       python-intake-parquet
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module appdirs}
# upper pin for bokeh required for resolver conflicts with dask, hvplot, and panel.
# upstream even declares bokeh<2, but we don't have it
BuildRequires:  %{python_module bokeh < 2.5}
BuildRequires:  %{python_module dask-bag}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module fsspec >= 2021.7.0}
BuildRequires:  %{python_module hvplot >= 0.5.2}
BuildRequires:  %{python_module msgpack}
# strictly a test req, but not a runtime requirement, not available in openSUSE
#BuildRequires:  %%{python_module intake-parquet}
BuildRequires:  %{python_module msgpack-numpy}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module panel >= 0.8.0}
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
sed -i -e "/import os/ a import sys" -e "s/cmd = \['python'/cmd = \[sys.executable/" intake/conftest.py
find intake -path '*/tests/*.py' -exec sed -i '1{/env python/d}' {} ';'

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/intake
%python_clone -a %{buildroot}%{_bindir}/intake-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/intake-%{version}*-info/*

%check
# Looks for `which python`, which we don't have in TW
donttest+=" or test_which"
# test_discover_cli overrides the PYTHONPATH and thus doesn't find the package in buildroot
# test_discover does not find its own config because the registration does not work in our test env
donttest+=" or test_discover"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # the test looks for the wrong dtype on 32-bit (int64 vs int)
  donttest+=" or test_zarr_minimal"
fi
# skip tests expecting the unavailable intake-parquet driver (configured in intake/tests/catalog_inherit_params.yml)
donttest+=" or test_inherit_params"
donttest+=" or test_runtime_overwrite_params"
donttest+=" or test_local_param_overwrites"
donttest+=" or test_local_and_global_params"
donttest+=" or test_search_inherit_params"
donttest+=" or test_multiple_cats_params"
# wrong exception class
donttest+=" or test_mlist_parameter"
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
%exclude %{python_sitelib}/intake/tests
%exclude %{python_sitelib}/intake/*/tests
%exclude %{python_sitelib}/intake/cli/*/tests
%exclude %{python_sitelib}/intake/interface/*/tests
%exclude %{python_sitelib}/intake/util_tests.py
%pycache_only %exclude %{python_sitelib}/intake/__pycache__/util_tests.*.pyc
%exclude %{python_sitelib}/intake/conftest.py
%pycache_only %exclude %{python_sitelib}/intake/__pycache__/conftest.*.pyc
%exclude %{python_sitelib}/intake/interface/conftest.py
%pycache_only %exclude %{python_sitelib}/intake/interface/__pycache__/conftest.*.pyc

%changelog
