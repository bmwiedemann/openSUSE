#
# spec file for package python-gnssanalysis
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

# affects the python macros even if not used in the spec file
%bcond_without libalternatives

%{?sle15_python_module_pythons}
%define pyname gnssanalysis
Name:           python-%{pyname}
Version:        0.0.58
Release:        0
Summary:        GNSS-related functionality from Geoscience Australia
License:        BSD-3-Clause
URL:            https://github.com/GeoscienceAustralia/%{pyname}
Source:         https://github.com/GeoscienceAustralia/%{pyname}/archive/refs/tags/%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module hatanaka}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module plotext}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module unlzw3}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       %{python_module boto3}
Requires:       %{python_module click}
Requires:       %{python_module hatanaka}
Requires:       %{python_module jinja2}
Requires:       %{python_module matplotlib}
Requires:       %{python_module numpy}
Requires:       %{python_module pandas}
Requires:       %{python_module plotext}
Requires:       %{python_module plotly}
Requires:       %{python_module pyfakefs}
Requires:       %{python_module pymongo}
Requires:       %{python_module pytest}
Requires:       %{python_module scipy}
Requires:       %{python_module tqdm}
Requires:       %{python_module typing_extensions}
Requires:       %{python_module unlzw3}
Requires:       alts
%python_subpackages

%description
The package encompasses various GNSS-related functionality such as efficient
reading and writing GNSS files (e.g. SINEX, SP3, CLK, IONEX and many others),
advanced analysis and comparison, various coordinate transformations including
geodetic frame rotations, predictions and combinations. Package Solver.

%prep
%autosetup -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/clkq
%python_clone -a %{buildroot}%{_bindir}/diffutil
%python_clone -a %{buildroot}%{_bindir}/gnss-filename
%python_clone -a %{buildroot}%{_bindir}/log2snx
%python_clone -a %{buildroot}%{_bindir}/orbq
%python_clone -a %{buildroot}%{_bindir}/snxmap
%python_clone -a %{buildroot}%{_bindir}/sp3merge
%python_clone -a %{buildroot}%{_bindir}/trace2mongo

%check
# somehow fakefs fails
#%#pytest -rs --tb=short

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{pyname}
%{python_sitelib}/%{pyname}-%{version}.dist-info
%python_alternative %{_bindir}/clkq
%python_alternative %{_bindir}/diffutil
%python_alternative %{_bindir}/gnss-filename
%python_alternative %{_bindir}/log2snx
%python_alternative %{_bindir}/orbq
%python_alternative %{_bindir}/snxmap
%python_alternative %{_bindir}/sp3merge
%python_alternative %{_bindir}/trace2mongo

%changelog
