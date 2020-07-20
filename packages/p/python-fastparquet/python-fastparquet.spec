#
# spec file for package python-fastparquet
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
Name:           python-fastparquet
Version:        0.4.1
Release:        0
Summary:        Python support for Parquet file format
License:        Apache-2.0
URL:            https://github.com/dask/fastparquet/
Source:         https://github.com/dask/fastparquet/archive/%{version}.tar.gz#/fastparquet-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module bson}
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module lz4 >= 0.19.1 }
BuildRequires:  %{python_module numba >= 0.28}
BuildRequires:  %{python_module numpy-devel >= 1.11}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 0.19}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lzo}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module thrift >= 0.11.0}
BuildRequires:  %{python_module zstandard}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.28
Requires:       python-numpy >= 1.11
Requires:       python-packaging
Requires:       python-pandas
Requires:       python-six
Requires:       python-thrift >= 0.11.0
Recommends:     python-Brotli
Recommends:     python-bson
Recommends:     python-lz4 >= 0.19.1
Recommends:     python-python-lzo
Recommends:     python-python-snappy
Recommends:     python-zstandard
%python_subpackages

%description
This is a Python implementation of the parquet format
for integrating it into python-based Big Data workflows.

%prep
%setup -q -n fastparquet-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand rm -v %{buildroot}%{$python_sitearch}/fastparquet/speedups.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cp -r fastparquet/test .
mv fastparquet temp
rm -rf build _build*
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
rm -rf build _build*
# Test test_time_millis fails in i586
# test_datetime_roundtrip fails due to a warning being accidentally caught by the test
# test_import_without_warning fails due to being already imported
pytest-%{$python_bin_suffix} -v test -k 'not test_time_millis and not test_datetime_roundtrip and not test_errors and not test_import_without_warning'
}
mv temp fastparquet
rm -rf test

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitearch}/fastparquet
%{python_sitearch}/fastparquet/*
%dir %{python_sitearch}/fastparquet-%{version}-py*.egg-info
%{python_sitearch}/fastparquet-%{version}-py*.egg-info/*

%changelog
