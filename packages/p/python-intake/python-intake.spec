#
# spec file for package python-intake
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
%define         skip_python2 1
Name:           python-intake
Version:        0.5.4
Release:        0
Summary:        Data loading and cataloging system
License:        BSD-2-Clause
URL:            https://github.com/ContinuumIO/intake
Source0:        https://files.pythonhosted.org/packages/source/i/intake/intake-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-dask
Requires:       python-dask-array
Requires:       python-dask-bag >= 1.0
Requires:       python-dask-dataframe
Requires:       python-entrypoints
Requires:       python-fsspec >= 0.3.6
Requires:       python-holoviews
Requires:       python-hvplot
Requires:       python-ipywidgets >= 7.2
Requires:       python-msgpack
Requires:       python-msgpack-numpy
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-pytest
Requires:       python-python-snappy
Requires:       python-requests
Requires:       python-ruamel.yaml >= 0.15.0
Requires:       python-six
Requires:       python-tornado >= 4.5.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module dask-bag >= 1.0}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module fsspec >= 0.3.6}
BuildRequires:  %{python_module holoviews}
BuildRequires:  %{python_module hvplot}
BuildRequires:  %{python_module ipywidgets >= 7.2}
BuildRequires:  %{python_module msgpack-numpy}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.0}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado >= 4.5.1}
# /SECTION
%python_subpackages

%description
A plugin system for loading your data and making data catalogs.

%prep
%setup -q -n intake-%{version}
sed -i -e '/^#!\//, 1d' intake/catalog/tests/test_persist.py
sed -i -e '/^#!\//, 1d' intake/container/tests/__init__.py
sed -i -e '/^#!\//, 1d' intake/container/tests/test_generics.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/intake
%python_clone -a %{buildroot}%{_bindir}/intake-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/intake/cli/tests/
%python_expand $python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/intake/cli/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}/intake/cli/tests/

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
%{python_sitelib}/*

%changelog
