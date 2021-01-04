#
# spec file for package python-statsmodels
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-statsmodels%{psuffix}
Version:        0.12.1
Release:        0
Summary:        A Python module that allows users to explore data
License:        BSD-3-Clause
URL:            https://github.com/statsmodels/statsmodels
Source:         https://files.pythonhosted.org/packages/source/s/statsmodels/statsmodels-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.15}
BuildRequires:  %{python_module scipy >= 1.1}
BuildRequires:  %{python_module setuptools >= 0.6}
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.15
Requires:       python-pandas >= 0.23
Requires:       python-patsy >= 0.5.1
Requires:       python-scipy >= 1.1
Recommends:     python-matplotlib >= 2.2
%if %{with test}
BuildRequires:  %{python_module matplotlib >= 2.2}
BuildRequires:  %{python_module pandas >= 0.21}
BuildRequires:  %{python_module patsy >= 0.5.1}
BuildRequires:  %{python_module statsmodels >= %{version}}
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
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
%setup -q -n statsmodels-%{version}
rm -rf statsmodels/.pytest_cache
find . -type f -name "*.py" -exec sed -i 's/\r$//' {} \;
find statsmodels -type f -name "*.py" -exec sed -i "/#! \/usr\/bin\/env python/d" {} \;
find statsmodels -type f -name "*.py" -exec sed -i "/#!\/usr\/bin\/env python/d" {} \;
find statsmodels -type f -name "*.py" -exec sed -i "/#! \/usr\/bin\/env python3/d" {} \;
find statsmodels -type f -name "*.py" -exec sed -i "/#!\/usr\/bin\/env python3/d" {} \;
find . -type f -name "*.ipynb" -exec sed -i 's/\r$//' {} \;
sed -i 's/\r$//' COPYRIGHTS.txt
sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' README.rst
sed -i 's/\r$//' README_l1.txt
sed -i 's/\r$//' statsmodels/tsa/statespace/tests/results/results_wpi1_ar3_stata.csv
sed -i 's/\r$//' statsmodels/tsa/regime_switching/tests/results/mar_filardo.csv
sed -i 's/\r$//' statsmodels/tsa/statespace/tests/results/results_wpi1_ar3_stata.csv
sed -i 's/\r$//' statsmodels/tsa/regime_switching/tests/results/mar_filardo.csv
chmod a-x COPYRIGHTS.txt
chmod a-x LICENSE.txt
chmod a-x README.rst
chmod a-x README_l1.txt

%build
%if !%{with test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Remove unwanted setup files
%python_expand find %{buildroot}%{$python_sitearch} -name 'setup.py*' -exec rm {} \;
%python_expand find %{buildroot}%{$python_sitearch} -type f -exec chmod a-x {} \;
rm -f %{buildroot}%{_prefix}/LICENSE.txt
rm -f %{buildroot}%{_prefix}/setup.cfg
%endif

%check
%if %{with test}
# The tests expect an in-place built source tree. Work around conftest import conflicts
# by directly discovering tests in installed sitearch.
testdir=/tmp/%{name}-testdir
mkdir $testdir
cp setup.cfg $testdir
pushd $testdir
# not slow: some tests in tsa and discrete take AGES to run in OBS, like 2h per the folder
%pytest_arch -n auto -p no:cacheprovider -m "not slow" %{$python_sitearch}/statsmodels
popd
rm -r $testdir
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst README_l1.txt
%doc examples/
%license COPYRIGHTS.txt LICENSE.txt
%{python_sitearch}/statsmodels/
%{python_sitearch}/statsmodels-%{version}-py*.egg-info
%endif

%changelog
