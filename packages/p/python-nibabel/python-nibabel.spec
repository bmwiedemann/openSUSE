#
# spec file for package python-nibabel
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
Name:           python-nibabel
Version:        3.0.1
Release:        0
Summary:        Tool to access multiple neuroimaging data formats
License:        MIT
URL:            https://nipy.org/nibabel
Source:         https://files.pythonhosted.org/packages/source/n/nibabel/nibabel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.12
Recommends:     python-Pillow
Recommends:     python-dicom >= 0.9.9
Recommends:     python-h5py
Recommends:     python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module nose >= 0.11}
BuildRequires:  %{python_module numpy >= 1.12}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
This package provides read +/- write access to some common medical and
neuroimaging file formats, including: ANALYZE (plain, SPM99, SPM2 and
later), GIFTI, NIfTI1, NIfTI2, CIFTI-2, MINC1, MINC2, AFNI BRIK/HEAD,
MGH and ECAT as well as Philips PAR/REC. We can read and write
FreeSurfer geometry, annotation and morphometry files. There is some
very limited support for DICOM.

%prep
%setup -q -n nibabel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%doc AUTHOR Changelog README.rst
%license COPYING
%python3_only %{_bindir}/nib-dicomfs
%python3_only %{_bindir}/nib-diff
%python3_only %{_bindir}/nib-ls
%python3_only %{_bindir}/nib-nifti-dx
%python3_only %{_bindir}/nib-tck2trk
%python3_only %{_bindir}/nib-trk2tck
%python3_only %{_bindir}/parrec2nii
%{python_sitelib}/*

%changelog
