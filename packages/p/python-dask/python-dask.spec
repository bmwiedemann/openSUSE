#
# spec file for package python-dask
#
# Copyright (c) 2024 SUSE LLC
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
%{?sle15_python_module_pythons}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%bcond_without test
%define psuffix -%{flavor}
%if 0%{suse_version} >= 1599
%if "%{flavor}" != "test-py310"
%define skip_python310 1
%endif
%if "%{flavor}" != "test-py311"
%define skip_python311 1
%endif
%if "%{flavor}" != "test-py312"
%define skip_python312 1
%endif
%if "%{flavor}" != "test-py313"
%define skip_python313 1
%endif
%else
%if "%{pythons}" == "python311" && "%{flavor}" != "test-py311"
# Hardcoded assumption: SLE15 pythons module has python311
%define pythons %{nil}
%endif
%endif
%endif
%if "%{shrink:%pythons}" == ""
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%endif

Name:           python-dask%{psuffix}
# ===> Note: python-dask MUST be updated in sync with python-dask-expr,python-distributed! <===
Version:        2024.12.0
Release:        0
Summary:        Minimal task scheduling abstraction
License:        BSD-3-Clause
URL:            https://dask.org
# SourceRepository: https://github.com/dask/dask
Source0:        https://files.pythonhosted.org/packages/source/d/dask/dask-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer-toml >= 0.29}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.3.1
Requires:       python-click >= 8.1
Requires:       python-cloudpickle >= 3.0
Requires:       python-fsspec >= 2021.9
Requires:       python-packaging >= 20.0
Requires:       python-partd >= 1.4.0
Requires:       python-toolz >= 0.10.0
Requires:       (python-cloudpickle >= 3.1 if python-base >= 3.13)
Requires:       (python-importlib-metadata >= 4.13.0 if python-base < 3.12)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-array = %{version}
Recommends:     %{name}-dataframe = %{version}
Recommends:     %{name}-distributed = %{version}
Suggests:       %{name}-complete = %{version}
Suggests:       %{name}-diagnostics = %{version}
# SECTION https://docs.dask.org/en/stable/install.html#optional-dependencies
Suggests:       python-SQLAlchemy >= 1.4.16
Suggests:       python-cityhash >= 0.2.4
Suggests:       python-fastparquet >= 0.8.2
Suggests:       python-gcsfs >= 2021.9.0
Suggests:       python-crick >= 0.0.3
Suggests:       python-cytoolz >= 0.10.1
Suggests:       python-dask-ml >= 1.4.0
Suggests:       python-fastavro >= 0.22.6
Suggests:       python-graphviz >= 0.8.4
Suggests:       python-h5py >= 2.10.0
Suggests:       python-psutil >= 0.5.7
Suggests:       python-pyarrow >= 14.0.1
Suggests:       python-matplotlib
Suggests:       python-mimesis >= 5.3.0
Suggests:       python-mmh3 >= 2.5.1
Suggests:       python-sparse >= 0.12.0
Suggests:       python-s3fs >= 0.4.0
Suggests:       python-xxhash >= 1.4.1
Suggests:       python-zarr >= 2.12.0
# /SECTION
Provides:       %{name}-bag = %{version}-%{release}
Obsoletes:      %{name}-bag < %{version}-%{release}
Provides:       %{name}-delayed = %{version}-%{release}
Obsoletes:      %{name}-delayed < %{version}-%{release}
Provides:       %{name}-dot = %{version}-%{release}
Obsoletes:      %{name}-dot < %{version}-%{release}
Provides:       %{name}-multiprocessing = %{version}-%{release}
Obsoletes:      %{name}-multiprocessing < %{version}-%{release}
BuildArch:      noarch
%if %{with test}
# test that we specified all requirements correctly in the core
# and subpackages by only requiring dask-test (= [complete] + pytest) and optional extras
BuildRequires:  %{python_module dask-test = %{version}}
# SECTION additional optionally tested (importorskip) packages
BuildRequires:  %{python_module SQLAlchemy >= 1.4.16}
BuildRequires:  %{python_module cachey}
BuildRequires:  %{python_module fastparquet >= 0.8.0}
# optional zarr increases fsspec miminum to 0.8.4 if present
BuildRequires:  %{python_module fsspec >= 0.8.4}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mimesis}
BuildRequires:  %{python_module multipledispatch}
BuildRequires:  %{python_module numba}
# snappy required for using fastparquet
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image if %python-base < 3.13}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sparse}
BuildRequires:  %{python_module tables}
BuildRequires:  %{python_module xarray}
BuildRequires:  %{python_module zarr}
# /SECTION
%endif
%python_subpackages

%description
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

%package complete
# This must have a Requires for dask and all the dask subpackages
Summary:        All dask components
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       %{name}-dataframe = %{version}
Requires:       %{name}-diagnostics = %{version}
Requires:       %{name}-distributed = %{version}
Requires:       python-lz4 >= 4.3.2
Requires:       python-pyarrow >= 7
Provides:       %{name}-all = %{version}-%{release}
Obsoletes:      %{name}-all < %{version}-%{release}

%description complete
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package pulls in all the optional dask components.

%package array
Summary:        Numpy-like array data structure for dask
Requires:       %{name} = %{version}
Requires:       %{name}-delayed = %{version}
Requires:       python-numpy >= 1.21
Recommends:     python-scipy

%description array
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the dask array class.

Dask arrays implement a subset of the NumPy interface on large
arrays using blocked algorithms and task scheduling.

