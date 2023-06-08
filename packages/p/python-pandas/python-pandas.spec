#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python310 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python39 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py311"
%define psuffix -test-py311
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif

# Only test the core functionality in Ring1 (Lettered Staging)
%bcond_with ringdisabled
# s3fs not available
%bcond_with aws
# pandas-gbq not available
%bcond_with gcp
# xlsb not available
%bcond_with xslb

%{?sle15_python_module_pythons}
Name:           python-pandas%{psuffix}
Version:        2.0.2
Release:        0
Summary:        Python data structures for data analysis, time series, and statistics
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://pandas.pydata.org/
# Use GitHub Archive: Test-data
Source0:        https://github.com/pandas-dev/pandas/archive/refs/tags/v%{version}.tar.gz#/pandas-%{version}-gh.tar.gz
# SourceRepository: https://github.com/pandas-dev/pandas
BuildRequires:  %{python_module Cython >= 0.29.33 with %python-Cython < 3}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.20.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  %{python_module versioneer-toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-pytz >= 2020.1
Requires:       timezone >= 2022a
Obsoletes:      python-pandas-doc < %{version}
Provides:       python-pandas-doc = %{version}
%if 0%{?python_version_nodots} >= 311
Requires:       python-numpy >= 1.23.2
%elif 0%{?python_version_nodots} >= 310
Requires:       python-numpy >= 1.21.0
%else
Requires:       python-numpy >= 1.20.3
%endif
# SECTION extras
Recommends:     python-pandas-performance
Suggests:       python-pandas-all
Suggests:       python-pandas-clipboard
Suggests:       python-pandas-compression
Suggests:       python-pandas-computation
Suggests:       python-pandas-excel
Suggests:       python-pandas-feather
Suggests:       python-pandas-fss
Suggests:       python-pandas-hdf5
Suggests:       python-pandas-html
Suggests:       python-pandas-mysql
Suggests:       python-pandas-output_formatting
Suggests:       python-pandas-parquet
Suggests:       python-pandas-plot
Suggests:       python-pandas-postgresql
Suggests:       python-pandas-spss
Suggests:       python-pandas-sql-other
Suggests:       python-pandas-test
Suggests:       python-pandas-xml
%{?_with_aws:Suggests: python-pandas-aws}
%{?_with_gcp:Suggests: python-pandas-gcp}
# /SECTION
%if %{with test}
# required for sqlite3 tests
BuildRequires:  %{pythons}
BuildRequires:  %{python_module pandas-test = %{version}}
BuildRequires:  memory-constraints
BuildRequires:  xvfb-run
%if !%{with ringdisabled}
BuildRequires:  %{python_module IPython}
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module pandas-all = %{version}}
BuildRequires:  %{python_module pandas-clipboard = %{version}}
BuildRequires:  %{python_module pandas-compression = %{version}}
BuildRequires:  %{python_module pandas-computation = %{version}}
BuildRequires:  %{python_module pandas-excel = %{version}}
BuildRequires:  %{python_module pandas-feather = %{version}}
BuildRequires:  %{python_module pandas-fss = %{version}}
BuildRequires:  %{python_module pandas-hdf5 = %{version}}
BuildRequires:  %{python_module pandas-html = %{version}}
BuildRequires:  %{python_module pandas-mysql = %{version}}
BuildRequires:  %{python_module pandas-output_formatting = %{version}}
BuildRequires:  %{python_module pandas-parquet = %{version}}
BuildRequires:  %{python_module pandas-performance = %{version}}
BuildRequires:  %{python_module pandas-plot = %{version}}
BuildRequires:  %{python_module pandas-postgresql = %{version}}
BuildRequires:  %{python_module pandas-spss = %{version}}
BuildRequires:  %{python_module pandas-sql-other = %{version}}
BuildRequires:  %{python_module pandas-xml = %{version}}
BuildRequires:  xclip
%{?_with_aws:BuildRequires:  %{python_module pandas-aws = %{version}}}
%{?_with_gcp:BuildRequires:  %{python_module pandas-gcp = %{version}}}
%endif
%endif
%python_subpackages

