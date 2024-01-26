#
# spec file for package python-pydicom
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


%{?sle15_python_module_pythons}
Name:           python-pydicom
Version:        2.4.4
Release:        0
Summary:        Pure python package for DICOM medical file reading and writing
License:        MIT
URL:            https://github.com/darcymason/pydicom
Source:         https://github.com/pydicom/pydicom/archive/refs/tags/v%{version}.tar.gz#/pydicom-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM pydicom-pr1908-fixpillow.patch gh#pydicom/pydicom#1908 fixes gh#pydicom/pydicom#1907
Patch0:         pydicom-pr1908-fixpillow.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pydicom-data}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
%if 0%{?suse_version} > 1550
# GDCM is not multiflavor in Tumbleweed
BuildRequires:  python3-gdcm
%endif
# /SECTION
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
pydicom is a pure python package for parsing DICOM files
into natural pythonic structures for further manipulation.
Modified datasets can be written again to DICOM format files.

DICOM is a standard (http://medical.nema.org) for communicating
medical images and related information such as reports
and radiotherapy objects.

%prep
%autosetup -p1 -n pydicom-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pydicom
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

%{python_expand # see https://github.com/pydicom/pydicom/issues/1697
mkdir build/locallib
cp -r %{$python_sitelib}/data_store %{$python_sitelib}/pydicom_data*.dist-info build/locallib/
}
export PYTHONPATH=$PWD/build/locallib
# these assume that a cache is updatable from online downloads
skips="test_fetch_data_files"
skips="$skips or test_get_testdata_file_external_hash_mismatch"
skips="$skips or test_get_testdata_files_local_external_and_cache"
skips="$skips or test_get_testdata_files_hash_match"
skips="$skips or test_get_testdata_files_hash_mismatch"
skips="$skips or test_get_testdata_files_external_ignore_hash"

if [ "$RPM_ARCH" = "ppc64le" -o "$RPM_ARCH" = "aarch64" ]; then
  skips="$skips or TestPillowHandler_JPEG2K"
fi
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # Failures on i586
  skips="$skips or test_write_file_id or test_file_id or test_encapsulate_bot_large_raises or (TestPillowHandler_JPEG2K and test_array)"
fi

%pytest -rsfR $ignores -k "not ($skips)"

%post
%python_install_alternative pydicom

%postun
%python_uninstall_alternative pydicom

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pydicom
%{python_sitelib}/pydicom
%{python_sitelib}/pydicom-%{version}.dist-info

%changelog
