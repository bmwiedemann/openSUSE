#
# spec file for package python-dtaidistance
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


%define         skip_python2 1
Name:           python-dtaidistance
Version:        2.3.10
Release:        0
Summary:        Dynamic Time Warping (DTW) package
License:        Apache-2.0
URL:            https://github.com/wannesm/dtaidistance
Source:         https://github.com/wannesm/dtaidistance/archive/v%{version}.tar.gz#/dtaidistance-%{version}.tar.gz
#PATCH-FIX-UPSTREAM https://github.com/wannesm/dtaidistance/commit/a4b4bbf4be5bac7b95210b993ee24213bc2a0a36 Fix build for Cython v3.0.0
Patch:          cython3.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# NEP 29: python36-numpy is not in TW anymore. This package can build a basic version without numpy
BuildRequires:  %{python_module numpy-devel if (%python-base without python36-base)}
Recommends:     python-jinja2
Recommends:     python-matplotlib
Recommends:     python-numpy
Recommends:     python-scipy
Recommends:     python-tqdm
# SECTION test requirements
BuildRequires:  %{python_module pytest-env}
BuildRequires:  %{python_module pytest}
# NEP 29: python36-scipy is not in TW anymore
BuildRequires:  %{python_module matplotlib if (%python-base without python36-base)}
BuildRequires:  %{python_module jinja2 if (%python-base without python36-base)}
BuildRequires:  %{python_module scipy if (%python-base without python36-base)}
# /SECTION
%python_subpackages

%description
Library for time series distances (e.g. Dynamic Time Warping, DTW).

%prep
%autosetup -p1 -n dtaidistance-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand find %{buildroot}%{$python_sitearch} -name '*.[ch]' -delete
%python_expand %fdupes %{buildroot}%{$python_sitearch}
find %{buildroot}/usr/lib*/python* -name compilation.log -delete

%check
# Test are too slow in x86
%ifnarch %{ix86}
# openMP library mismatch (symbol in libgomp not found) -- use use_mp=True"
donttest+=" or (test_clustering and test_clustering_tree_ndim)"
donttest+=" or (test_dtw and test_distance_matrix2_e)"
donttest+=" or (test_dtw and test_distance_matrix_block)"
donttest+=" or (test_dtw2d and test_distances1_fast_parallel)"
donttest+=" or (test_dtw2d and test_distances2_fast_parallel)"

# Broken tests with latest numpy >= 1.24
donttest+=" or test_bug3 or test_distance1_a"
%pytest_arch ${donttest:+ -k "not (${donttest:4})"} -m "not benchmark"
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/dtaidistance
%{python_sitearch}/dtaidistance-%{version}-py*.egg-info

%changelog