%description
Pandas is a Python package providing data structures designed for
working with structured (tabular, multidimensional, potentially
heterogeneous) and time series data. It is a high-level building
block for doing data analysis in Python.

%package test
Summary:        The python pandas[test] extra
Requires:       python-hypothesis >= 6.34.2
Requires:       python-pandas = %{version}
Requires:       python-pytest >= 7.0.0
Requires:       python-pytest-asyncio >= 0.17.0
Requires:       python-pytest-xdist >= 2.2.0
BuildArch:      noarch

%description test
This package provides the [test] extra for python-pandas

%package performance
Summary:        The python pandas[performance] extra
Requires:       python-Bottleneck >= 1.3.2
Requires:       python-numba >= 0.53.1
Requires:       python-numexpr >= 2.7.1
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description performance
This package provides the [performance] extra for python-pandas

It is highly recommended to install this subpackage, as its dependencies
provide speed improvements, especially when working with large data sets.

%package computation
Summary:        The python pandas[computation] extra
Requires:       python-pandas = %{version}
Requires:       python-scipy >= 1.7.1
Requires:       python-xarray >= 0.21.0
BuildArch:      noarch

%description computation
This package provides the [computation] extra for python-pandas

%package fss
Summary:        The python pandas[fss] extra
Requires:       python-fsspec >= 2021.07.0
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description fss
This package provides the [fss] extra for python-pandas

%package aws
Summary:        The python pandas[aws] extra
Requires:       python-pandas = %{version}
Requires:       python-s3fs >= 2021.08.0
BuildArch:      noarch

%description aws
This package provides the [aws] extra for python-pandas

%package gcp
Summary:        The python pandas[gcp] extra
Requires:       python-gcsfs >= 2021.07.0
Requires:       python-pandas = %{version}
Requires:       python-pandas-gbq >= 0.15.0
BuildArch:      noarch

%description gcp
This package provides the [gcp] extra for python-pandas

%package excel
Summary:        The python pandas[excel] extra
Requires:       python-odfpy >= 1.4.1
Requires:       python-openpyxl >= 3.0.7
Requires:       python-pandas = %{version}
%{?_with_xlsb:Requires: python-pyxlsb >= 1.0.8}
Requires:       python-XlsxWriter >= 1.4.3
Requires:       python-xlrd >= 2.0.1
BuildArch:      noarch

%description excel
This package provides the [excel] extra for python-pandas.
(Except for pyxlsb, which is not available as openSUSE rpm package)

%package parquet
Summary:        The python pandas[parquet] extra
Requires:       python-pandas = %{version}
Requires:       python-pyarrow >= 7.0.0
BuildArch:      noarch

%description parquet
This package provides the [parquet] extra for python-pandas

%package feather
Summary:        The python pandas[feather] extra
Requires:       python-pandas = %{version}
Requires:       python-pyarrow >= 7.0.0
BuildArch:      noarch

%description feather
This package provides the [feather] extra for python-pandas

%package hdf5
Summary:        The python pandas[hdf5] extra
Requires:       python-blosc
Requires:       python-pandas = %{version}
Requires:       python-tables >= 3.6.1
BuildArch:      noarch

%description hdf5
This package provides the [hdf5] extra for python-pandas

%package spss
Summary:        The python pandas[spss] extra
Requires:       python-pandas = %{version}
Requires:       python-pyreadstat >= 1.1.2
BuildArch:      noarch

%description spss
This package provides the [spss] extra for python-pandas

%package postgresql
Summary:        The python pandas[postgresql] extra
Requires:       python-SQLAlchemy >= 1.4.16
Requires:       python-pandas = %{version}
Requires:       python-psycopg2 >= 2.8.6
BuildArch:      noarch

%description postgresql
This package provides the [postgresql] extra for python-pandas

