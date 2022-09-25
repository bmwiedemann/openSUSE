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
Version:        2.3.0
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
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  python3-gdcm
# /SECTION
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-dicom < %{version}
Provides:       %{oldpython}-dicom = %{version}
%endif
Requires(post):   update-alternatives
Requires(postun): update-alternatives
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
# Many test modules and individual tests fail due to test data not included in sdist
# And requires https://github.com/pydicom/pydicom-data , which hasnt been
# packaged yet. c.f. https://github.com/pydicom/pydicom-data/issues/9

skips="test_fetch_data_files or test_reading_ds_with_known_tags_with_UN_VR or test_empty_bot_multi_fragments_per_frame"
skips="$skips or test_convert_rgb_from_implicit_to_explicit_vr or test_empty_bot_too_few_fragments or test_encapsulate"
skips="$skips or test_sequence_with_implicit_vr or test_rgb_ybr_rgb_single_frame or test_rgb_ybr_rgb_multi_frame or test_frame_by_frame"
skips="$skips or test_specific_tags_with_unknown_length_tag or test_tag_with_unknown_length_tag_too_short or test_planar_config"
skips="$skips or test_correct_ambiguous_vr_compressed or test_write_removes_grouplength or test_raw_elements_preserved_explicit_vr"
skips="$skips or test_cycle_u8_1s_1f or test_encoders_gdcm or test_unsupported_syntax_raises or test_can_access_unsupported_dataset"
skips="$skips or TestDatasetOverlayArray or TestGDCM_JPEG_LS_no_gdcm or TestGDCM_JPEG2000_no_gdcm or TestGDCM_JPEGlossy_no_gdcm"
skips="$skips or TestGDCM_JPEGlossless_no_gdcm or TestEncodeFrame or TestEncodeSegment or TestRLEEncodeFrame or TestNumpy_ModalityLUT"
skips="$skips or TestNumpy_PaletteColor or TestNumpy_ApplyWindowing or TestNumpy_ApplyVOI or (TestNumpy_PackBits and test_functional)"
skips="$skips or TestNumpy_NumpyHandler or TestNumpy_GetOverlayArray or TestNumpy_NoRLEHandler or TestNumpy_RLEHandler"
skips="$skips or TestPillowHandler_JPEG2K or TestPillowHandler_JPEG"
# Failures only on ppc64
skips="$skips or test_invalid_arr_dtype_raises or TestHandlerGenerateMultiplex or TestHandlerMultiplexArray"
# Failures only on i586
skips="$skips or test_write_file_id or test_file_id"

# The ignores cause failure during test collection
%{pytest -rs pydicom/tests \
         --ignore pydicom/tests/test_JPEG_LS_transfer_syntax.py \
         --ignore pydicom/tests/test_dataset.py \
         --ignore pydicom/tests/test_gdcm_pixel_data.py \
         --ignore pydicom/tests/test_jpeg_ls_pixel_data.py \
         --ignore pydicom/tests/test_JPEG_LS_transfer_syntax.py \
         --ignore pydicom/tests/test_jpeg_ls_pixel_data.py \
         --ignore pydicom/tests/test_numpy_pixel_data.py \
         -k "not ($skips)"
}

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
