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
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
Name:           python-pandas%{psuffix}
Version:        1.4.4
Release:        0
Summary:        Python data structures for data analysis, time series, and statistics
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://pandas.pydata.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pandas/pandas-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.32}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.18.5}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module pytz >= 2020.1}
BuildRequires:  %{python_module setuptools >= 51.0.0}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.18.5
Requires:       python-python-dateutil >= 2.8.1
Requires:       python-pytz >= 2020.1
Recommends:     python-Bottleneck >= 1.3.1
Recommends:     python-numexpr >= 2.7.1
Suggests:       python-Jinja2 >= 2.10
Suggests:       python-PyMySQL >= 0.10.1
Suggests:       python-SQLAlchemy >= 1.4.0
Suggests:       python-XlsxWriter >= 1.2.2
Suggests:       python-beautifulsoup4 >= 4.8.2
Suggests:       python-blosc >= 1.17.0
Suggests:       python-fastparquet >= 0.4.0
Suggests:       python-fsspec >= 0.7.4
Suggests:       python-gcsfs >= 0.6.0
Suggests:       python-html5lib >= 1.0.1
Suggests:       python-lxml >= 4.5.0
Suggests:       python-matplotlib >= 3.3.2
Suggests:       python-numba >= 0.50.1
Suggests:       python-openpyxl >= 3.0.3
Suggests:       python-pandas-gbq >= 0.14.0
Suggests:       python-psycopg2 >= 2.7
Suggests:       python-pyarrow >= 1.0.1
Suggests:       python-pyreadstat
Suggests:       python-qt5
Suggests:       python-s3fs >= 0.4.0
Suggests:       python-scipy >= 1.4.1
Suggests:       python-tables >= 3.6.1
Suggests:       python-tabulate >= 0.8.7
Suggests:       python-xarray >= 0.15.1
Suggests:       python-xlrd >= 1.2.0
Suggests:       python-xlwt >= 1.3.0
Suggests:       python-zlib
Suggests:       xclip
Suggests:       xsel
Obsoletes:      python-pandas-doc < %{version}
Provides:       python-pandas-doc = %{version}
%if %{with test}
BuildRequires:  %{python_module Bottleneck >= 1.3.1}
BuildRequires:  %{python_module SQLAlchemy >= 1.4.0}
BuildRequires:  %{python_module XlsxWriter >= 1.2.2}
BuildRequires:  %{python_module beautifulsoup4 >= 4.8.2}
BuildRequires:  %{python_module hypothesis >= 5.5.3}
BuildRequires:  %{python_module lxml >= 4.5.0}
BuildRequires:  %{python_module matplotlib >= 3.3.2}
BuildRequires:  %{python_module numexpr >= 2.7.1}
BuildRequires:  %{python_module openpyxl >= 3.0.3}
BuildRequires:  %{python_module pandas = %{version}}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.17}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist >= 1.31}
BuildRequires:  %{python_module scipy >= 1.4.1}
BuildRequires:  %{python_module xlrd >= 2.0.1}
BuildRequires:  memory-constraints
BuildRequires:  xclip
BuildRequires:  xvfb-run
%endif
%python_subpackages

%description
Pandas is a Python package providing data structures designed for
working with structured (tabular, multidimensional, potentially
heterogeneous) and time series data. It is a high-level building
block for doing data analysis in Python.

%prep
%setup -q -n pandas-%{version}
sed -i 's/--strict-data-files//' pyproject.toml

