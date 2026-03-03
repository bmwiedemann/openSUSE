#
# spec file for package python-arviz-stats
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
Name:           python-arviz-stats
Version:        1.0.0
Release:        0
Summary:        Statistical computation and diagnostics for ArviZ
License:        Apache-2.0
URL:            https://github.com/arviz-devs/arviz-base
Source:         https://github.com/arviz-devs/arviz-stats/archive/refs/tags/v%{version}.tar.gz#/arviz_stats-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 2}
BuildRequires:  %{python_module scipy >= 1.13}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy >= 2
Requires:       python-scipy >= 1.13
Requires:       python-xarray-einstats >= 0.8
Suggests:       python-arviz-base >= 1.0
Suggests:       python-numba
BuildArch:      noarch
%python_subpackages

%description
ArviZ computational/numeric features: statistical summaries, diagnostics, model comparison.

%prep
%autosetup -p1 -n arviz-stats-%{version}

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
%{python_sitelib}/arviz_stats
%{python_sitelib}/arviz_stats-%{version}.dist-info

%changelog
