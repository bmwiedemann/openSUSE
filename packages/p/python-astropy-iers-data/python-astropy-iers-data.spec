#
# spec file for package python-astropy-iers-data
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-astropy-iers-data
Version:        0.2024.6.24.0.31.11
Release:        0
Summary:        IERS Earth Rotation and Leap Second tables for the astropy core package
License:        BSD-3-Clause
URL:            https://github.com/astropy/astropy-iers-data
Source:         https://files.pythonhosted.org/packages/source/a/astropy-iers-data/astropy_iers_data-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-remotedata}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
IERS Earth Rotation and Leap Second tables for the astropy core package

Note: This package is not currently meant to be used directly by users, and only meant to be used from the core astropy package.

%prep
%autosetup -p1 -n astropy_iers_data-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests yet
#%%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/astropy_iers_data
%{python_sitelib}/astropy_iers_data-%{version}.dist-info

%changelog
