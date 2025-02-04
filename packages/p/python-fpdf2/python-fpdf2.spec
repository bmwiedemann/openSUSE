#
# spec file for package python-fpdf2
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-fpdf2
Version:        2.8.2
Release:        0
Summary:        Simple & fast PDF generation for Python
License:        LGPL-3.0-or-later
URL:            https://py-pdf.github.io/fpdf2/
# The _service download the source and repack without some ttf files
# that has non-commercial license. boo#1232452
Source:         fpdf2-%{version}.tar.xz
BuildRequires:  %{python_module Pillow >= 6.2.2}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module fonttools >= 4.34.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module camelot-py}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module endesive}
BuildRequires:  %{python_module ghostscript}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module opencv}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module qrcode}
BuildRequires:  %{python_module tabula-py}
BuildRequires:  %{python_module uharfbuzz}
BuildRequires:  java
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pillow >= 6.2.2
Requires:       python-defusedxml
Requires:       python-fonttools >= 4.34.0
BuildArch:      noarch
%python_subpackages

%description
Simple & fast PDF generation for Python.

%prep
%autosetup -p1 -n fpdf2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_png_url or test_bidi_conformance or test_bidi_character or test_page_background or test_insert_jpg_jpxdecode"
# Requires non-commercial licensed file SBL_Hbrw.ttf
donttest+=" or test_bidi_paragraph_direction or test_hebrew_diacritics or test_text_with_parentheses"
%pytest -s -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fpdf
%{python_sitelib}/fpdf2-%{version}.dist-info

%changelog