%package mysql
Summary:        The python pandas[mysql] extra
Requires:       python-PyMySQL >= 1.0.2
Requires:       python-SQLAlchemy >= 1.4.16
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description mysql
This package provides the [mysql] extra for python-pandas

%package sql-other
Summary:        The python pandas[sql-other] extra
Requires:       python-SQLAlchemy >= 1.4.16
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description sql-other
This package provides the [sql-other] extra for python-pandas

%package html
Summary:        The python pandas[html] extra
Requires:       python-beautifulsoup4 >= 4.9.3
Requires:       python-html5lib >= 1.1
Requires:       python-lxml >= 4.6.3
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description html
This package provides the [html] extra for python-pandas

%package xml
Summary:        The python pandas[xml] extra
Requires:       python-lxml >= 4.6.3
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description xml
This package provides the [xml] extra for python-pandas

%package plot
Summary:        The python pandas[plot] extra
Requires:       python-matplotlib >= 3.6.1
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description plot
This package provides the [plot] extra for python-pandas

%package output_formatting
Summary:        The python pandas[output_formatting] extra
Requires:       python-Jinja2 >= 3.0.0
Requires:       python-pandas = %{version}
Requires:       python-tabulate >= 0.8.9
BuildArch:      noarch

%description output_formatting
This package provides the [output_formatting] extra for python-pandas

%package clipboard
Summary:        The python pandas[clipboard] extra
Requires:       python-PyQt5 >= 5.15.1
Requires:       python-QtPy >= 2.2.0
Requires:       python-pandas = %{version}
BuildArch:      noarch

%description clipboard
This package provides the [clipboard] extra for python-pandas

%package compression
Summary:        The python pandas[compression] extra
Requires:       python-brotlipy >= 0.7.0
Requires:       python-pandas = %{version}
Requires:       python-python-snappy >= 0.6.0
Requires:       python-zstandard >= 0.15.2
BuildArch:      noarch

%description compression
This package provides the [compression] extra for python-pandas

%package all
Summary:        The python pandas[all] extra
Requires:       python-Bottleneck >= 1.3.2
Requires:       python-Jinja2 >= 3.0.0
Requires:       python-PyMySQL >= 1.0.2
Requires:       python-PyQt5 >= 5.15.1
Requires:       python-QtPy >= 2.2.0
Requires:       python-SQLAlchemy >= 1.4.16
Requires:       python-XlsxWriter >= 1.4.3
Requires:       python-beautifulsoup4 >= 4.9.3
Requires:       python-blosc
Requires:       python-brotlipy >= 0.7.0
Requires:       python-fastparquet >= 0.6.3
Requires:       python-fsspec >= 2021.07.0
Requires:       python-gcsfs >= 2021.07.0
Requires:       python-html5lib >= 1.1
Requires:       python-hypothesis >= 6.34.2
Requires:       python-lxml >= 4.6.3
Requires:       python-matplotlib >= 3.6.1
Requires:       python-numba >= 0.53.1
Requires:       python-numexpr >= 2.7.3
Requires:       python-odfpy >= 1.4.1
Requires:       python-openpyxl >= 3.0.7
Requires:       python-pandas = %{version}
Requires:       python-psycopg2 >= 2.8.6
Requires:       python-pyarrow >= 7.0.0
Requires:       python-pyreadstat >= 1.1.2
Requires:       python-pytest >= 7.0.0
Requires:       python-pytest-asyncio >= 0.17.0
Requires:       python-pytest-xdist >= 2.2.0
Requires:       python-python-snappy >= 0.6.0
Requires:       python-scipy >= 1.7.1
Requires:       python-tables >= 3.6.1
Requires:       python-tabulate >= 0.8.9
Requires:       python-xarray >= 0.21.0
Requires:       python-xlrd >= 2.0.1
Requires:       python-zstandard >= 0.15.2
%{?_with_aws:Requires:       python-s3fs >= 2021.08.0}
%{?_with_gcp:Requires:       python-pandas-gbq >= 0.15.0}
%{?_with_xslb:Requires:       python-pyxlsb >= 1.0.8}
BuildArch:      noarch

