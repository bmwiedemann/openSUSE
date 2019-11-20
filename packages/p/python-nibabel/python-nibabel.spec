#
# spec file for package python-nibabel
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
Name:           python-nibabel
Version:        2.5.1
Release:        0
Summary:        Tool to access multiple neuroimaging data formats
License:        MIT
URL:            https://nipy.org/nibabel
Source:         https://files.pythonhosted.org/packages/source/n/nibabel/nibabel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.8
Requires:       python-six >= 1.3
Recommends:     python-dicom >= 0.9.9
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose >= 0.10.1}
BuildRequires:  %{python_module numpy >= 1.8}
BuildRequires:  %{python_module six >= 1.3}
BuildRequires:  python-bz2file
# /SECTION
%ifpython2
Requires:       python-bz2file
%endif
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
%python_expand nosetests-%{$python_bin_suffix} nibabel

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
