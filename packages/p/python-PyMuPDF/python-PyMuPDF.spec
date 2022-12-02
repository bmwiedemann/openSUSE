#
# spec file
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
# Python 2 build fails always
%define skip_python2 1
%define pypi_name PyMuPDF
Name:           python-%{pypi_name}
Version:        1.21.0
Release:        0
Summary:        Python binding for MuPDF, a PDF and XPS viewer
License:        AGPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://github.com/pymupdf/PyMuPDF
Source:         https://files.pythonhosted.org/packages/source/P/PyMuPDF/PyMuPDF-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jbig2dec-devel
BuildRequires:  mupdf-devel-static >= 1.20.3
BuildRequires:  openSUSE-release
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
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
%autosetup -p1 -n %{pypi_name}-%{version}

%build
export CFLAGS="%{optflags} -I/usr/include/freetype2"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cd /tmp
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c 'import fitz'

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/PyMuPDF-%{version}*-info
%{python_sitearch}/fitz/

%changelog
