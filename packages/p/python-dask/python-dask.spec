#
# spec file for package python-dask
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-dask%{psuffix}
Version:        2.8.0
Release:        0
Summary:        Minimal task scheduling abstraction
License:        BSD-3-Clause
URL:            https://github.com/ContinuumIO/dask/
Source:         https://files.pythonhosted.org/packages/source/d/dask/dask-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-toolz >= 0.7.3
Requires:       python-tornado >= 5
Recommends:     %{name}-array = %{version}
Recommends:     %{name}-bag = %{version}
Recommends:     %{name}-dataframe = %{version}
Recommends:     %{name}-distributed = %{version}
Recommends:     %{name}-dot = %{version}
Recommends:     %{name}-multiprocessing = %{version}
Recommends:     python-cachey
Recommends:     python-chest
Recommends:     python-cytoolz >= 0.7.3
Recommends:     python-hdfs3
Recommends:     python-lz4
Recommends:     python-lzmaffi
Recommends:     python-s3fs >= 0.0.8
Recommends:     python-scipy
Recommends:     python-snappy
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module bcolz}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module cachey}
BuildRequires:  %{python_module chest}
BuildRequires:  %{python_module cloudpickle >= 0.2.1}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module fsspec >= 0.5.1}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module lzmaffi}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module multipledispatch}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 0.19.0}
BuildRequires:  %{python_module pandas-datareader}
BuildRequires:  %{python_module partd >= 0.3.7}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module s3fs >= 0.0.8}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tables}
BuildRequires:  %{python_module tornado >= 5}
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  python-mock
BuildRequires:  python3-sparse
BuildConflicts: python3-buildservice-tweak
%endif
%python_subpackages

%description
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

# This must have a Requires for dask and all the dask subpackages
%package all
Summary:        All dask components
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       %{name}-bag = %{version}
Requires:       %{name}-dataframe = %{version}
Requires:       %{name}-distributed = %{version}
Requires:       %{name}-dot = %{version}
Requires:       %{name}-multiprocessing = %{version}

%description all
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package pulls in all the optional dask components.

%package array
Summary:        Numpy-like array data structure for dask
Requires:       %{name} = %{version}
Requires:       python-numpy >= 1.13.0
Recommends:     python-chest
Recommends:     python-h5py
Recommends:     python-pandas
Recommends:     python-scikit-image
Recommends:     python-scipy

%description array
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the dask array class.

Dask arrays implement a subset of the NumPy interface on large
arrays using blocked algorithms and task scheduling.

%package bag
Summary:        Data structure generic python objects in dask
Requires:       %{name} = %{version}
Requires:       %{name}-multiprocessing = %{version}
Requires:       python-cloudpickle >= 0.2.1
Requires:       python-fsspec >= 0.5.1
Requires:       python-partd >= 0.3.10

%description bag
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the dask bag class.

Dask.Bag parallelizes computations across a large collection of
generic Python objects. It is particularly useful when dealing
with large quantities of semi-structured data like JSON blobs
or log files.

%package dataframe
Summary:        Pandas-like DataFrame data structure for dask
Requires:       %{name} = %{version}
Requires:       %{name}-array = %{version}
Requires:       %{name}-multiprocessing = %{version}
Requires:       python-fsspec >= 0.5.1
Requires:       python-numpy >= 1.13.0
Requires:       python-pandas >= 0.21.0
Requires:       python-partd >= 0.3.10
Requires:       python-six
Recommends:     %{name}-bag = %{version}
Recommends:     python-SQLAlchemy
Recommends:     python-bcolz
Recommends:     python-chest
Recommends:     python-fastparquet
Recommends:     python-pandas-datareader
Recommends:     python-psutil
Recommends:     python-pyarrow

%description dataframe
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the dask DataFrame class.

A Dask DataFrame is a large parallel dataframe composed of many
smaller Pandas dataframes, split along the index. These pandas
dataframes may live on disk for larger-than-memory computing
on a single machine, or on many different machines in a cluster.

%package distributed
Summary:        Interface with the distributed task scheduler in dask
Requires:       %{name} = %{version}
Requires:       python-distributed >= 2.0

%description distributed
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the dask distributed interface.

Dask.distributed is a lightweight library for distributed computing in
Python. It extends both the concurrent.futures and dask APIs to
moderate sized clusters.

%package dot
Summary:        Display dask graphs using graphviz
Requires:       %{name} = %{version}
Requires:       graphviz
Requires:       graphviz-gd
Requires:       graphviz-gnome
Requires:       python-graphviz

%description dot
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the graphviz dot rendering interface.

%package multiprocessing
Summary:        Display dask graphs using graphviz
Requires:       %{name} = %{version}
Requires:       python-cloudpickle >= 0.2.1
Requires:       python-partd >= 0.3.7

%description multiprocessing
A minimal task scheduling abstraction and parallel arrays.
* dask is a specification to describe task dependency graphs.
* dask.array is a drop-in NumPy replacement (for a subset of NumPy) that
  encodes blocked algorithms in dask dependency graphs.
* dask.async is a shared-memory asynchronous scheduler that efficiently
  executes dask dependency graphs on multiple cores.

This package contains the multiprocessing interface.

%prep
%setup -q -n dask-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# Tests need network:
#   test_await
#   test_serializable_groupby_agg
#   test_persist
#   test_local_get_with_distributed_active
#   test_local_scheduler
%pytest dask/tests -k 'not (test_serializable_groupby_agg or test_persist or test_local_get_with_distributed_active or test_await or test_local_scheduler)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/dask/
%{python_sitelib}/dask-%{version}-py*.egg-info
%exclude %{python_sitelib}/dask/array/
%exclude %{python_sitelib}/dask/bag/
%exclude %{python_sitelib}/dask/dataframe/
%exclude %{python_sitelib}/dask/distributed.py*
%exclude %{python_sitelib}/dask/dot.py*
%exclude %{python_sitelib}/dask/multiprocessing.py*
%exclude %{python3_sitelib}/dask/__pycache__/distributed.*
%exclude %{python3_sitelib}/dask/__pycache__/dot.*
%exclude %{python3_sitelib}/dask/__pycache__/multiprocessing.*

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
%{python_sitelib}/dask/distributed.py*
%python3_only %{python_sitelib}/dask/__pycache__/distributed.*

%files %{python_files dot}
%license LICENSE.txt
%{python_sitelib}/dask/dot.py*
%python3_only %{python_sitelib}/dask/__pycache__/dot.*

%files %{python_files multiprocessing}
%license LICENSE.txt
%{python_sitelib}/dask/multiprocessing.py*
%python3_only %{python_sitelib}/dask/__pycache__/multiprocessing.*
%endif

%changelog
