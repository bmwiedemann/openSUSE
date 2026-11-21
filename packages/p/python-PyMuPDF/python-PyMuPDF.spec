#
# spec file for package python-PyMuPDF
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


%define mupdf_version 1.28.6
%{?sle15_python_module_pythons}
%bcond_without libalternatives
Name:           python-PyMuPDF
Version:        2.1
Release:        0
Summary:        Python binding for MuPDF, a PDF and XPS viewer
License:        AGPL-3.0-only
URL:            https://github.com/pymupdf/PyMuPDF
Source:         https://files.pythonhosted.org/packages/source/P/PyMuPDF/pymupdf-%{version}.tar.gz
Source1:        https://mupdf.com/downloads/archive/mupdf-%{mupdf_version}-source.tar.gz
BuildRequires:  %{python_module devel >= 3.11}
BuildRequires:  %{python_module pipcl}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  clang19-devel
%if 0%{?suse_version} >= 1699
BuildRequires:  llvm21-libclang13
%endif
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jbig2dec-devel
BuildRequires:  openSUSE-release
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-clang19
BuildRequires:  swig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(zlib)
Requires:       alts
Provides:       bundled(mupdf) = %version
# mupdf has bundled() on its own, too, so kinda bad
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  codespell
# /SECTION
%python_subpackages

%description
This is PyMuPDF, a Python binding for MuPDF, a PDF and XPS viewer.
MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats. PyMuPDF can also access files with extensions *.pdf,
*.xps, *.oxps, *.epub, *.cbz or *.fb2 from Python scripts.

%package devel
Summary:        Python binding for MuPDF
Requires:       %{name} = %{version}

%description devel
Devel package for %{name}.

%prep
%autosetup -p1 -n pymupdf-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags} -ffat-lto-objects -frandom-seed=%{version} -I/usr/include/freetype2 -DNDEBUG"
export ARCHFLAGS="%{optflags}"
# -D makes .a files deterministic
export AR="ar -D"
# Otherwise, it tries to install pipcl directly
export PYTHONPATH=%{python3_sitelib}
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pymupdf
%python_clone -a %{buildroot}%{_bindir}/pymupdf-config
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYMUPDF_TEST_USE_4LLM=0
export PYMUPDF_SYSINSTALL_ROOT='-'
# Expects to run in a git checkout
donttest="test_codespell or test_release_bug_template or test_open2"
# Assumes ubuntu, like GitHub Actions
donttest+=" or test_subset_fonts or test_spikes"
# No python-pymupdf-fonts
donttest+=" or test_fontarchive"
# No pymupdf4llm
donttest+=" or test_configuration_layout"
# Non-deterministic failures
donttest+=" or test_4125"
# Requires network
donttest+=" or test_5082 or test_4702 or test_4533 or test_4457"
donttest+=" or test_4445 or test_2791"
# Fails on 32 bit
if [ $(getconf LONG_BIT) -eq 32 ]; then
    donttest+=" or test_2246 or test_4415 or test_4435 or test_4245"
fi
# test_tables.py expects results from the ONNX-backed pymupdf_layout engine
%pytest_arch --ignore tests/test_tables.py -k "not ($donttest)"

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/[Pp]y[Mm]u[Pp][Dd][Ff]_lite-%{version}.dist-info
%{python_sitearch}/fitz/
%{python_sitearch}/pymupdf/
%python_alternative %{_bindir}/pymupdf
%python_alternative %{_bindir}/pymupdf-config
%exclude %{python_sitearch}/pymupdf/mupdf-devel/

%files %{python_files devel}
%{python_sitearch}/pymupdf/mupdf-devel/

%changelog
