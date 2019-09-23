#
# spec file for package python2-scikit-image
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python3 1
%define         oldpython python
# Test discovery issues
%bcond_with tests
Name:           python2-scikit-image
Version:        0.14.2
Release:        0
Summary:        Collection of algorithms for image processing in Python
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            http://scikit-image.org/
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
Requires:       python2-Pillow >= 2.1.0
Requires:       python2-PyWavelets >= 0.4.0
Requires:       python2-matplotlib >= 1.3.1
Requires:       python2-networkx >= 1.8
Requires:       python2-numpy >= 1.11
Requires:       python2-scipy >= 0.17
Requires:       python2-six >= 1.7.3
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python2-SimpleITK
Recommends:     python2-astropy
Recommends:     python2-dask-array >= 0.5.0
Recommends:     python2-imread
Recommends:     python2-pyamg
Recommends:     python2-qt4
%if %{with tests}
# Runtime dependencies
BuildRequires:  %{python_module Pillow >= 2.1.0}
BuildRequires:  %{python_module PyWavelets >= 0.4.0}
BuildRequires:  %{python_module matplotlib >= 1.3.1}
BuildRequires:  %{python_module networkx >= 1.8}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
%endif
Provides:       %{oldpython}-scikits-image = %{version}
Obsoletes:      %{oldpython}-scikits-image < %{version}
%python_subpackages

%description
Scikit-image is a collection of algorithms for image processing in Python.
It is available free of charge and free of restriction.

%prep
%setup -q -n scikit-image-%{version}

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

%if %{with tests}
%check
mkdir tester
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
py.test-%{$python_bin_suffix} -v skimage
}
popd
rm -r tester
%endif

%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTING.txt CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/skivi
%{python_sitearch}/skimage/
%{python_sitearch}/scikit_image-%{version}-py*.egg-info

%changelog
