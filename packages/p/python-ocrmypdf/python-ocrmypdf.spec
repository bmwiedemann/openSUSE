#
# spec file for package python-ocrmypdf
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-ocrmypdf
Version:        17.4.2
Release:        0
Summary:        OCRmyPDF adds an OCR text layer to scanned PDF files
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ocrmypdf/OCRmyPDF
#Source:         https://files.pythonhosted.org/packages/source/o/ocrmypdf/ocrmypdf-%%{version}.tar.gz
Source:         OCRmyPDF-%{version}.tar.xz
BuildRequires:  %{python_module Pillow >= 10.0.1}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module deprecation >= 2.1.0}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module img2pdf >= 0.5}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pdfminer.six >= 20220319}
BuildRequires:  %{python_module pikepdf >= 10.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pluggy >= 1}
BuildRequires:  %{python_module rich >= 13}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module setuptools_scm >= 7.0.5}
BuildRequires:  %{python_module typing_extensions >= 4.15.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# upstream use Requires:  ghostscript >= 10.01.2
Requires:       ghostscript >= 9.55
Requires:       python-Pillow >= 10.0.1
Requires:       python-deprecation >= 2.1.0
Requires:       python-fpdf2 >= 2.8.0
Requires:       python-img2pdf >= 0.5
Requires:       python-packaging >= 20
Requires:       python-pdfminer.six >= 20220319
Requires:       python-pikepdf >= 10.0.0
Requires:       python-pluggy >= 1
Requires:       python-pydantic >= 2.11.9
Requires:       python-reportlab >= 3.6.8
Requires:       python-rich >= 13
Requires:       python-typing_extensions >= 4.15.0
Requires:       python-uharfbuzz >= 0.53.2
Requires:       tesseract-ocr >= 5.4.1
Requires:       tesseract-ocr-traineddata-deu >= 4.1.0
Requires:       tesseract-ocr-traineddata-eng >= 4.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-Flask >= 2.0.1
Suggests:       python-PyMuPDF >= 1.19.1
Suggests:       python-python-dotenv
Suggests:       python-sphinx
Suggests:       python-sphinx-issues
Suggests:       python-sphinx-rtd-theme
Suggests:       python-typer
Suggests:       python-watchdog >= 1.0.2
Provides:       OCRmyPDF = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 6.2}
BuildRequires:  %{python_module fpdf2 >= 2.8.0}
BuildRequires:  %{python_module hypothesis >= 6.36.0}
# upstrema use python-pydantic >= 2.12.5
BuildRequires:  %{python_module pydantic >= 2.11.9}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-cov >= 3.0.0}
BuildRequires:  %{python_module pytest-xdist >= 2.5.0}
# upstream use: BuildRequires:  %%{python_module python-xmp-toolkit == 2.0.1}
BuildRequires:  %{python_module python-xmp-toolkit >= 2.0.1}
BuildRequires:  %{python_module reportlab >= 3.6.8}
BuildRequires:  %{python_module types-Pillow if %python-Pillow < 10.3.0}
BuildRequires:  %{python_module types-humanfriendly}
BuildRequires:  %{python_module uharfbuzz >= 0.53.2}
# upstream use BuildRequires:  ghostscript >= 10.02.1
BuildRequires:  ghostscript >= 9.55
BuildRequires:  tesseract-ocr >= 5.4.1
BuildRequires:  tesseract-ocr-traineddata-eng >= 4.1.0
# /SECTION
%python_subpackages

%description
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched

%prep
%autosetup -p1 -n OCRmyPDF-%{version}
# rpmlintrc
# Cleanup shebang and executable bits.
sed -i -e '1{\@^#!%{_bindir}/env python@d}' src/ocrmypdf/*.py src/ocrmypdf/*/*.py

%build
%pyproject_wheel

%install
%pyproject_install

# Fix python-bytecode-inconsistent-mtime
%python_compileall

%python_clone -a %{buildroot}%{_bindir}/ocrmypdf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_acroform_and_redo"
donttest+=" or test_blank_input_pdf"
donttest+=" or test_decompression_bomb_error"
donttest+=" or test_force_ocr"
donttest+=" or test_graft"
donttest+=" or test_image_input"
donttest+=" or test_input_file_not_found"
donttest+=" or test_input_file_not_readable"
donttest+=" or test_invalid_input_pdf"
donttest+=" or test_jbig2_passthrough"
donttest+=" or test_maximum_options"
donttest+=" or test_ocr_timeout"
donttest+=" or test_oversample"
donttest+=" or test_pagesegmode"
donttest+=" or test_pagesize_consistency"
donttest+=" or test_pdfa"
donttest+=" or test_quick"
donttest+=" or test_redo_ocr"
donttest+=" or test_repeat_ocr"
donttest+=" or test_rotate_deskew_ocr_timeout"
donttest+=" or test_sidecar_nonempty"
donttest+=" or test_sidecar_pagecount"
donttest+=" or test_skip_big"
donttest+=" or test_skip_ocr"
donttest+=" or test_tesseract_config_valid"
donttest+=" or test_tesseract_crash_autorotate"
donttest+=" or test_tesseract_crash"
donttest+=" or test_tesseract_oem"
donttest+=" or test_tesseract_thresholding"
donttest+=" or test_user_words_ocr"
donttest+=" or test_very_high_dpi"
donttest+=" or test_rotate_and_crop"
donttest+=" or test_rotated_skew_timeout"
donttest+=" or test_rasterize_rotates"
donttest+=" or test_rotate_interaction"
%pytest -k "not ($donttest)"

%post
%python_install_alternative ocrmypdf

%postun
%python_uninstall_alternative ocrmypdf

%files %{python_files}
%doc README.md
%license LICENSE LICENSES
%{python_sitelib}/ocrmypdf
%{python_sitelib}/ocrmypdf-%{version}.dist-info
%python_alternative %{_bindir}/ocrmypdf

%changelog
