#
# spec file for package python-acoular
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
%define		github_version 20.10
Name:           python-acoular
Version:        20.10
Release:        0
Summary:        Library for acoustic beamforming
License:        BSD-3-Clause
URL:            https://github.com/acoular/acoular
Source0:        https://github.com/acoular/acoular/archive/v%{github_version}.tar.gz#/acoular-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.40.0
Requires:       python-numpy >= 1.11.3
Requires:       python-scikit-learn >= 0.19.1
Requires:       python-scipy >= 0.1.0
Requires:       python-tables >= 3.4.4
Requires:       python-traits >= 4.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numba >= 0.40.0}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-learn >= 0.19.1}
BuildRequires:  %{python_module scipy >= 0.1.0}
BuildRequires:  %{python_module tables >= 3.4.4}
BuildRequires:  %{python_module traits >= 4.6.0}
BuildRequires:  %{python_module traitsui}
# /SECTION
%python_subpackages

%description
Acoular is a Python module for acoustic beamforming.  Multichannel
data recorded by a microphone array can be processed and analyzed in
order to generate mappings of sound source distributions. The maps
(acoustic photographs) can then be used to locate sources of
interest and to characterize them using their spectra.

%prep
%setup -q -n acoular-%{github_version}
sed -i -e '/^#!\//, 1d' acoular/fastFuncs.py
# UNIX-incompatible test
rm acoular/nidaqimport.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -c 'import acoular';
cd acoular/tests
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v -p "test_*.py"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
