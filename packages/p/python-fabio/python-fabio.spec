#
# spec file for package python-fabio
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


%define packagename fabio
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fabio
Version:        0.11.0
Release:        0
Summary:        Image IO for images produced by 2D X-ray detectors
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT
URL:            https://github.com/silx-kit/fabio
Source:         https://github.com/silx-kit/fabio/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module numpy >= 1.19.1}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-h5py
Requires:       python-lxml
Requires:       python-numpy >= 1.19.1
Requires:       python-qt5
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
# This package does not support 32 bit arch.
ExcludeArch:    i586 %{arm}
%python_subpackages

%description
FabIO is an I/O library for images produced by 2D X-ray detectors.

%prep
%autosetup -n %{packagename}-%{version}
# Fix W: non-executable-script
grep -ElRZ '*.py' . | xargs -0 -l sed -i '/^#!/d'

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/fabio-convert
%python_clone -a %{buildroot}%{_bindir}/fabio_viewer
%python_clone -a %{buildroot}%{_bindir}/eiger2cbf
%python_clone -a %{buildroot}%{_bindir}/eiger2crysalis
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%prepare_alternative fabio-convert fabio_viewer eiger2cbf eiger2crysalis

%post
%python_install_alternative fabio-convert fabio_viewer eiger2cbf eiger2crysalis

%postun
%python_uninstall_alternative fabio-convert fabio_viewer eiger2cbf eiger2crysalis

%check
# Does not support pytest
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license copyright
%python_alternative %{_bindir}/fabio-convert
%python_alternative %{_bindir}/fabio_viewer
%python_alternative %{_bindir}/eiger2cbf
%python_alternative %{_bindir}/eiger2crysalis
%{python_sitearch}/*egg-info
%{python_sitearch}/%{packagename}

%changelog
