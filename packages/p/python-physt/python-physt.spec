#
# spec file for package python-physt
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-physt
Version:        0.9.0
Release:        0
Summary:        Python histogram library
License:        MIT
URL:            https://github.com/janpipek/physt
Source:         https://github.com/janpipek/physt/archive/v%{version}.tar.gz#/physt-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.1.8
Requires:       python-hypothesis >= 6.96.1
Requires:       python-narwhals >= 2.0.1
Requires:       python-numpy >= 1.25
Requires:       python-packaging
Requires:       python-rich >= 14.1.0
Requires:       python-typing-extensions
Recommends:     python-astropy >= 6
Recommends:     python-dask-array >= 2023.0
Recommends:     python-folium
Recommends:     python-matplotlib >= 3.0
Recommends:     python-pandas >= 1.3
Recommends:     python-xarray
Suggests:       python-plotly
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module click >= 8.1.8}
BuildRequires:  %{python_module dask-array >= 2023.0}
BuildRequires:  %{python_module hypothesis >= 6.96.1}
BuildRequires:  %{python_module matplotlib >= 3.0}
BuildRequires:  %{python_module narwhals >= 2.0.1}
BuildRequires:  %{python_module numpy >= 1.25}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 1.3}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 14.1.0}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%python_subpackages

%description
P(i/y)thon h(i/y)stograms. Inspired (and based on) numpy.histogram.

The unifies different concepts of histograms as occurring in numpy,
pandas, matplotlib, ROOT, etc. and to create one representation that
can be manipulated with from the data point of view and at the same
time provides integration into IPython notebook and various plotting
options.

%prep
%autosetup -p1 -n physt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/physt
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no polars
ignore="--ignore tests/compat/test_polars.py"
donttest="test_array_at_least_two_different_values or test_zero_statistics or test_plot_hbar"
%pytest $ignore -k "not ($donttest)"

%post
%python_install_alternative physt

%postun
%python_uninstall_alternative physt

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/physt
%{python_sitelib}/physt
%{python_sitelib}/physt-%{version}.dist-info

%changelog
