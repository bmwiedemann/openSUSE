#
# spec file for package python-tifffile
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


Name:           python-tifffile
Version:        2022.10.10
Release:        0
Summary:        Read and write TIFF(r) files
License:        BSD-2-Clause
URL:            https://github.com/cgohlke/tifffile/
Source:         https://github.com/cgohlke/tifffile/archive/v%{version}.tar.gz#/tifffile-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module numpy >= 1.19.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-fsspec
Recommends:     python-imagecodecs >= 2022.2.22
Recommends:     python-lxml
Recommends:     python-matplotlib >= 3.3
Recommends:     python-zarr
# SECTION test
BuildRequires:  %{python_module imagecodecs >= 2022.2.22}
BuildRequires:  %{python_module cmapfile}
BuildRequires:  %{python_module czifile}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module lfdfiles}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib >= 3.3}
BuildRequires:  %{python_module oiffile}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module roifile}
BuildRequires:  %{python_module xarray}
BuildRequires:  %{python_module zarr}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Read and write TIFF(r) files. Read image and metadata from many
bio-scientific formats such as plain TIFF, BigTIFF, OME-TIFF, STK, LSM,
SGI, NIH, ImageJ, MicroManager, MD GEL, and FluoView files. Write numpy
arrays to TIFF, BigTIFF, and ImageJ hyperstack compatible files.

%prep
%setup -q -n tifffile-%{version}
# Fix warning wrong-file-end-of-line-encoding
sed -i 's/\r//' README.rst
sed -i '1{/env python/d}' tifffile/{lsm2bin,tiff2fsspec,tiffcomment}.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tifffile
%python_clone -a %{buildroot}%{_bindir}/lsm2bin
%python_clone -a %{buildroot}%{_bindir}/tiffcomment
%python_clone -a %{buildroot}%{_bindir}/tiff2fsspec

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative tifffile
%prepare_alternative lsm2bin
%prepare_alternative tiffcomment

%post
%python_install_alternative tifffile
%python_install_alternative lsm2bin
%python_install_alternative tiffcomment
%python_install_alternative tiff2fsspec

%postun
%python_uninstall_alternative tifffile
%python_uninstall_alternative lsm2bin
%python_uninstall_alternative tiffcomment
%python_uninstall_alternative tiff2fsspec

%check
# Crashes Out-Of-Memory
donttest="test_write_ome"
donttest="$donttest or test_write_imagej_raw"
donttest="$donttest or test_write_bigtiff"
# can't connect to localhost
donttest="$donttest or test_write_fsspec"
# no lerc support in imagecodecs
donttest="$donttest or test_write_compression_lerc"
# can't connect to external server
donttest="$donttest or test_class_omexml"
%pytest -n auto -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/tifffile
%python_alternative %{_bindir}/lsm2bin
%python_alternative %{_bindir}/tiffcomment
%python_alternative %{_bindir}/tiff2fsspec
%{python_sitelib}/tifffile-%{version}.dist-info/
%{python_sitelib}/tifffile

%changelog