%package dataframe
Summary:        Pandas-like DataFrame data structure for dask
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       %{name}-bag = %{version}
# This is an extra package
Requires:       (python-dask-expr >= 1.1 with python-dask-expr < 1.2)
Requires:       python-pandas >= 2

%description dataframe
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the dask DataFrame class.

A Dask DataFrame is a large parallel dataframe composed of many
smaller Pandas dataframes, split along the index. These pandas
dataframes may live on disk for larger-than-memory computing
on a single machine, or on many different machines in a cluster.

%package distributed
Summary:        Interface with the distributed task scheduler in dask
Requires:       %{name} = %{version}
# dask and distributed are always updated together
Requires:       python-distributed = %{version}

%description distributed
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This meta package pulls in the distributed module into the dask namespace.

%package diagnostics
Summary:        Diagnostics for dask
Requires:       %{name} = %{version}
Requires:       python-Jinja2 >= 2.10.3
Requires:       python-bokeh >= 3.1

%description diagnostics
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the dask.diagnostics module

%package test
Summary:        The test submodules of the python-dask package
Requires:       %{name}-complete = %{version}
Requires:       python-pandas-test
Requires:       python-pytest
Requires:       python-pytest-rerunfailures
Requires:       python-pytest-timeout
Requires:       python-pytest-xdist

%description test
Dask is a flexible library for parallel computing in Python.
This subpackage provides the .test submodules in the sitelib required for
unit testing dask.

%prep
%autosetup -p1 -n dask-%{version}
sed -i  '/addopts/d' pyproject.toml

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dask
%{python_expand # give SUSE specific install instructions
sed -E -i '/Please either conda or pip install/,/python -m pip install/ {
  s/either conda or pip//;
  /conda install/ d;
  s/python -m pip install "dask\[(.*)\]".*pip install/zypper in $python-dask-\1/
  }' \
  %{buildroot}%{$python_sitelib}/dask/distributed.py
sed -E -i '/Please either conda or pip install/,/python -m pip install/ c \
        "Please file a bug report https://bugzilla.opensuse.org and\\n"\
        "report the missing requirements."' \
  %{buildroot}%{$python_sitelib}/dask/array/__init__.py \
  %{buildroot}%{$python_sitelib}/dask/bag/__init__.py \
  %{buildroot}%{$python_sitelib}/dask/dataframe/__init__.py
}
%{python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# move away from importpath
mv dask dask.moved
# different seed or mimesis version
donttest="(test_datasets and test_deterministic)"
# upstreams test if their ci is up to date, irrelevant for obs
donttest+=" or test_development_guidelines_matches_ci"
if [[ $(getconf LONG_BIT) -eq 32 ]]; then
  # https://github.com/dask/dask/issues/8620
  donttest+=" or test_query_with_meta"
  donttest+=" or test_repartition_npartitions"
  #
  donttest+=" or test_pandas_multiindex"
  donttest+=" or test_categorize_info"
  donttest+=" or test_memory_usage_dataframe"
  donttest+=" or test_multi"
fi
# (rarely) flaky on obs
donttest+=" or test_local_scheduler"
donttest+=" or (test_threaded and test_interrupt)"
# perhaps? rh#1968947#c4
donttest+=" or test_select_from_select"
# tries to get an IP address
donttest+=" or test_map_partitions_df_input"
# needs s3fs support in arrow
donttest+=" or test_pyarrow_filesystem_option_real_data"
# different hash naming (?)
donttest+=" or test_to_delayed_optimize_graph"
%pytest --pyargs dask -n auto -r fE -m "not network" -k "not ($donttest)" --reruns 3 --reruns-delay 3
%endif

%post
%python_install_alternative dask

%postun
%python_uninstall_alternative dask

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/dask
%{python_sitelib}/dask/
%{python_sitelib}/dask-%{version}.dist-info
%exclude %{python_sitelib}/dask/array/
%exclude %{python_sitelib}/dask/dataframe/
%exclude %{python_sitelib}/dask/diagnostics
%exclude %{python_sitelib}/dask/tests
%exclude %{python_sitelib}/dask/bag/tests
%exclude %{python_sitelib}/dask/bytes/tests
%exclude %{python_sitelib}/dask/widgets/tests
%pycache_only %exclude %{python_sitelib}/dask/__pycache__/delayed*.pyc
%pycache_only %exclude %{python_sitelib}/dask/__pycache__/dot.*

%files %{python_files complete}
%license LICENSE.txt

%files %{python_files array}
%license LICENSE.txt
%{python_sitelib}/dask/array/
%exclude %{python_sitelib}/dask/array/tests

%files %{python_files dataframe}
%license LICENSE.txt
%{python_sitelib}/dask/dataframe/
%exclude %{python_sitelib}/dask/dataframe/tests
%exclude %{python_sitelib}/dask/dataframe/io/tests
%exclude %{python_sitelib}/dask/dataframe/tseries/tests

%files %{python_files distributed}
%license LICENSE.txt

%files %{python_files diagnostics}
%license LICENSE.txt
%{python_sitelib}/dask/diagnostics/
%exclude %{python_sitelib}/dask/diagnostics/tests

%files %{python_files test}
%license LICENSE.txt
%{python_sitelib}/dask/tests
%{python_sitelib}/dask/bytes/tests
%{python_sitelib}/dask/widgets/tests
%{python_sitelib}/dask/array/tests
%{python_sitelib}/dask/bag/tests
%{python_sitelib}/dask/dataframe/tests
%{python_sitelib}/dask/dataframe/io/tests
%{python_sitelib}/dask/dataframe/tseries/tests
%{python_sitelib}/dask/diagnostics/tests
%endif

%changelog
