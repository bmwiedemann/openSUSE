#
# spec file for package xer
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           xer
Version:        0.0.5+git20250808
Release:        0
Summary:        Byte stream conversion utility
License:        GPL-3.0-only
URL:            https://github.com/v-p-b/xer
#Git-Clone:     https://github.com/v-p-b/xer.git
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Command line byte encoding swiss army knife.
The goal is to be the iconv of byte stream encodings.

Have you ever spent precious time converting something
like 0xde, 0xad,\r\n0xbe, 0xef to \xde\xad\xbe\xef ?
If so, then xer is for you.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc Changes.md README.md
%{_bindir}/xer

%changelog
