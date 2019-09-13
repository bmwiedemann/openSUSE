#
# spec file for package python-librosa
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-librosa
Version:        0.7.0
Release:        0
Summary:        Python module for audio and music processing
License:        ISC
Group:          Development/Languages/Python
URL:            http://github.com/librosa/librosa
Source0:        https://github.com/librosa/librosa/archive/%{version}.tar.gz#//librosa-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SoundFile >= 0.9.0
Requires:       python-audioread >= 2.0.0
Requires:       python-decorator >= 3.0.0
Requires:       python-joblib >= 0.12
Requires:       python-numba >= 0.38.0
Requires:       python-numpy >= 1.15.0
Requires:       python-resampy >= 0.2.0
Requires:       python-scikit-learn >= 0.14.0
Requires:       python-scipy >= 1.0.0
Requires:       python-six >= 1.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SoundFile >= 0.9.0}
BuildRequires:  %{python_module audioread >= 2.0.0}
BuildRequires:  %{python_module decorator >= 3.0.0}
BuildRequires:  %{python_module joblib >= 0.12}
BuildRequires:  %{python_module numba >= 0.38.0}
BuildRequires:  %{python_module numpy >= 1.15.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module resampy >= 0.2.0}
BuildRequires:  %{python_module scikit-learn >= 0.14.0}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module six >= 1.3}
# /SECTION
%python_subpackages

%description
LibROSA is a python package for music and audio analysis. It provides
the building blocks necessary to create music information retrieval
systems.

%prep
%setup -q -n librosa-%{version}
# Remove unneeded shebangs
find librosa -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests files are missing, even from github sources
# %%check
# %%pytest

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE.md
%{python_sitelib}/*

%changelog
