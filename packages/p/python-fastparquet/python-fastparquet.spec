#
# spec file for package python-fastparquet
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
%define         skip_python2 1
Name:           python-fastparquet
Version:        0.5.0
Release:        0
Summary:        Python support for Parquet file format
License:        Apache-2.0
URL:            https://github.com/dask/fastparquet/
Source:         https://github.com/dask/fastparquet/archive/%{version}.tar.gz#/fastparquet-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module bson}
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module lz4 >= 0.19.1}
BuildRequires:  %{python_module numba >= 0.49}
BuildRequires:  %{python_module numpy-devel >= 1.11}
BuildRequires:  %{python_module pandas >= 1.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lzo}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module thrift >= 0.11.0}
BuildRequires:  %{python_module zstandard}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.49
Requires:       python-numpy >= 1.11
Requires:       python-pandas >= 1.1.0
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
# remove pytest-runner from setup_requires
sed -i "s/'pytest-runner',//" setup.py
# the tests import the fastparquet.test module and we need to import from sitearch, so install it.
sed -i -e "s/^\s*packages=\[/&'fastparquet.test', /" -e "/exclude_package_data/ d" setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand rm -v %{buildroot}%{$python_sitearch}/fastparquet/speedups.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# newer packaging package creates false DeprecationWarning gh#dask/fastparquet#558
donttest+=" or test_import_without_warning"
# Test test_time_millis has the wrong reference type for 32-bit
%if 0%{?__isa_bits} != 64
donttest+=" or test_time_millis"
%endif
%pytest_arch --pyargs fastparquet --import-mode append -k "not (${donttest:4})"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/fastparquet
%{python_sitearch}/fastparquet-%{version}*-info

%changelog
