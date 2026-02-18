#
# spec file for package python-scikit-image
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define srcname scikit_image
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-scikit-image%{psuffix}
Version:        0.26.0
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org/
# SourceRepository: https://github.com/scikit-image/scikit-image
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-image/%{srcname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#scikit-image/scikit-image#8010
Patch0:         support-new-pillow.patch
BuildRequires:  %{python_module Cython >= 3.0.4}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module meson-python >= 0.15}
BuildRequires:  %{python_module numpy-devel >= 1.24}
BuildRequires:  %{python_module packaging >= 21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pythran}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 10.1
Requires:       python-imageio >= 2.33
Requires:       python-lazy-loader >= 0.4
Requires:       python-networkx >= 3
Requires:       python-numpy >= 1.24
Requires:       python-packaging >= 21.0
Requires:       python-scipy >= 1.11.4
Requires:       python-tifffile >= 2022.8.12
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-PyWavelets >= 1.6
Recommends:     python-QtPy
Recommends:     python-SimpleITK
Recommends:     python-astropy >= 5
Recommends:     python-cloudpickle >= 1.1.1
Recommends:     python-dask-array >= 2023.2.0
Recommends:     python-matplotlib >= 3.7
Recommends:     python-pooch >= 1.6.0
Recommends:     python-pyamg >= 5.2
%if %{with test}
BuildRequires:  %{python_module dask-array >= 2023.2.0}
BuildRequires:  %{python_module matplotlib >= 3.7}
BuildRequires:  %{python_module numpydoc >= 1.7}
BuildRequires:  %{python_module pytest >= 8}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-pretty}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scikit-image = %{version}}
%endif
# /SECTION
%python_subpackages

%description
Scikit-image is a collection of algorithms for image processing in Python.
It is available free of charge and free of restriction.

%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -Ei "1{s@/usr/bin/env python\$@%{_bindir}/python3@}" ./src/skimage/_build_utils/*.py
# don't install the header file
sed -i '/fast_exp.h/d' ./src/skimage/_shared/meson.build
chmod -x src/skimage/measure/{__init__,_find_contours}.py

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# fails randomly gh#scikit-image/scikit-image#3237
donttest+="test_wrap_around"
# fails randomly on all platforms
donttest+=" or test_structural_similarity_dtype"
# gh#scikit-image/scikit-image#7051 -- works locally but not on obs
donttest+=" or test_ellipse_parameter_stability"
# gh#scikit-image/scikit-image#7491, gh#scikit-image/scikit-image#7509
donttest+=" or test_thresholds_dask_compatibility"
# Another floating point flaky test (works for now, but let's keep it commented just in case)
#donttest+=" or test_clear_border_non_binary_out"
# test collection with xdist not in deterministic order gh#pytest-dev/pytest-xdist#432
notparallel="test_all_numeric_types"
# These try to copy an array if we're on 32 bits
if [ $(getconf LONG_BIT) -eq 32 ]; then
    donttest+=" or test_binary_descriptors_rotation_crosscheck"
    donttest+=" or test_normal_mode or test_uniform_mode or test_border"
    donttest+=" or test_independent_rng"
fi
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
%pytest_arch -v --pyargs skimage -n auto -k "not ($donttest or $notparallel)" tests
%pytest_arch -v --pyargs skimage -k "not ($donttest) and ($notparallel)" tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.md TODO.txt
%{python_sitearch}/skimage/
%{python_sitearch}/skimage2/
%{python_sitearch}/scikit_image-%{version}.dist-info
%endif

%changelog
