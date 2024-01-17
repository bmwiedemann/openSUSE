#
# spec file for package python-pydicom
#
# Copyright (c) 2022 SUSE LLC
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
%define         oldpython python
Name:           python-pydicom
Version:        2.3.1
Release:        0
Summary:        Pure python package for DICOM medical file reading and writing
License:        MIT
URL:            https://github.com/darcymason/pydicom
Source:         https://files.pythonhosted.org/packages/source/p/pydicom/pydicom-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pydicom-data}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  python3-gdcm
# /SECTION
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-dicom < %{version}
Provides:       %{oldpython}-dicom = %{version}
%endif
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
%setup -q -n pydicom-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pydicom
%python_expand rm -r %{buildroot}%{$python_sitelib}/pydicom/{benchmarks,tests,data/test_files}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

skips="test_fetch_data_files"
# see https://github.com/pydicom/pydicom-data/issues/9
skips="$skips or OBXXXX1A or (test_can_access_unsupported_dataset and (TestPillowHandler_JPEG or TestPillowHandler_JPEG2K))"

# Failures only on ppc64
skips="$skips or test_invalid_arr_dtype_raises or TestHandlerGenerateMultiplex or TestHandlerMultiplexArray"
# Failures only on i586
skips="$skips or test_write_file_id or test_file_id or test_encapsulate_bot_large_raises or (TestPillowHandler_JPEG2K and test_array)"

# see https://github.com/pydicom/pydicom/issues/1697
ignores="--ignore pydicom/tests/test_dataset.py --ignore pydicom/tests/test_data_manager.py"

%pytest -rs pydicom/tests $ignores -k "not ($skips)"

%post
%python_install_alternative pydicom

%postun
%python_uninstall_alternative pydicom

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pydicom
%{python_sitelib}/pydicom*

%changelog
