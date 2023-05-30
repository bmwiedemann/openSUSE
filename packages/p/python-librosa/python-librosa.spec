#
# spec file for package python-librosa
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


Name:           python-librosa
Version:        0.9.2
Release:        0
Summary:        Python module for audio and music processing
License:        CC-BY-3.0 AND ISC
URL:            https://github.com/librosa/librosa
# The github archive has the tests
Source0:        https://github.com/librosa/librosa/archive/%{version}.tar.gz#/librosa-%{version}.tar.gz
Source1:        librosa-create-pooch-cache.py
# Pooch test data. Use librosa-create-pooch-cache.py to create this file
Source2:        librosa-pooch-cache.tar.gz
# PATCH-FIX-UPSTREAM gh#librosa/librosa#1551
Patch0:         remove-contextlib2.patch
# PATCH-FIX-OPENSUSE Skip tests that require further test data that is ~180MiB
Patch1:         skip-test-data-missing-tests.patch
# PATCH-FIX-UPSTREAM update-tests-for-numpy-123.patch gh#librosa/librosa#1581
Patch2:         update-tests-for-numpy-123.patch
# PATCH-FIX-UPSTREAM remove-hanning-from-tests.patch gh#librosa/librosa#1548
Patch3:         remove-hanning-from-tests.patch
# PATCH-FIX-UPSTREAM update-for-numpy-124.patch, parts from gh#librosa/librosa#1587,  gh#librosa/librosa#1632
Patch4:         update-for-numpy-124.patch
BuildRequires:  %{python_module SoundFile >= 0.10.2}
BuildRequires:  %{python_module audioread >= 2.1.9}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module decorator >= 4.0.10}
BuildRequires:  %{python_module joblib >= 0.14}
BuildRequires:  %{python_module numba >= 0.45.1}
BuildRequires:  %{python_module numpy >= 1.17.0}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pooch >= 1.0}
BuildRequires:  %{python_module resampy >= 0.2.2}
BuildRequires:  %{python_module scikit-learn >= 0.19.1}
BuildRequires:  %{python_module scipy >= 1.2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SoundFile >= 0.10.2
Requires:       python-audioread >= 2.1.9
Requires:       python-decorator >= 4.0.10
Requires:       python-joblib >= 0.14
Requires:       python-numba >= 0.45.1
Requires:       python-numpy >= 1.17.0
Requires:       python-packaging >= 20.0
Requires:       python-pooch >= 1.0
Requires:       python-resampy >= 0.2.2
Requires:       python-scikit-learn >= 0.19.1
Requires:       python-scipy >= 1.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.3.0}
BuildRequires:  %{python_module pytest-mpl}
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
%autosetup -p1 -n librosa-%{version} -a 2
# Remove unneeded shebangs
find librosa -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
# don't measure test coverage
sed -i '/addopts/ s/--cov-report.*--cov-report=xml//' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LIBROSA_DATA_DIR=$PWD/librosa-pooch-cache
# test data files not packaged
donttest+=" or (test_core and test_iirt) or test_find_files"
donttest+=" or (test_features and test_cens)"
donttest+=" or (test_filters and test_semitone_filterbank)"
# image files do not match without exact mpl version
donttest+=" or test_display"
# soxr not in Tumbleweed
donttest+=" or soxr"
# fails with current Tumbleweed
donttest+=" or test_pyin_multi_center"
# Overflow on i586
if [ $(getconf LONG_BIT) -eq 32 ]; then
    donttest+=" or test_tempo or test_hybrid_cqt or test_stft_winsizes"
    donttest+=" or test_istft_reconstruction or test_trim"
    donttest+=" or test_nnls_multiblock"
fi
%pytest -k "not (${donttest:4})" -n auto

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE.md
%{python_sitelib}/librosa
%{python_sitelib}/librosa-%{version}.dist-info

%changelog
