#
# spec file for package python-arviz-plots
#
# Copyright (c) 2026 SUSE LLC
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


# Upstream supports Python 3.12+
%define skip_python311 1
Name:           python-arviz-plots
Version:        1.0.0
Release:        0
Summary:        Ready to use and composable plots for Bayesian Workflow
License:        Apache-2.0
URL:            https://github.com/arviz-devs/arviz-plots
Source:         https://github.com/arviz-devs/arviz-plots/archive/refs/tags/v%{version}.tar.gz#/arviz_plots-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module arviz-base >= 1.0}
BuildRequires:  %{python_module arviz-stats >= 1.0}
BuildRequires:  %{python_module h5netcdf}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module matplotlib >= 3.9}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module webcolors}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
Requires:       python-arviz-base >= 1.0
Requires:       python-arviz-stats >= 1.0
Suggests:       python-plotly
Suggests:       python-webcolors
Suggests:       python-matplotlib >= 3.9
BuildArch:      noarch
%python_subpackages

%description
ArviZ plotting elements and static battery included plots

%prep
%autosetup -p1 -n arviz-plots-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/arviz_plots
%{python_sitelib}/arviz_plots-%{version}.dist-info

%changelog
