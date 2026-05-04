#
# spec file for package pdfposter
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


%define pythons python3
Name:           pdfposter
Version:        0.9.1
Release:        0
Summary:        Scale and tile PDF images/pages to print on multiple pages
License:        GPL-3.0-or-later
URL:            https://pdfposter.readthedocs.io/
Source:         https://gitlab.com/pdftools/pdfposter/-/archive/v%{version}/pdfposter-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pip
BuildRequires:  python3-pypdf >= 5.5
BuildRequires:  python3-pytest
BuildRequires:  python3-reportlab
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-base >= 3.8
Requires:       python3-pypdf >= 5.5
BuildArch:      noarch

%package doc
Summary:        Documentation files for %{name}

%description
Create a large poster by building it from
multiple pages and/or printing it on large media. It expects as input a
PDF file, normally printing on a single page. The output is again a
PDF file, maybe containing multiple pages together building the
poster.
The input page will be scaled to obtain the desired size.

This is much like 'poster' does for Postscript files, but working
with PDF.

For more information please refer to the manpage or visit
the project homepage https://pdfposter.readthedocs.io/

%description doc
HTML Documentation and examples for %{name}.

%prep
%autosetup -p1 -n pdfposter-v%{version}
sed -i '1{/\/usr\/bin/d;}' pdfposter/__init__.py pdfposter/cmd.py

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 test/gen-chessboard.py test/chessboard.pdf
PYTHONPATH=. pytest -vv test/unit test/functional

%files
%{python3_sitelib}/pdfposter
%{python3_sitelib}/pdfposter-%{version}*-info
%{_bindir}/pdfposter

%files doc
%doc examples docs

%changelog