%build
%if !%{with test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
%endif

%install
%if !%{with test}
%python_install
%{python_expand sed -i -e 's|"python", "-c",|"%{__$python}", "-c",|' %{buildroot}%{$python_sitearch}/pandas/tests/io/test_compression.py
# don't install devel files
rm -r %{buildroot}%{$python_sitearch}/pandas/_libs/src
rm -r %{buildroot}%{$python_sitearch}/pandas/_libs/tslibs/src
%fdupes %{buildroot}%{$python_sitearch}
}
%else
# Copy the installed package back into the source tree
# This is equivalent to build and install editable (pip install -e .), and the only way
# to have a passing test suite due to how the test collection works in pytest >= 7.
# Only works for separate python flavors in multibuild.
%python_expand cp -rf %{$python_sitearch}/pandas/* pandas/
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
# Workaround for pytest-xdist flaky collection order
# https://github.com/pytest-dev/pytest/issues/920
# https://github.com/pytest-dev/pytest/issues/1075
export PYTHONHASHSEED=1
# dtypes not as expected
# https://github.com/pandas-dev/pandas/issues/39096
# https://github.com/pandas-dev/pandas/issues/36579
SKIP_TESTS="(test_misc and test_memory_usage and series and empty and index)"
# pytest-xdist worker crash
SKIP_TESTS+=" or test_pivot_number_of_levels_larger_than_int32"

# --skip-* arguments: Upstream's custom way to skip marked tests. These do not use pytest.mark.
SKIP_ARGS="--skip-network"
# clipboard not set up properly in build service without window manager
SKIP_MARKERS="clipboard"
# skip tests which upstream marked for -n 1 only.
SKIP_MARKERS+=" or single_cpu"

if [ $(getconf LONG_BIT) -eq 32 ]; then
# https://github.com/pandas-dev/pandas/issues/31856
SKIP_TESTS+=" or test_maybe_promote_int_with_int"
# rounding error
SKIP_TESTS+=" or (test_rolling_quantile_interpolation_options and data1 and linear and 0.1)"
fi
%ifarch %{ix86}
# overflows on i586
SKIP_TESTS+=" or test_encode_non_c_locale"
# fails on i586 (was gcc10-skip-one-test.patch)
SKIP_TESTS+=" or test_merge_on_ints_floats_warning"
%endif
%ifarch ppc64 s390x
# big endian type issues
SKIP_TESTS+=" or test_astype"
SKIP_TESTS+=" or test_to_numpy_string"
SKIP_TESTS+=" or (test_construction and test_to_numpy)"
SKIP_TESTS+=" or test_to_records_index_name"
SKIP_TESTS+=" or test_to_records_dtype"
SKIP_TESTS+=" or test_to_records_dict_like"
SKIP_TESTS+=" or (test_c_parser_only and test_unsupported_dtype)"
SKIP_TESTS+=" or test_td_mul_td64_ndarray_invalid"
%endif
%ifnarch x86_64
# type and numeric precision issues, partially reported for arm and marked xfail upstream but not for e.g. ppc
SKIP_TESTS+=" or (test_astype and test_subtype_integer_errors)"
SKIP_TESTS+=" or (test_to_numeric and test_downcast_nullable_numeric and data12-UInt64-signed-UInt64)"
SKIP_TESTS+=" or (test_rolling and test_rolling_var_numerical_issues)"
SKIP_TESTS+=" or (test_groupby  and test_groupby_numerical_stability_sum_mean)"
SKIP_TESTS+=" or (test_groupby  and test_groupby_numerical_stability_cumsum)"
SKIP_TESTS+=" or (test_c_parser_only and test_float_precision_options)"
# run the slow tests only on x86_64
SKIP_ARGS+=" --skip-slow --skip-db"
%endif

# The test collection consumes a lot of memory per worker. This sets %%jobs.
%limit_build -m 2048

%{python_expand $python -c 'import pandas; print(pandas.__path__); print(pandas.show_versions())'
# cache: can't just say no cacheprovider, because one test checks for the --lf option of pytest-cache
xvfb-run pytest-%{$python_bin_suffix} -v -n %{jobs} --dist=loadfile \
                                      -o cache_dir=$PWD/.pytest_cache --cache-clear \
                                      ${SKIP_ARGS} \
                                      -m "not (${SKIP_MARKERS})" \
                                      -k "not (${SKIP_TESTS})" \
                                      pandas
}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md RELEASE.md
%{python_sitearch}/pandas/
%{python_sitearch}/pandas-%{version}*-info
%endif

%changelog
