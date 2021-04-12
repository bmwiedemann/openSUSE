#
# spec file for package python-dask-test
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-dask%{psuffix}
Version:        2021.4.0
Release:        0
Summary:        Minimal task scheduling abstraction
License:        BSD-3-Clause
URL:            https://dask.org
Source:         https://files.pythonhosted.org/packages/source/d/dask/dask-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-cloudpickle >= 1.1.1
Requires:       python-fsspec >= 0.6.0
Requires:       python-partd >= 0.3.10
Requires:       python-toolz >= 0.8.2
Recommends:     %{name}-array = %{version}
Recommends:     %{name}-bag = %{version}
Recommends:     %{name}-dataframe = %{version}
Recommends:     %{name}-delayed = %{version}
Recommends:     %{name}-distributed = %{version}
Recommends:     %{name}-dot = %{version}
Recommends:     python-SQLAlchemy
Recommends:     python-cityhash
Recommends:     python-distributed >= %{version}
Recommends:     python-fastparquet
Recommends:     python-gcsfs >= 0.4.0
Recommends:     python-murmurhash
Recommends:     python-psutil
Recommends:     python-pyarrow >= 0.14.0
Recommends:     python-s3fs >= 0.4.0
Recommends:     python-xxhash
Suggests:       %{name}-all = %{version}
Suggests:       %{name}-diagnostics = %{version}
Provides:       %{name}-multiprocessing = %{version}-%{release}
Obsoletes:      %{name}-multiprocessing < %{version}-%{release}
BuildArch:      noarch
%if %{with test}
# test that we specified all requirements correctly in the core
# and subpackages by only requiring dask-all and optional extras
BuildRequires:  %{python_module dask-all = %{version}}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# SECTION additional optionally tested (importorskip) packages
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module cachey}
BuildRequires:  %{python_module fastparquet}
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
BuildRequires:  %{python_module scikit-image}
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

%package all
# This must have a Requires for dask and all the dask subpackages
Summary:        All dask components
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       %{name}-bag = %{version}
Requires:       %{name}-dataframe = %{version}
Requires:       %{name}-delayed = %{version}
Requires:       %{name}-diagnostics = %{version}
Requires:       %{name}-distributed = %{version}
Requires:       %{name}-dot = %{version}

%description all
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
Requires:       python-numpy >= 1.16
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

%package bag
Summary:        Data structure generic python objects in dask
Requires:       %{name} = %{version}

%description bag
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the dask bag class.

Dask.Bag parallelizes computations across a large collection of
generic Python objects. It is particularly useful when dealing
with large quantities of semi-structured data like JSON blobs
or log files.

%package dataframe
Summary:        Pandas-like DataFrame data structure for dask
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       python-numpy >= 1.16
Requires:       python-pandas >= 0.25.0

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
Requires:       python-distributed >= %{version}

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
Requires:       python-bokeh >= 1.0.0

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

%package delayed
Summary:        Delayed module for dask
Requires:       %{name} = %{version}

%description delayed
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the dask.delayed module

%package dot
Summary:        Display dask graphs using graphviz
Requires:       %{name} = %{version}
Requires:       graphviz
Requires:       graphviz-gd
Requires:       graphviz-gnome
Requires:       python-graphviz

%description dot
A flexible library for parallel computing in Python.

Dask is composed of two parts:
- Dynamic task scheduling optimized for computation. This is similar to
  Airflow, Luigi, Celery, or Make, but optimized for interactive
  computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that
  extend common interfaces like NumPy, Pandas, or Python iterators to
  larger-than-memory or distributed environments. These parallel collections
  run on top of dynamic task schedulers.

This package contains the graphviz dot rendering interface.

%prep
%autosetup -p1 -n dask-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
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
# distributed/pytest-asyncio cancer is spreading
# https://github.com/dask/distributed/pull/4212 and https://github.com/pytest-dev/pytest-asyncio/issues/168
donttest+="or (test_distributed and test_annotations_blockwise_unpack)"
donttest+="or (test_distributed and test_persist)"
donttest+="or (test_distributed and test_local_get_with_distributed_active)"
donttest+="or (test_distributed and test_serializable_groupby_agg)"
donttest+="or (test_distributed and test_await)"
%pytest --pyargs dask -ra -m "not network" -k "not ($donttest)" -n auto
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/dask/
%{python_sitelib}/dask-%{version}*-info
%exclude %{python_sitelib}/dask/array/
%exclude %{python_sitelib}/dask/bag/
%exclude %{python_sitelib}/dask/dataframe/
%exclude %{python_sitelib}/dask/diagnostics
%exclude %{python_sitelib}/dask/delayed.py*
%exclude %{python_sitelib}/dask/dot.py*
%pycache_only %exclude %{python_sitelib}/dask/__pycache__/delayed*.pyc
%pycache_only %exclude %{python_sitelib}/dask/__pycache__/dot.*

%files %{python_files all}
%license LICENSE.txt

%files %{python_files array}
%license LICENSE.txt
%{python_sitelib}/dask/array/

%files %{python_files bag}
%license LICENSE.txt
%{python_sitelib}/dask/bag/

%files %{python_files dataframe}
%license LICENSE.txt
%{python_sitelib}/dask/dataframe/

%files %{python_files distributed}
%license LICENSE.txt

%files %{python_files dot}
%license LICENSE.txt
%{python_sitelib}/dask/dot.py*
%pycache_only %{python_sitelib}/dask/__pycache__/dot.*

%files %{python_files diagnostics}
%license LICENSE.txt
%{python_sitelib}/dask/diagnostics/

%files %{python_files delayed}
%license LICENSE.txt
%{python_sitelib}/dask/delayed.py*
%pycache_only %{python_sitelib}/dask/__pycache__/delayed*.pyc
%endif

%changelog
