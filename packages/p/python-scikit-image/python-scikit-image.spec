#
# spec file for package python-scikit-image
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
%define skip_python2 1
# SciPy 1.6.0 dropped Python 3.6 and numpy 1.20 will soon
%define skip_python36 1
Name:           python-scikit-image%{psuffix}
Version:        0.18.1
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-image/scikit-image-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.13}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.15.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 4.3.0
Requires:       python-PyWavelets >= 1.1.1
Requires:       python-imageio >= 2.3.0
Requires:       python-matplotlib >= 2.0.0
Requires:       python-networkx >= 2.0
Requires:       python-numpy >= 1.15.1
Requires:       python-scipy >= 1.0.1
Requires:       python-tifffile >= 2019.7.26
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-QtPy
Recommends:     python-SimpleITK
Recommends:     python-astropy >= 1.2.0
Recommends:     python-cloudpickle >= 0.2.1
Recommends:     python-dask-array >= 0.15.0
Recommends:     python-imread >= 0.5.1
Recommends:     python-pyamg
Recommends:     python-pooch >= 0.5.2
%if %{with test}
BuildRequires:  %{python_module Pillow >= 4.3.0}
BuildRequires:  %{python_module PyWavelets >= 1.1.1}
BuildRequires:  %{python_module imageio >= 2.3.0}
BuildRequires:  %{python_module matplotlib >= 2.0.0}
BuildRequires:  %{python_module networkx >= 2.0}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scikit-image = %{version}}
BuildRequires:  %{python_module scipy >= 1.0.1}
BuildRequires:  %{python_module tifffile >= 2019.7.26}
%endif
# /SECTION
%python_subpackages

%description
Scikit-image is a collection of algorithms for image processing in Python.
It is available free of charge and free of restriction.

%prep
%if !%{with test}
%setup -q -n scikit-image-%{version}
#remove shebang
sed -i '1 {\@usr/bin/env@ d}' skimage/*/setup.py skimage/future/graph/setup.py
%else
%setup -q -c scikit-image-%{version}-test -D -T
%endif

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/skivi
%endif

%if !%{with test}
%post
%python_install_alternative skivi

%preun
%python_uninstall_alternative skivi
%endif

%if %{with test}
%check
# test_wrap_around - fails randomly https://github.com/scikit-image/scikit-image/issues/3237
skiptests="test_wrap_around"
# test_structural_similarity_dtype - also fails randomly on 32bit
skiptests+=" or test_structural_similarity_dtype"
# test_colorconv.py hdx and hed tests segfault
skiptests+=" or test_hdx_rgb or test_hed_rgb"
# these test require pooch to download data files, which we don't have and which needs internet to work anyway
# see skimage/data/_registry.py
skiptests+=" or test_ndim or test_skin or test_custom_load_func_w_kwarg"
%pytest_arch -v --pyargs skimage -n auto -k "not ($skiptests)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/skivi
%{python_sitearch}/skimage/
%{python_sitearch}/scikit_image-%{version}-py*.egg-info
%endif

%changelog
