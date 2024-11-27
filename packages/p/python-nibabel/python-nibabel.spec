#
# spec file for package python-nibabel
#
# Copyright (c) 2024 SUSE LLC
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


%define binaries nib-conform nib-convert nib-dicomfs nib-diff nib-ls nib-nifti-dx nib-roi nib-stats nib-tck2trk nib-trk2tck parrec2nii
Name:           python-nibabel
Version:        5.3.2
Release:        0
Summary:        Tool to access multiple neuroimaging data formats
License:        MIT
URL:            https://nipy.org/nibabel
# SourceRepository: https://github.com/nipy/nibabel
Source:         https://files.pythonhosted.org/packages/source/n/nibabel/nibabel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.20
Requires:       python-packaging => 17
%if 0%{?python_version_nodots} < 312
Requires:       python-importlib-resources >= 5.12
%endif
%if 0%{?python_version_nodots} < 313
Requires:       python-typing-extensions >= 4.6
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-h5py
Recommends:     python-pydicom >= 1
Recommends:     python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module importlib-resources >= 5.12 if %python-base < 3.12}
BuildRequires:  %{python_module numpy >= 1.20}
BuildRequires:  %{python_module packaging >= 17}
BuildRequires:  %{python_module pydicom >= 1}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module typing-extensions >= 4.6 if %python-base < 3.13}
BuildRequires:  %{pythons}
BuildRequires:  git-core
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
%autosetup -p1 -n nibabel-%{version}
find nibabel -name .gitignore -delete
sed -i '1{/^!#/d}' nibabel/cmdline/*.py
chmod a-x nibabel/cmdline/*.py
chmod a-x nibabel/tests/data/umass_anonymized.PAR nibabel/gifti/tests/data/gzipbase64.gii nibabel/nicom/dicomwrappers.py nibabel/nicom/tests/test_dicomwrappers.py

%build
%pyproject_wheel

%install
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -n auto -rsfE

%post
%{expand:%(for b in %{binaries}; do echo "%%python_install_alternative $b"; done)}

%postun
%{expand:%(for b in %{binaries}; do echo "%%python_uninstall_alternative $b"; done)}

%files %{python_files}
%doc AUTHOR Changelog README.rst
%license COPYING
%{expand:%(for b in %{binaries}; do echo "%%python_alternative %%{_bindir}/$b"; done)}
%{python_sitelib}/nibabel
%{python_sitelib}/nibabel-%{version}.dist-info

%changelog