%description all
This package provides most the [all] extra for python-pandas

Some requirements defined in the PyPI package are left out
because they are not available as openSUSE RPM packages:

  * pandas-gbq
  * pyxlsb
  * s3fs

You can install them directly through `pip3 install --user`, if needed.

%prep
%autosetup -p1 -n pandas-%{version}
# don't call pytest with --strict-data-files
sed -i '/addopts/ {s/--strict-data-files//}' pyproject.toml
# don't require the PyPI data only tzdata package, we use the timezone RPM package
sed -i '/dependencies = \[/,/\]/ {/tzdata.*>=/d}' pyproject.toml

%build
%if !%{with test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%{python_expand sed -i -e 's|"python", "-c",|"%{__$python}", "-c",|' %{buildroot}%{$python_sitearch}/pandas/tests/io/test_compression.py
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
# --skip-* arguments: Upstream's custom way to skip marked tests. These do not use pytest.mark.
SKIP_ARGS="--skip-network"
# clipboard not set up properly in build service without window manager
SKIP_MARKERS="clipboard"
# skip tests which upstream marked for -n 1 only.
SKIP_MARKERS+=" or single_cpu"
# pytest-xdist worker crash
SKIP_TESTS="test_pivot_number_of_levels_larger_than_int32"
# no locally running database server
SKIP_TESTS+=" or psycopg2_engine or psycopg2_conn or pymysql_engine or pymysql_conn"

%ifarch %{ix86} %{arm32}
# https://github.com/pandas-dev/pandas/issues/31856
SKIP_TESTS+=" or test_maybe_promote_int_with_int"
# rounding error
SKIP_TESTS+=" or (test_rolling_quantile_interpolation_options and data1 and linear and 0.1)"
# overflow
SKIP_TESTS+=" or test_large_string_pyarrow"
# dtype mismatch
SKIP_TESTS+=" or test_frame_setitem_dask_array_into_new_col"
# numba formats not supported on 32-bit
SKIP_TESTS+=" or numba"
%endif
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
%limit_build -m 3072

%{python_expand $python -c 'import pandas; print(pandas.__path__); print(pandas.show_versions())'
# cache: can't just say no cacheprovider, because one test checks for the --lf option of pytest-cache
xvfb-run pytest-%{$python_bin_suffix} -v -n %{jobs} -rsfE --dist=loadfile \
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
%{python_sitearch}/pandas-%{version}.dist-info

%files %{python_files test}
%license LICENSE
%doc README.md

%if !%{with ringdisabled}
%files %{python_files performance}
%license LICENSE
%doc README.md

%files %{python_files computation}
%license LICENSE
%doc README.md

%files %{python_files fss}
%license LICENSE
%doc README.md

%if %{with aws}
%files %{python_files aws}
%license LICENSE
%doc README.md
%endif

%if %{with gcp}
%files %{python_files gcp}
%license LICENSE
%doc README.md
%endif

%files %{python_files excel}
%license LICENSE
%doc README.md

%files %{python_files parquet}
%license LICENSE
%doc README.md

%files %{python_files feather}
%license LICENSE
%doc README.md

%files %{python_files hdf5}
%license LICENSE
%doc README.md

%files %{python_files spss}
%license LICENSE
%doc README.md

%files %{python_files postgresql}
%license LICENSE
%doc README.md

%files %{python_files mysql}
%license LICENSE
%doc README.md

%files %{python_files sql-other}
%license LICENSE
%doc README.md

%files %{python_files html}
%license LICENSE
%doc README.md

%files %{python_files xml}
%license LICENSE
%doc README.md

%files %{python_files plot}
%license LICENSE
%doc README.md

%files %{python_files output_formatting}
%license LICENSE
%doc README.md

%files %{python_files clipboard}
%license LICENSE
%doc README.md

%files %{python_files compression}
%license LICENSE
%doc README.md

%files %{python_files all}
%license LICENSE
%doc README.md
%endif
%endif

%changelog
