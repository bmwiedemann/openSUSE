#
# spec file for package python-scikit-image
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
Version:        0.23.2
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org/
# SourceRepository: https://github.com/scikit-image/scikit-image
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-image/%{srcname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skimage-pr7414-np2.patch gh#scikit-image/scikit-image#7414
Patch0:         https://github.com/scikit-image/scikit-image/pull/7414.patch#/skimage-pr7414-np2.patch
BuildRequires:  %{python_module Cython >= 3.0.4}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module meson-python >= 0.15}
BuildRequires:  %{python_module numpy-devel >= 1.23}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pythran}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 9.1
Requires:       python-PyWavelets >= 1.1.1
Requires:       python-imageio >= 2.33
Requires:       python-lazy-loader >= 0.4
Requires:       python-networkx >= 2.8
Requires:       python-numpy >= 1.23
Requires:       python-packaging >= 21.0
Requires:       python-scipy >= 1.9
Requires:       python-tifffile >= 2022.8.12
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-QtPy
Recommends:     python-SimpleITK
Recommends:     python-astropy >= 3.1.2
Recommends:     python-cloudpickle >= 0.2.1
Recommends:     python-dask-array >= 1.0.0
Recommends:     python-imread >= 0.5.1
Recommends:     python-matplotlib >= 3.6
Recommends:     python-pooch >= 1.3.0
Recommends:     python-pyamg
%if %{with test}
BuildRequires:  %{python_module dask-array >= 1.0.0}
BuildRequires:  %{python_module matplotlib >= 3.6}
BuildRequires:  %{python_module numpydoc}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scikit-image = %{version}}
%endif
# /SECTION
%python_subpackages

%description
Scikit-image is a collection of algorithms for image processing in Python.
It is available free of charge and free of restriction.

%prep
%if !%{with test}
%autosetup -p1 -n %{srcname}-%{version}
sed -Ei "1{s@/usr/bin/env python@%{_bindir}/python3@}" ./skimage/_build_utils/*.py
chmod -x skimage/measure/{__init__,_find_contours}.py
%else
%setup -q -c scikit-image-%{version}-test -D -T
%endif

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
# fails randomly https://github.com/scikit-image/scikit-image/issues/3237
donttest+="test_wrap_around"
# fails randomly on all platforms
donttest+=" or test_structural_similarity_dtype"
# https://github.com/scikit-image/scikit-image/issues/7051
donttest+=" or test_ellipse_parameter_stability"
# Another floating point flaky test (works for now, but let's keep it commented just in case)
#donttest+=" or test_clear_border_non_binary_out"
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
%pytest_arch -v --pyargs skimage -n auto -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt TODO.txt
%{python_sitearch}/skimage/
%{python_sitearch}/scikit_image-%{version}*-info
%endif

%changelog
