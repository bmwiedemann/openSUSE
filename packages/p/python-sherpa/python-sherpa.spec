#
# spec file for package python-sherpa
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-sherpa
Version:        4.17.0
Release:        0
Summary:        Modeling and fitting package for scientific data analysis
License:        GPL-3.0-only
URL:            https://github.com/sherpa/sherpa/
Source0:        https://github.com/sherpa/sherpa/archive/%{version}.tar.gz#/sherpa-%{version}.tar.gz
Source1:        https://github.com/sherpa/sherpa-test-data/archive/refs/tags/%{version}.tar.gz#/sherpa-test-data-%{version}.tar.gz
# PATCH-FIX-UPSTREAM sherpa-pr2188-np2docstrings.patch gh#sherpa/sherpa#2188
Patch0:         https://github.com/sherpa/sherpa/pull/2188.patch#/sherpa-pr2188-np2docstrings.patch
# PATCH-FIX-OPENSUSE sherpa-suse-libdir.patch -- UPSTREAM struggles with library paths, see e.g. gh#sherpa/sherpa#2159 code@bnavigator.de
Patch1:         sherpa-suse-libdir.patch
# PATCH-FIX-UPSTREAM gh#sherpa/sherpa#2203
Patch2:         support-pytest-8.3.4.patch
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  wcslib-devel
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
ExcludeArch:    %{ix86} %{arm}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8}
# doctestplus tests don’t look ready gh#sherpa/sherpa#1719
# BuildRequires:  %%{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-xvfb}
# Highly recommended by upstream when building from source
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module matplotlib}
# /SECTION
%python_subpackages

%description
Sherpa is the CIAO modeling and fitting application. It enables the
user to construct models from definitions and fit those models to
data, using a variety of statistics and optimization methods.

%prep
%autosetup -p1 -n sherpa-%{version} -a1
sed -i -e 's|@_LIB@|%{_lib}|' setup.cfg helpers/sherpa_config.py
rm -r extern/fftw-*
# Remove shebangs
sed -i "1{/\\/usr\\/bin\\/env python/d}" \
  sherpa/optmethods/ncoresde.py \
  sherpa/optmethods/ncoresnm.py \
  sherpa/optmethods/opt.py \
  sherpa/utils/akima.py

%build
cp -r extern extern0
%{python_expand # rebuild and install extern/ into build/ for every wheel
%$python_pyproject_wheel
rm -r extern
cp -r extern0 extern
}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/sherpa_test
%python_clone -a %{buildroot}%{_bindir}/sherpa_smoke
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# avoid conftest import mismatch
mv sherpa sherpa_temp
export PYTHONPATH=$PWD/sherpa-test-data-%{version}
donttest="test_Griewank"
# precision issues
%ifnarch x86_64
donttest+=" or (test_regproj and sherpa.plot.dummy_backend)"
donttest+=" or (test_fit_single and Chi2XspecVar)"
%endif
# gh#sherpa/sherpa#1923
donttest+=" or test_integrate1d_basic_epsabs"
# flaky
donttest+=" or test_scaling_staterr"
donttest+=" or (test_Shekel7 and montecarlo)"
donttest+=" or (test_Shekel5 and montecarlo)"
# docstring mismatches
python313_donttest=" or test_show_fit or test_modify_doctring or test_modelwrapper_str_with_doc"
%pytest_arch --pyargs sherpa -n auto --dist=loadgroup -r fE -k "not ($donttest ${$python_donttest})"

%post
%python_install_alternative sherpa_smoke
%python_install_alternative sherpa_test

%postun
%python_uninstall_alternative sherpa_smoke
%python_uninstall_alternative sherpa_test

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sherpa_test
%python_alternative %{_bindir}/sherpa_smoke
%{python_sitearch}/sherpa
%{python_sitearch}/sherpa-%{version}.dist-info
%{python_sitearch}/stk.so
%{python_sitearch}/group.so

%changelog
