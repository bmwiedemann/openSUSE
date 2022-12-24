#
# spec file for package python-fastparquet
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


Name:           python-fastparquet
Version:        0.8.3
Release:        0
Summary:        Python support for Parquet file format
License:        Apache-2.0
URL:            https://github.com/dask/fastparquet/
Source:         https://github.com/dask/fastparquet/archive/%{version}.tar.gz#/fastparquet-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fastparquet-pr813-updatefixes.patch gh#dask/fastparquet#813
Patch1:         fastparquet-pr813-updatefixes.patch
# PATCH-FIX-UPSTREAM fastparquet-pr835.patch gh#dask/fastparquet#835
Patch2:         fastparquet-pr835.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module cramjam >= 2.3.0}
# version requirement not declared for runtime, but necessary for tests.
BuildRequires:  %{python_module fsspec >= 2021.6.0}
BuildRequires:  %{python_module numpy-devel >= 1.20.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 1.5.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lzo}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cramjam >= 2.3.0
Requires:       python-fsspec
Requires:       python-numpy >= 1.20.3
Requires:       python-packaging
Requires:       python-pandas >= 1.5.0
Recommends:     python-python-lzo
%python_subpackages

%description
This is a Python implementation of the parquet format
for integrating it into python-based Big Data workflows.

%prep
%autosetup -p1 -n fastparquet-%{version}
# remove pytest-runner from setup_requires
sed -i "s/'pytest-runner',//" setup.py
# this is not meant for setup.py
sed -i "s/oldest-supported-numpy/numpy/" setup.py
# the tests import the fastparquet.test module and we need to import from sitearch, so install it.
sed -i -e "s/^\s*packages=\[/&'fastparquet.test', /" -e "/exclude_package_data/ d" setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand rm -v %{buildroot}%{$python_sitearch}/fastparquet/{speedups,cencoding}.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --pyargs fastparquet --import-mode append -n auto

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/fastparquet
%{python_sitearch}/fastparquet-%{version}*-info

%changelog
