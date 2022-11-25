#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-statsmodels%{psuffix}
Version:        0.13.5
Release:        0
Summary:        A Python module that allows users to explore data
License:        BSD-3-Clause
URL:            https://github.com/statsmodels/statsmodels
Source:         https://files.pythonhosted.org/packages/source/s/statsmodels/statsmodels-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.32}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.17}
BuildRequires:  %{python_module scipy >= 1.3}
BuildRequires:  %{python_module setuptools >= 0.59.2}
BuildRequires:  %{python_module setuptools_scm >= 7}
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.17
Requires:       python-pandas >= 0.25
Requires:       python-patsy >= 0.5.2
Requires:       python-scipy >= 1.3
Recommends:     python-matplotlib >= 3
%if %{with test}
# SECTION mandatory
BuildRequires:  %{python_module statsmodels = %{version}}
# /SECTION
# SECTION optional
BuildRequires:  %{python_module matplotlib >= 3}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module pytest >= 7.0.1}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%endif
%python_subpackages

%description
Statsmodels is a Python module that allows users to explore data,
estimate statistical models, and perform statistical tests.
An extensive list of descriptive statistics, statistical tests,
plotting functions, and result statistics are available for different
types of data and each estimator. Researchers across fields may find
that statsmodels fully meets their needs for statistical computing
and data analysis in Python.

%prep
%autosetup -p1 -n statsmodels-%{version}
rm -rf statsmodels/.pytest_cache
find . -type f -name "*.py" -exec sed -i -e '1{/env python/ d}' -e 's/\r$//' {} \;
find . -type f -exec chmod a-x {} \;
find . -type f -name "*.ipynb" -exec sed -i 's/\r$//' {} \;
find . -type f -name "*.csv" -exec sed -i 's/\r$//' {} \;
sed -i 's/\r$//' COPYRIGHTS.txt
sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' README.rst
sed -i 's/\r$//' README_l1.txt

%build
%if !%{with test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
# force cythonization
export SM_FORCE_C=1
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
# The tests expect an in-place built source tree. Work around conftest import conflicts
# by directly discovering tests in installed sitearch.
testdir=/tmp/%{name}-testdir
rm -rf $testdir
mkdir $testdir
cp setup.cfg $testdir
pushd $testdir
%ifarch %{ix86} %{arm32}
# Note: there is no upstream 32-bit support for testing
# gh#statsmodels/statsmodels#7463
%define donttest  -k "not (test_seasonal_order or (test_holtwinters and test_forecast_index) or (test_discrete and test_basic))"
%endif
# not slow: some tests in tsa and discrete take AGES to run in OBS, like 2h per the folder
%pytest_arch -n auto -p no:cacheprovider -m "not slow" %{$python_sitearch}/statsmodels %{?donttest}
popd
rm -r $testdir
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst README_l1.txt
%doc examples/
%license COPYRIGHTS.txt LICENSE.txt
%{python_sitearch}/statsmodels/
%{python_sitearch}/statsmodels-%{version}*-info
%endif

%changelog
