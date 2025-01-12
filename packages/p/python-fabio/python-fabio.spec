#
# spec file for package python-fabio
#
# Copyright (c) 2025 SUSE LLC
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


%define pyversion 2024.9.0
Name:           python-fabio
Version:        2024.9.0
Release:        0
Summary:        Image IO for images produced by 2D X-ray detectors
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT
URL:            https://github.com/silx-kit/fabio
Source:         https://github.com/silx-kit/fabio/archive/v%{version}.tar.gz#/fabio-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module hdf5plugin}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib-qt}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module meson-python >= 0.11}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-h5py
Requires:       python-hdf5plugin
Requires:       python-lxml
Requires:       python-numpy
Recommends:     python-PyQt5
Recommends:     python-matplotlib
Requires(post): update-alternatives
Requires(postun): update-alternatives
# This package does not support 32 bit arch.
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
FabIO is an I/O library for images produced by 2D X-ray detectors.

%prep
%autosetup -n fabio-%{version}
find src -name '*.py' -and ! -path src/fabio/_version.py -exec sed -i '1{/^#!/d}' '{}' ';' -exec chmod -x '{}' ';'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand sed -i '1{s|^#!.*$|#!%{__$python}|}' %{buildroot}%{$python_sitearch}/fabio/version.py
%python_clone -a %{buildroot}%{_bindir}/densify_Bragg
%python_clone -a %{buildroot}%{_bindir}/fabio-convert
%python_clone -a %{buildroot}%{_bindir}/fabio_viewer
%python_clone -a %{buildroot}%{_bindir}/eiger2cbf
%python_clone -a %{buildroot}%{_bindir}/eiger2crysalis
%python_clone -a %{buildroot}%{_bindir}/hdf2neggia
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# the master/slave names have changed, we need to uninstall the old set before installing any new flavor
%pre
%python_uninstall_alternative densify-Bragg

%post
%python_install_alternative fabio-convert fabio_viewer eiger2cbf eiger2crysalis densify_Bragg hdf2neggia

%postun
%python_uninstall_alternative fabio-convert

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python ./run_tests.py --installed -v
}

%files %{python_files}
%doc README.rst
%license copyright
%python_alternative %{_bindir}/hdf2neggia
%python_alternative %{_bindir}/densify_Bragg
%python_alternative %{_bindir}/fabio-convert
%python_alternative %{_bindir}/fabio_viewer
%python_alternative %{_bindir}/eiger2cbf
%python_alternative %{_bindir}/eiger2crysalis
%{python_sitearch}/fabio
%{python_sitearch}/fabio-%{pyversion}.dist-info

%changelog
