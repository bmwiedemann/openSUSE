#
# spec file for package python-pyUSID
#
# Copyright (c) 2023 SUSE LLC
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


%define packagename pyUSID
%define ghtag 0.0.10r2
Name:           python-pyUSID
Version:        0.0.10.post2
Release:        0
Summary:        Framework for processing scientific data (USID)
License:        MIT
URL:            https://pycroscopy.github.io/pyUSID/
Source0:        https://github.com/pycroscopy/pyUSID/archive/%{ghtag}.tar.gz#/%{packagename}-%{ghtag}.tar.gz
# PATCH-FIX-UPSTREAM abc_iterable.patch gh#pycroscopy/pyUSID#81 mcepl@suse.com
# Iterable goes from collections.abc not directly from collections
Patch0:         abc_iterable.patch
# PATCH-FIX-UPSTREAM pyUSID-pr84-np1.24.patch gh#pycroscopy/pyUSID#84
Patch1:         pyUSID-pr84-np1.24.patch
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cytoolz}
BuildRequires:  %{python_module dask >= 0.10}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module h5py >= 2.6.0}
BuildRequires:  %{python_module ipywidgets >= 5.2.2}
BuildRequires:  %{python_module joblib >= 0.11.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sidpy >= 0.0.2}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-cytoolz
Requires:       python-dask >= 0.10
Requires:       python-h5py >= 2.6.0
Requires:       python-numpy >= 1.10
Requires:       python-psutil
Requires:       python-sidpy >= 0.0.2
Requires:       python-toolz
BuildArch:      noarch
%python_subpackages

%description
Framework for storing, visualizing, and processing Universal Spectroscopic
and Imaging Data (USID).

%prep
%autosetup -p1 -n %{packagename}-%{ghtag}
sed -i -e /pytest-runner/d -e /six/d setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#pycroscopy/pyUSID#80 for skips
%pytest -k 'not (test_custom_interp or test_single_default_interp or test_tuple_default_interp or test_normalize_and_default_interp)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{packagename}-%{version}*-info
%{python_sitelib}/%{packagename}

%changelog
