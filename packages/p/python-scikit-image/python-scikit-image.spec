#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-scikit-image%{psuffix}
Version:        0.19.3
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-image/scikit-image-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skimage-fix-module-install.patch -- gh#scikit-image/scikit-image#6428
Patch0:         skimage-fix-module-install.patch
BuildRequires:  %{python_module Cython >= 0.29.21}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.17.0}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pythran}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 6.1.0
Requires:       python-PyWavelets >= 1.1.1
Requires:       python-imageio >= 2.4.1
Requires:       python-networkx >= 2.2
Requires:       python-numpy >= 1.17.0
Requires:       python-packaging >= 20.0
Requires:       python-scipy >= 1.4.1
Requires:       python-tifffile >= 2019.7.26
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-QtPy
Recommends:     python-SimpleITK
Recommends:     python-astropy >= 3.1.2
Recommends:     python-cloudpickle >= 0.2.1
Recommends:     python-dask-array >= 1.0.0
Recommends:     python-imread >= 0.5.1
Recommends:     python-matplotlib >= 3.0.3
Recommends:     python-pooch >= 1.3.0
Recommends:     python-pyamg
%if %{with test}
BuildRequires:  %{python_module dask-array >= 1.0.0}
BuildRequires:  %{python_module matplotlib >= 3.0.3}
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
%autosetup -p1 -n scikit-image-%{version}
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

%postun
%python_uninstall_alternative skivi
%endif

%if %{with test}
%check
# fails randomly https://github.com/scikit-image/scikit-image/issues/3237
donttest+="test_wrap_around"
# fails randomly on all platforms
donttest+=" or test_structural_similarity_dtype"
%pytest_arch -v --pyargs skimage -n auto -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/skivi
%{python_sitearch}/skimage/
%{python_sitearch}/scikit_image-%{version}*-info
%endif

%changelog
