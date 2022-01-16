#
# spec file for package python-PyMuPDF
#
# Copyright (c) 2021 SUSE LLC
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
# Python 3 only syntax
%define skip_python2 1
%define pypi_name PyMuPDF
Name:           python-%{pypi_name}
Version:        1.19.4
Release:        0
Summary:        Python binding for MuPDF, a PDF and XPS viewer
License:        AGPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://github.com/pymupdf/PyMuPDF
Source:         https://files.pythonhosted.org/packages/source/P/PyMuPDF/PyMuPDF-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jbig2dec-devel
BuildRequires:  mupdf-devel-static < 1.20.0
BuildRequires:  mupdf-devel-static >= 1.19.0
BuildRequires:  openSUSE-release
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(zlib)
%python_subpackages

%description
This is PyMuPDF, a Python binding for MuPDF, a PDF and XPS viewer.
MuPDF can access files in PDF, XPS, OpenXPS, epub, comic and fiction
book formats. PyMuPDF can also access files with extensions *.pdf,
*.xps, *.oxps, *.epub, *.cbz or *.fb2 from Python scripts.

%prep
%setup -q -n %{pypi_name}-%{version}
dos2unix README.md changes.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# https://github.com/pymupdf/PyMuPDF/issues/1002 requests a better test sequence
cd /tmp
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c 'import fitz'

%files %{python_files}
%license COPYING
%doc README.md changes.txt
%{python_sitearch}/*

%changelog
