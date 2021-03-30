#
# spec file for package python-librosa
#
# Copyright (c) 2021 SUSE LLC
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
# SciPy 1.6.0 dropped support for Python 3.6, many packages from the NumPy family follow. (NEP 29)
%define         skip_python36 1
Name:           python-librosa
Version:        0.8.0
Release:        0
Summary:        Python module for audio and music processing
License:        ISC AND CC-BY-3.0
URL:            https://github.com/librosa/librosa
# The github archive has the tests
Source0:        https://github.com/librosa/librosa/archive/%{version}.tar.gz#/librosa-%{version}.tar.gz
Source1:        librosa-create-pooch-cache.py
# Test data. Use create librosa-create-pooch-cache.py to create this file
Source2:        librosa-pooch-cache.tar.gz
BuildRequires:  %{python_module SoundFile >= 0.9.0}
BuildRequires:  %{python_module audioread >= 2.0.0}
BuildRequires:  %{python_module decorator >= 3.0.0}
BuildRequires:  %{python_module joblib >= 0.12}
BuildRequires:  %{python_module numba >= 0.43.0}
BuildRequires:  %{python_module numpy >= 1.15.0}
BuildRequires:  %{python_module pooch >= 1.0}
BuildRequires:  %{python_module resampy >= 0.2.0}
BuildRequires:  %{python_module scikit-learn >= 0.14.0}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SoundFile >= 0.9.0
Requires:       python-audioread >= 2.0.0
Requires:       python-decorator >= 3.0.0
Requires:       python-joblib >= 0.12
Requires:       python-numba >= 0.43.0
Requires:       python-numpy >= 1.15.0
Requires:       python-pooch >= 1.0
Requires:       python-resampy >= 0.2.0
Requires:       python-scikit-learn >= 0.14.0
Requires:       python-scipy >= 1.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module contextlib2}
BuildRequires:  %{python_module matplotlib >= 2.0}
BuildRequires:  %{python_module pytest-mpl}
# xdist not specified upstream but it uses resources more efficiently
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module samplerate}
BuildRequires:  ffmpeg
# /SECTION
%python_subpackages

%description
LibROSA is a python package for music and audio analysis. It provides
the building blocks necessary to create music information retrieval
systems.

%prep
%setup -q -n librosa-%{version} -a 2
# Remove unneeded shebangs
find librosa -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
# don't measure test coverage
sed -i '/tool:pytest/,/addopts/ s/--cov-report.*--cov librosa//' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LIBROSA_DATA_DIR=$PWD/librosa-pooch-cache
# test data files not packaged
donttest+=" or (test_core and test_iirt)"
donttest+=" or (test_features and test_cens)"
donttest+=" or (test_filters and test_semitone_filterbank)"
# image files do not match without exact mpl version
donttest+=" or test_display"
%pytest -n auto -k "not (${donttest:4})"

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE.md
%{python_sitelib}/librosa
%{python_sitelib}/librosa-%{version}*-info

%changelog
