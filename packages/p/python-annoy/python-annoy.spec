#
# spec file for package python-annoy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python36 1
Name:           python-annoy
Version:        1.17.1
Release:        0
Summary:        Approximation of Nearest Neighbors
License:        Apache-2.0
URL:            https://github.com/spotify/annoy
Source:         https://github.com/spotify/annoy/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE boo#1100677
Patch0:         reproducible.patch
Patch1:         denose.patch
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Annoy (Approximate Nearest Neighbors) is a C++ library with Python
bindings to search for points in space that are close to a given
query point. It also creates large read-only file-based data
structures that are mmapped into memory so that many processes may
share the same data.

%prep
%setup -q -n annoy-%{version}
%patch0 -p1
%patch1 -p1
# fix testdata location
sed -i -e "s:'test/test:'test:g" test/index_test.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# online tests: test_fashion_mnist, test_glove_25, test_nytimes_16
# fails on 32bit: test_distance_consistency
# fails on 32bit: test_very_large_index
# flakey on Python 3.6: AngularIndexTest.test_include_dists
cd test
%pytest_arch -k 'not (test_fashion_mnist or test_glove_25 or test_nytimes_16 or test_distance_consistency or test_very_large_index or (AngularIndexTest and test_include_dists))'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
