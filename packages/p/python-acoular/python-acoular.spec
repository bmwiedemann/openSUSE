#
# spec file for package python-acoular
#
# Copyright (c) 2022 SUSE LLC
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


%define int_version 22.3
Name:           python-acoular
Version:        22.3
Release:        0
Summary:        Library for acoustic beamforming
License:        BSD-3-Clause
URL:            https://github.com/acoular/acoular
Source0:        https://github.com/acoular/acoular/archive/v%{version}.tar.gz#/acoular-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-setup.patch gh#acoular/acoular#59 mcepl@suse.com -- Bad limit on the Python version, remove numpy upper pin, remove setuptools runtimereq
Patch0:         fix-setup.patch
# PATCH-FIX-OPENSUSE relax-tests.patch code@bnavigator.de -- Precision errors on our architectures differing from upstream
Patch1:         relax-tests.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba
Requires:       python-numpy
Requires:       python-scikit-learn
Requires:       python-scipy >= 1.1.0
Requires:       python-tables >= 3.4.4
Requires:       python-traits >= 6.0
Recommends:     python-traisui
BuildArch:      noarch
# unresolved failure with numba/llvmlite: undefined symbol __powidf2 https://github.com/numba/numba/issues/6012
ExcludeArch:    %{ix86}
# SECTION test requirements
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy >= 1.1.0}
BuildRequires:  %{python_module tables >= 3.4.4}
BuildRequires:  %{python_module traits >= 6.0}
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
%setup -q -n acoular-%{version}
%autopatch -p1

sed -i -e '1{/^#!/ d}' acoular/fastFuncs.py acoular/demo/acoular_demo.py acoular/tests/*.py
# remove test scripts not applicable here
rm acoular/tests/run_tests*.sh
# Windows only load of the NIDAQmx dll
rm acoular/nidaqimport.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd acoular/tests
%pyunittest discover -v -p "test_*.py"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/acoular
%{python_sitelib}/acoular-%{int_version}*-info

%changelog
