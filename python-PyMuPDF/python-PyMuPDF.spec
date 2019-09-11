#
# spec file for package python-PyMuPDF
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
# Upstream doesn't support Python 2 anymore.
%define skip_python2 1
%define pypi_name PyMuPDF
Name:           python-%{pypi_name}
Version:        1.16.1
Release:        0
Summary:        Python binding for MuPDF, a PDF and XPS viewer
License:        GPL-3.0-only AND AGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rk700/PyMuPDF
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch1:         fix-library-linking.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  jbig2dec-devel
BuildRequires:  mupdf-devel-static >= 1.16.0
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(freetype2)
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

%package -n     python-%{pypi_name}-doc
Summary:        Documentation for PyMuPDF
Group:          Development/Languages/Python

%description -n python-%{pypi_name}-doc
This is the documentation for PyMuPDF.

%prep
%setup -q -n %{pypi_name}-%{version}
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# no upstream tests

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/*

%files -n python-%{pypi_name}-doc
%doc doc/PyMuPDF.pdf

%changelog
