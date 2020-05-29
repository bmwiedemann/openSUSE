#
# spec file for package python-pandas
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pandas
Version:        1.0.3
Release:        0
Summary:        Python data structures for data analysis, time series, and statistics
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://pandas.pydata.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pandas/pandas-%{version}.tar.gz
Patch0:         gcc10-skip-one-test.patch
BuildRequires:  %{python_module Cython >= 0.28.2}
# test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.13.3}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pyperclip}
BuildRequires:  %{python_module setuptools >= 24.2.0}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Cython >= 0.28.2
Requires:       python-numpy >= 1.13.3
Requires:       python-python-dateutil >= 2.6.1
Requires:       python-pytz >= 2015.4
Recommends:     python-Bottleneck >= 1.2.1
Recommends:     python-Jinja2
Recommends:     python-PyMySQL >= 0.7.11
Recommends:     python-QtPy
Recommends:     python-SQLAlchemy >= 1.1.4
Recommends:     python-XlsxWriter >= 0.9.8
Recommends:     python-beautifulsoup4 >= 4.6.0
Recommends:     python-blosc
Recommends:     python-fastparquet >= 0.2.1
Recommends:     python-gcsfs >= 0.2.2
Recommends:     python-html5lib
Recommends:     python-lxml >= 3.8.0
Recommends:     python-matplotlib >= 2.2.2
Recommends:     python-numexpr >= 2.6.2
Recommends:     python-openpyxl >= 2.4.8
Recommends:     python-pandas-gbq >= 0.8.0
Recommends:     python-psycopg2
Recommends:     python-pyarrow >= 0.9.0
Recommends:     python-pyperclip
Recommends:     python-pyreadstat
Recommends:     python-qt5
Recommends:     python-scipy >= 0.19.0
Recommends:     python-tables >= 3.4.2
Recommends:     python-xarray >= 0.8.2
Recommends:     python-xlrd >= 1.1.0
Recommends:     python-xlwt >= 1.2.0
Recommends:     python-zlib
Recommends:     xclip
Recommends:     xsel
Obsoletes:      python-pandas-doc < %{version}
Provides:       python-pandas-doc = %{version}
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy >= 1.1.4}
BuildRequires:  %{python_module XlsxWriter >= 0.9.8}
BuildRequires:  %{python_module beautifulsoup4 >= 4.6.0}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module lxml >= 3.8.0}
BuildRequires:  %{python_module openpyxl >= 2.4.8}
BuildRequires:  %{python_module pytest >= 4.0.2}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-dateutil >= 2.6.1}
BuildRequires:  %{python_module pytz >= 2015.4}
BuildRequires:  %{python_module xlrd >= 1.1.0}
BuildRequires:  %{python_module xlwt >= 1.2.0}
BuildRequires:  xvfb-run
# /SECTION
%python_subpackages

%description
Pandas is a Python package providing data structures designed for
working with structured (tabular, multidimensional, potentially
heterogeneous) and time series data. It is a high-level building
block for doing data analysis in Python.

%prep
%setup -q -n pandas-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' pandas/core/computation/eval.py
sed -i -e '/^#!\//, 1d' pandas/tests/io/generate_legacy_storage_files.py
sed -i -e '/^#!\//, 1d' pandas/tests/plotting/common.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand sed -i -e 's|"python", "-c",|"%{__$python}", "-c",|' %{buildroot}%{$python_sitearch}/pandas/tests/io/test_compression.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# skip test that tries to compile stuff in buildroot test_oo_optimizable
# test_encode_non_c_locale - skip test as it overflows on 32bit
# test_maybe_promote_int_with_int https://github.com/pandas-dev/pandas/issues/31856
export PYTHONHASHSEED=$(python -c 'import random; print(random.randint(1, 4294967295))')
export http_proxy=http://1.2.3.4 https_proxy=http://1.2.3.4;
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
mv pandas pandas_temp
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'import pandas; print(pandas.show_versions())'
xvfb-run py.test-%{$python_version} -n auto -v %{buildroot}%{$python_sitearch}/pandas/tests -k 'not test_oo_optimizable and not test_encode_non_c_locale and not test_maybe_promote_int_with_int'
}
mv pandas_temp pandas

%files %{python_files}
%license LICENSE
%doc doc/README.rst RELEASE.md
%{python_sitearch}/pandas/
%{python_sitearch}/pandas-%{version}-py*.egg-info

%changelog
