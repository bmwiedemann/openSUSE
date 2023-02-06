#
# spec file for package python-pytesseract
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


Name:           python-pytesseract
Version:        0.3.10
Release:        0
Summary:        Python wrapper for Google's Tesseract-OCR
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/madmaze/python-tesseract
# https://github.com/madmaze/pytesseract/issues/262
Source:         https://github.com/madmaze/pytesseract/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-setuptools
Requires:       tesseract-ocr-traineddata-deu
Requires:       tesseract-ocr-traineddata-eng
Requires:       pkgconfig(tesseract)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest}
BuildRequires:  tesseract-ocr-traineddata-deu
BuildRequires:  tesseract-ocr-traineddata-eng
BuildRequires:  tesseract-ocr-traineddata-fra
BuildRequires:  tesseract-ocr-traineddata-orientation_and_script_detection
BuildRequires:  pkgconfig(tesseract)
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Python-tesseract is an optical character recognition (OCR) tool for Python,
that is, it will recognize and "read" the text embedded in images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine. It can be used
as a stand-alone invocation script to tesseract, as it can read all image types
supported by the Python Imaging Library, including JPEG, PNG, GIF, BMP, TIFF,
and others, whereas tesseract-ocr, by default, only supports TIFF and BMP.
Additionally, if used as a script, python-tesseract will print the recognized
text instead of writing it to a file. There is no support for confidence estimates and
bounding box data is planned for future releases.

%prep
%setup -q -n pytesseract-%{version}
sed -i -e '/^#!\//, 1d' pytesseract/pytesseract.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pytesseract
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export TESSDATA_PREFIX=%{_datadir}/tessdata/
%pytest

%post
%python_install_alternative pytesseract

%postun
%python_uninstall_alternative pytesseract

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pytesseract
%{python_sitelib}/pytesseract
%{python_sitelib}/pytesseract-%{version}*-info

%changelog
