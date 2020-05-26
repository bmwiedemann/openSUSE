#
# spec file for package python-img2pdf
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-img2pdf
Version:        0.3.4
Release:        0
Summary:        Python module for converting images to PDF via direct JPEG inclusion
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://gitlab.mister-muffin.de/josch/img2pdf
Source:         https://files.pythonhosted.org/packages/source/i/img2pdf/img2pdf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-pdfrw
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-pdfrw
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pdfrw}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This module losslessly converts raster images to PDF. The file size
will not unnecessarily increase. It can, for example, be used to
create a PDF document from a number of scans that are only available
in JPEG format. Existing solutions would either re-encode the input
JPEG files (leading to quality loss) or store them in the Deflate
format which results in the PDF becoming unnecessarily large in terms
of file size.

%prep
%setup -q -n img2pdf-%{version}
sed -i -e '/^#!\//, 1d' src/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/img2pdf-gui
%python_clone -a %{buildroot}%{_bindir}/img2pdf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative img2pdf-gui
%python_install_alternative img2pdf

%postun
%python_uninstall_alternative img2pdf-gui
%python_uninstall_alternative img2pdf

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.md
%python_alternative %{_bindir}/img2pdf
%python_alternative %{_bindir}/img2pdf-gui
%{python_sitelib}/*

%changelog
