#
# spec file for package python-hdf5storage
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


Name:           python-hdf5storage
Version:        0.1.19
Release:        0
Summary:        Utilities to read/write HDF5 files, including MATLAB v7.3 MAT files
License:        BSD-3-Clause
URL:            https://github.com/frejanordsiek/hdf5storage
Source:         https://files.pythonhosted.org/packages/source/h/hdf5storage/hdf5storage-%{version}.tar.gz
# PATCH-FIX-UPSTREAM nose-to-pytest.patch gh#frejanordsiek/hdf5storage#96 mcepl@suse.com
# uses pytest instead of nose
Patch0:         nose-to-pytest.patch
BuildRequires:  %{python_module h5py >= 3.3}
BuildRequires:  %{python_module numpy < 2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.0}
# I don't know how to do @pytest.mark.parametrize on class methods
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires:       python-h5py >= 3.3
Requires:       python-numpy < 2
Recommends:     python-scipy
# This pure python package uses ctypes only suited for 64-bit. The tests segfault on 32-bit in libc memmove
# gh#frejanordsiek/hdf5storage#109
ExcludeArch:    %ix86 %arm
%python_subpackages

%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%prep
%autosetup -p1 -n hdf5storage-%{version}
# fix end-of-line encoding
sed -i 's/\r$//' COPYING.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/hdf5storage/
%{python_sitelib}/hdf5storage-%{version}-py*.egg-info

%changelog
