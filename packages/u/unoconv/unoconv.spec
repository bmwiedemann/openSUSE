#
# spec file for package unoconv
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           unoconv
Version:        0.8.2
Release:        0
Summary:        Tool to convert between any document format supported by LibreOffice
License:        GPL-2.0-only
Group:          Productivity/File utilities
URL:            http://dag.wieers.com/home-made/unoconv/
Source:         https://github.com/dagwieers/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       libreoffice-pyuno
Requires:       python3
BuildArch:      noarch

%description
unoconv converts between any document format that LibreOffice understands.
It uses LibreOffice's UNO bindings for non-interactive conversion of
documents.

Supported document formats include: Open Document Text (.odt),
Open Document Draw (.odd), Open Document Presentation (.odp),
Open Document calc (.odc), MS Word (.doc), MS PowerPoint (.pps/.ppt),
MS Excel (.xls), MS Office Open/OOXML (.xml),
Portable Document Format (.pdf), DocBook (.xml), LaTeX (.ltx),
HTML, XHTML, RTF, Docbook (.xml), GIF, PNG, JPG, SVG, BMP, EPS
and many more...

%prep
%setup -q
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' unoconv

%build

%install
%make_install
make DESTDIR=%{buildroot} install-links
rm -v %{buildroot}%{_bindir}/odt2txt

%files
%license COPYING
%doc AUTHORS CHANGELOG.md ChangeLog README.adoc doc/*.adoc
%{_mandir}/man1/unoconv.1%{?ext_man}
%{_bindir}/*

%changelog
