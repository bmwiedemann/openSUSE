#
# spec file for package python-sidpy
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


%define packagename sidpy
%define skip_python2 1
Name:           python-sidpy
Version:        0.11.2
Release:        0
Summary:        Utilities for processing Spectroscopic and Imaging Data
License:        MIT
URL:            https://pycroscopy.github.io/sidpy/
Source:         https://github.com/pycroscopy/sidpy/archive/%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module ase}
BuildRequires:  %{python_module cytoolz}
BuildRequires:  %{python_module dask >= 0.10}
BuildRequires:  %{python_module dask-array >= 0.10}
BuildRequires:  %{python_module distributed >= 2}
BuildRequires:  %{python_module h5py >= 2.6.0}
BuildRequires:  %{python_module ipyfilechooser >= 0.0.6}
BuildRequires:  %{python_module ipywidgets >= 5.2.2}
BuildRequires:  %{python_module joblib >= 0.11.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toolz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ase
Requires:       python-cytoolz
Requires:       python-dask >= 0.10
Requires:       python-dask-array >= 0.10
Requires:       python-distributed >= 2
Requires:       python-h5py >= 2.6.0
Requires:       python-ipyfilechooser >= 0.0.6
Requires:       python-ipywidgets >= 5.2.2
Requires:       python-joblib >= 0.11.0
Requires:       python-matplotlib >= 2.0.0
Requires:       python-mpi4py
Requires:       python-numpy >= 1.10
Requires:       python-psutil
Requires:       python-qt5
Requires:       python-scikit-learn
Requires:       python-scipy
Requires:       python-toolz
BuildArch:      noarch
%python_subpackages

%description
Python utilities for storing, visualizing, and processing Spectroscopic and Imaging Data (SID).

%prep
%setup -q -n %{packagename}-%{version}
# https://github.com/pycroscopy/sidpy/issues/142
sed -i 's:pytest-runner:pytest:' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken test
donttest="test_standard_serial_compute_few_jobs"
%pytest -k "not $donttest"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{packagename}-%{version}*-info
%{python_sitelib}/%{packagename}

%changelog
