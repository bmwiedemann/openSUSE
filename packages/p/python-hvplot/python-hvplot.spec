#
# spec file for package python-hvplot
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
Name:           python-hvplot
Version:        0.6.0
Release:        0
Summary:        High-level plotting API for the PyData ecosystem built on HoloViews
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyviz/hvplot
Source0:        https://files.pythonhosted.org/packages/source/h/hvplot/hvplot-%{version}.tar.gz
Source100:      python-hvplot-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 1.0.0
Requires:       python-holoviews >= 1.11.0
Requires:       python-pandas
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-dask
Recommends:     python-datashader >= 0.6.5
Recommends:     python-geopandas
Recommends:     python-geoviews
Recommends:     python-intake
Recommends:     python-intake-parquet
Recommends:     python-nbsite >= 0.5.1
Recommends:     python-networkx
Recommends:     python-notebook >= 5.4
Recommends:     python-param >= 1.6.1
Recommends:     python-phantomjs
Recommends:     python-scipy
Recommends:     python-selenium
Recommends:     python-streamz >= 0.3.0
Recommends:     python-xarray
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module bokeh >= 1.0.0}
BuildRequires:  %{python_module coveralls}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module datashader >= 0.6.5}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module holoviews >= 1.11.0}
BuildRequires:  %{python_module nbsmoke >= 0.2.0}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module notebook >= 5.4}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module param >= 1.6.1}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module streamz >= 0.3.0}
BuildRequires:  %{python_module xarray}
# /SECTION
%python_subpackages

%description
hvPlot provides a high-level plotting API built on HoloViews that
provides a general and consistent API for plotting data in various
formats from the PyData ecosystem. hvPlot can integrate neatly with
individual PyData libraries if an extension mechanism for the native
plot APIs is offered, or it can be used as a standalone component.

%prep
%setup -q -n hvplot-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/hvplot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# tests require a network connection
# %%check
# %%python_expand nosetests-%%{$python_bin_suffix} -v hvplot

%post
%python_install_alternative hvplot

%postun
%python_uninstall_alternative hvplot

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/hvplot
%{python_sitelib}/*

%changelog
