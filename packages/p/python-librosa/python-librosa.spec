#
# spec file for package python-librosa
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


%define static_test_data_commit 72bd79e448829187f6336818b3f6bdc2c2ae8f5a
Name:           python-librosa
Version:        0.10.2.post1
Release:        0
Summary:        Python module for audio and music processing
License:        CC-BY-3.0 AND ISC
URL:            https://github.com/librosa/librosa
# The github archive has the tests
Source0:        https://github.com/librosa/librosa/archive/%{version}.tar.gz#/librosa-%{version}.tar.gz
Source1:        librosa-create-pooch-cache.py
# Pooch test data. Use librosa-create-pooch-cache.py to create this file
Source2:        librosa-pooch-cache.tar.gz
# Static test data
Source3:        https://github.com/librosa/librosa-test-data/archive/%{static_test_data_commit}.tar.gz#/librosa-static-test-data-%{version}.tar.gz
# Provide information required by upstream
Source20:       sysinfo.py
# PATCH-FIX-UPSTREAM csr_matrix-attr-H.patch gh#librosa/librosa#1849 mcepl@suse.com
# csr_matrix.H in scipy has been removed
Patch0:         csr_matrix-attr-H.patch
# PATCH-FIX-UPSTREAM mark-network-tests.patch mcepl@suse.com
# to skip test which require network access
Patch1:         mark-network-tests.patch
BuildRequires:  %{python_module SoundFile >= 0.12.1}
BuildRequires:  %{python_module audioread >= 2.1.9}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module decorator >= 4.3.0}
BuildRequires:  %{python_module joblib >= 0.14}
BuildRequires:  %{python_module lazy_loader >= 0.1}
BuildRequires:  %{python_module msgpack >= 1.0}
BuildRequires:  %{python_module numba >= 0.51.0}
BuildRequires:  %{python_module numpy >= 1.22.3 with %python-numpy < 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pooch >= 1.0}
BuildRequires:  %{python_module scikit-learn >= 0.20.0}
BuildRequires:  %{python_module scipy >= 1.2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module soxr >= 0.3.2}
BuildRequires:  %{python_module typing_extensions >= 4.1.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SoundFile >= 0.12.1
Requires:       python-audioread >= 2.1.9
Requires:       python-decorator >= 4.3.0
Requires:       python-joblib >= 0.14
Requires:       python-lazy_loader >= 0.1
Requires:       python-msgpack >= 1.0
Requires:       python-numba >= 0.51.0
Requires:       python-numpy >= 1.22.3
Requires:       python-pooch >= 1.0
Requires:       python-scikit-learn >= 0.20.0
Requires:       python-scipy >= 1.2.0
Requires:       python-soxr >= 0.3.2
Requires:       python-typing_extensions >= 4.1.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.3.0}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module resampy >= 0.2.2}
BuildRequires:  %{python_module samplerate}
BuildRequires:  ffmpeg-4
# /SECTION
%python_subpackages

%description
LibROSA is a python package for music and audio analysis. It provides
the building blocks necessary to create music information retrieval
systems.

%prep
%autosetup -p1 -n librosa-%{version} -a 2
pushd tests/data
tar xf %{SOURCE3} --strip-components=1
popd
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
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" $python %{SOURCE20}

export LIBROSA_DATA_DIR=$PWD/librosa-pooch-cache
# image files do not match without exact mpl version
donttest="test_display"
# fails with current Tumbleweed
donttest+=" or test_pyin_multi_center"
# causes interpreter SEGVs in some situations
donttest+=" or test_piptrack_errors"
# Overflow on 32-bit
# can not use "ifarch" when BuildArch is set to noarch
%if "%_arch" != "x86_64" && "%_arch" != "aarch64" && "%_arch" != "ppc64le"
donttest+=" or test_tempo or test_hybrid_cqt or test_stft_winsizes"
donttest+=" or test_istft_reconstruction or test_trim"
donttest+=" or test_multichannel"
donttest+=" or test_time_stretch_multi"
donttest+=" or test_piptrack_properties"
donttest+=" or test_pitch_shift_multi"
donttest+=" or test_split_multi"
donttest+=" or test_hpss_multi"
donttest+=" or test_nn_filter_multi"
donttest+=" or (test_nnls_multiblock and 256)"
donttest+=" or (test_rms and (4096 or 4097))"
donttest+=" or test_tonnetz_audio"
%endif
%if "%_arch" == "aarch64"
donttest+=" or test_piptrack_errors"
donttest+=" or test_match_events_onesided"
donttest+=" or test_yin"
donttest+=" or test_yin_tone"
%endif
%if "%_arch" == "ppc64le"
donttest+=" or test_cqt"
%endif
# Flaky segfaults when run in parallel, upstream does not test with xdist
notparallel="test_piptrack"
notparallel+=" or (test_onset_strength_audio and chroma_stft)"
notparallel+=" or test_localmax"
notparallel+=" or test_localmin"
notparallel+=" or test_yin"
notparallel+=" or test_pyin"
notparallel+=" or test_tonnetz"
notparallel+=" or test_remix"
notparallel+=" or test_chroma"
notparallel+=" or test_estimate_tuning"
notparallel+=" or test_zero_crossings"
# gh#librosa/librosa#1879
donttest+=" or test_beat"
# gh#librosa/librosa#1880
donttest+=" or test_nnls_multiblock"
#
donttest+=" or test_subsegment_badn"
%pytest -k "not (${donttest} or ${notparallel} or network)" -n auto
%pytest -k "not (${donttest} or network) and (${notparallel})"

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE.md
%{python_sitelib}/librosa
%{python_sitelib}/librosa-%{version}.dist-info

%changelog
