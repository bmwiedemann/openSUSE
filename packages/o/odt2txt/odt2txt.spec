#
# spec file for package odt2txt
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


Name:           odt2txt
Version:        0.5
Release:        0
Summary:        Converter from OpenDocument Text to plain text
License:        GPL-2.0-only
URL:            https://github.com/dstosberg
Source:         https://github.com/dstosberg/odt2txt/archive/v%{version}.tar.gz
BuildRequires:  zlib-devel

%description
odt2txt is a command-line tool which extracts the text out
of OpenDocument Texts produced by OpenOffice.org, StarOffice,
KOffice and others.

odt2txt can also extract text from some file formats similar
to OpenDocument Text, such as OpenOffice.org XML (*.sxw),
which was used by OpenOffice.org version 1.x and older StarOffice
versions. To a lesser extend, odt2txt may be useful to extract
content from OpenDocument spreadsheets (*.ods) and OpenDocument
presentations (*.odp).

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} install
chmod 644 %{buildroot}%{_mandir}/man1/odt2txt.1

%files
%license GPL-2
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/odt2txt.1%{?ext_man}

%changelog
