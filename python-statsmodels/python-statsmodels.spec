#
# spec file for package python-statsmodels
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-statsmodels
Version:        0.10.1
Release:        0
Summary:        A Python module that allows users to explore data
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Url:            http://statsmodels.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/s/statsmodels/statsmodels-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools >= 0.6}
BuildRequires:  %{python_module matplotlib >= 1.0.0}
BuildRequires:  %{python_module numpy-devel >= 1.7.0}
BuildRequires:  %{python_module pandas >= 0.7.1}
BuildRequires:  %{python_module patsy >= 0.3.0}
BuildRequires:  %{python_module scipy >= 0.9.0}
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy >= 1.7.0
Requires:       python-pandas >= 0.7.1
Requires:       python-patsy >= 0.3.0
Requires:       python-scipy >= 0.9.0
Recommends:     python-matplotlib >= 1.0.0

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
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Remove unwanted setup files
%python_expand find %{buildroot}%{$python_sitearch} -name 'setup.py*' -exec rm {} \;
%python_expand find %{buildroot}%{$python_sitearch} -type f -exec chmod a-x {} \;
rm -f %{buildroot}%{_prefix}/LICENSE.txt
rm -f %{buildroot}%{_prefix}/setup.cfg

%ifnarch ppc64le
%check
export PYTHONDONTWRITEBYTECODE=1 # do not write unreproducible .pyc files
mv statsmodels statsmodels_temp
rm -rf build _build.*
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
pytest-%{$python_bin_suffix} -p no:cacheprovider %{buildroot}%{$python_sitearch}/statsmodels/
}
mv statsmodels_temp statsmodels
%endif

%files %{python_files}
%doc README.rst README_l1.txt
%doc examples/
%license COPYRIGHTS.txt LICENSE.txt
%{python_sitearch}/statsmodels/
%{python_sitearch}/statsmodels-%{version}-py*.egg-info

%changelog
