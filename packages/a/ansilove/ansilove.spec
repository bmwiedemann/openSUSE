#
# spec file for package ansilove
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020, Martin Hauke <mardnh@gmx.de>
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


Name:           ansilove
Version:        4.1.4
Release:        0
Summary:        ANSI and ASCII art to PNG converter
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://www.ansilove.org
#Git-Clone:     https://github.com/ansilove/ansilove.git
Source:         https://github.com/ansilove/ansilove/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libansilove-devel

%description
AnsiLove/C is a tool to convert ANSI and artscene-related file formats into
PNG images.

The following formats are supported:
 - .ANS - ANSi (ANSI escape sequences: ANSI X3.64 standard)
 - .PCB - PCBoard Bulletin Board System (BBS) own file format
 - .BIN - Binary format (raw memory copy of text mode video memory)
 - .ADF - Artworx format, supporting custom character sets and palettes
 - .IDF - iCE Draw format, supporting custom character sets and palettes
 - .TND - TundraDraw format, supporting 24-bit color mode
 - .XB  - The eXtended Binary XBin format, supporting custom character
          sets and palettes

%prep
%setup -q
find examples/ -type f -name "*.ans" -exec sed -i 's/\r$//' {} +

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%doc examples/
%{_bindir}/ansilove
%{_mandir}/man1/ansilove.1%{?ext_man}

%changelog
