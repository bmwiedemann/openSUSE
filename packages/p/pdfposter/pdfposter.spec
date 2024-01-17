#
# spec file for package pdfposter
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


Name:           pdfposter
Version:        0.8.1
Release:        0
Summary:        Scale and tile PDF images/pages to print on multiple pages
License:        GPL-3.0-or-later
URL:            https://pdfposter.readthedocs.io/
Source:         https://gitlab.com/pdftools/pdfposter/-/archive/v%{version}/pdfposter-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyPDF2 >= 2.1.1
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pytest
BuildRequires:  python3-reportlab
BuildRequires:  python3-setuptools
Requires:       python3-PyPDF2 >= 2.1.1
Requires:       python3-base >= 3.6
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
%setup -q -n pdfposter-v%{version}

%build
%python3_build
pushd docs
PYTHONPATH=.. make html
rm _build/html/.buildinfo
popd

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 test/gen-chessboard.py test/chessboard.pdf
PYTHONPATH=. pytest -vv test/unit test/functional

%files
%{python3_sitelib}/pdftools/
%{python3_sitelib}/pdftools.pdfposter-%{version}*-info
%{python3_sitelib}/pdftools.pdfposter-%{version}*-nspkg.pth
%{_bindir}/pdfposter

%files doc
%doc examples docs/_build/html/

%changelog
