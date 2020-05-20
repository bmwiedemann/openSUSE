#
# spec file for package python-scikit-image
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
%define skip_python2 1
Name:           python-scikit-image
Version:        0.16.2
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org/
Source0:        https://files.pythonhosted.org/packages/source/s/scikit-image/scikit-image-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.23.4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.11}
BuildRequires:  %{python_module scipy >= 0.17}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.3}
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 2.1.0
Requires:       python-PyWavelets >= 0.4.0
Requires:       python-matplotlib >= 1.3.1
Requires:       python-networkx >= 1.8
Requires:       python-numpy >= 1.11
Requires:       python-scipy >= 0.17
Requires:       python-six >= 1.7.3
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-SimpleITK
Recommends:     python-astropy
Recommends:     python-dask-array >= 0.5.0
Recommends:     python-imread
Recommends:     python-pyamg
Recommends:     python-qt4
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 2.1.0}
BuildRequires:  %{python_module PyWavelets >= 0.4.0}
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module matplotlib >= 1.3.1}
BuildRequires:  %{python_module networkx >= 1.8}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%python_subpackages

%description
Scikit-image is a collection of algorithms for image processing in Python.
It is available free of charge and free of restriction.

%prep
%setup -q -n scikit-image-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/skivi

%post
%python_install_alternative skivi

%preun
%python_uninstall_alternative skivi

%check
export PYTHONDONTWRITEBYTECODE=1 # do not write unreproducible test_random_walker.cpython-37-PYTEST.pyc files (boo#1062303)
mv skimage skimage_temp
# test_wrap_around - fails randomly https://github.com/scikit-image/scikit-image/issues/3237
# test_structural_similarity_dtype - also fails randomly on 32bit
%pytest_arch -v %{buildroot}%{$python_sitearch}/skimage -n auto -k 'not (test_wrap_around or test_structural_similarity_dtype)'
mv skimage_temp skimage

%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/skivi
%{python_sitearch}/skimage/
%{python_sitearch}/scikit_image-%{version}-py*.egg-info

%changelog
