#
# spec file for package python-pyUSID
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


%define packagename pyUSID
%{?!python_module:%define python_module() python-%{**} python-%{**}}
Name:           python-pyUSID
Version:        0.0.9
Release:        0
Summary:        Framework for processing scientific data (USID)
License:        MIT
URL:            https://pycroscopy.github.io/pyUSID/
Source0:        https://github.com/pycroscopy/pyUSID/archive/%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cytoolz}
BuildRequires:  %{python_module dask >= 0.10}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module h5py >= 2.6.0}
BuildRequires:  %{python_module ipywidgets >= 5.2.2}
BuildRequires:  %{python_module joblib >= 0.11.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sidpy}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toolz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-cytoolz
Requires:       python-dask >= 0.10
Requires:       python-dask-array
Requires:       python-h5py >= 2.6.0
Requires:       python-ipywidgets >= 5.2.2
Requires:       python-joblib >= 0.11.0
Requires:       python-matplotlib >= 2.0.0
Requires:       python-numpy >= 1.10
Requires:       python-psutil
Requires:       python-sidpy
Requires:       python-six
Requires:       python-toolz
BuildArch:      noarch
%python_subpackages

%description
Framework for storing, visualizing, and processing Universal Spectroscopic
and Imaging Data (USID).

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}


%changelog
