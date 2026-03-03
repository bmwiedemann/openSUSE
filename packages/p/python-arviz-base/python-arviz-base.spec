#
# spec file for package python-arviz-base
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
Name:           python-arviz-base
Version:        1.0.0
Release:        0
Summary:        Base ArviZ features and converters
License:        Apache-2.0
URL:            https://github.com/arviz-devs/arviz-base/
Source:         https://github.com/arviz-devs/arviz-base/archive/refs/tags/v%{version}.tar.gz#/arviz_base-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 2}
BuildRequires:  %{python_module typing-extensions >= 3.10}
BuildRequires:  %{python_module xarray-complete >= 2024.11.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module scipy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy >= 2
Requires:       python-typing-extensions >= 3.10
Requires:       python-xarray >= 2024.11.0
Suggests:       python-h5netcdf
Suggests:       python-netcdf4
Suggests:       python-h5netcdf
Suggests:       python-zarr
BuildArch:      noarch
%python_subpackages

%description
Base ArviZ features and converters.

%prep
%autosetup -p1 -n arviz-base-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm %{buildroot}%{$python_sitelib}/arviz_base/example_data/.gitignore
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/arviz_base
%{python_sitelib}/arviz_base-%{version}.dist-info

%changelog
