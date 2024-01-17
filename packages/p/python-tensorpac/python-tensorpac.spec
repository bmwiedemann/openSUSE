#
# spec file for package python-tensorpac
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


%define skip_python2 1
%define skip_python36 1
Name:           python-tensorpac
Version:        1.1
Release:        0
Summary:        Tensor-based phase-Amplitude coupling package
License:        BSD-3-Clause
URL:            https://etiennecmb.github.io/tensorpac/
Source:         https://github.com/EtienneCmb/tensorpac/archive/refs/tags/v%{version}.tar.gz#/tensorpac-%{version}.tar.gz
# PATCH-FIX-OPENSUSE numpy-1.24.patch gh#EtienneCmb/tensorpac#17
Patch0:         numpy-1.24.patch
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib
Requires:       python-numpy >= 1.12
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy >= 1.12}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module statsmodels}
# /SECTION
%python_subpackages

%description
Tensorpac is an Python toolbox for computing Phase-Amplitude Coupling
(PAC) using tensors and parallel computing.

%prep
%autosetup -p1 -n tensorpac-%{version}
chmod a-x LICENSE README.rst
# upstream tarball contains py3.7 cache files
rm -rf */__pycache__
rm -rf */*/__pycache__

%build
%python_build

%install
%python_install
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/*egg-info/*
%python_expand rm -r %{buildroot}%{$python_sitelib}/tensorpac/{tests,methods/tests}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# optional python-mne is not available
donttest="     (TestPac and test_fit)"
donttest+=" or (TestPac and test_pac_comodulogram)"
donttest+=" or (TestErpac and test_fit)"
donttest+=" or (TestErpac and test_filterfit)"
donttest+=" or (TestErpac and test_functional_erpac)"
donttest+=" or (TestUtils and test_psd)"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tensorpac
%{python_sitelib}/tensorpac*-info

%changelog
