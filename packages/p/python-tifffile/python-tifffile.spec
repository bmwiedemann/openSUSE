#
# spec file for package python-tifffile
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


%define packagename tifffile
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tifffile
Version:        2021.1.14
Release:        0
Summary:        Read and write TIFF(r) files
License:        BSD-2-Clause
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/tifffile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module imagecodecs >= 2020.5.30}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib >= 3.2}
BuildRequires:  %{python_module numpy >= 1.15.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zarr >= 2.5.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-imagecodecs >= 2020.5.30
Requires:       python-lxml
Requires:       python-matplotlib >= 3.2
Requires:       python-numpy >= 1.15.1
Requires:       python-zarr >= 2.5.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Read and write TIFF(r) files. Read image and metadata from many
bio-scientific formats such as plain TIFF, BigTIFF, OME-TIFF, STK, LSM,
SGI, NIH, ImageJ, MicroManager, MD GEL, and FluoView files. Write numpy
arrays to TIFF, BigTIFF, and ImageJ hyperstack compatible files.

%prep
%setup -q -n %{packagename}-%{version}
# Fix warning wrong-file-end-of-line-encoding
sed -i 's/\r//' README.rst

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/%{packagename}
%python_clone -a %{buildroot}%{_bindir}/lsm2bin
%python_clone -a %{buildroot}%{_bindir}/tiffcomment

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}
%prepare_alternative lsm2bin
%prepare_alternative tiffcomment

%post
%python_install_alternative %{packagename}
%python_install_alternative lsm2bin
%python_install_alternative tiffcomment

%postun
%python_uninstall_alternative %{packagename}
%python_uninstall_alternative lsm2bin
%python_uninstall_alternative tiffcomment

%check
# skip online tests and tests that OOM
%pytest -k 'not (test_issue_infinite_loop or test_func_pformat_xml or test_filehandle_seekable or test_write_compress_lerc or test_write_imagej_raw or test_write_bigtiff or test_write_ome or test_class_omexml_attributes or test_class_omexml_multiimage or test_class_omexml or test_write_compression_lerc)'

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/tifffile
%python_alternative %{_bindir}/lsm2bin
%python_alternative %{_bindir}/tiffcomment
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
