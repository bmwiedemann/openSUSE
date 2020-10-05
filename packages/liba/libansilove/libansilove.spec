#
# spec file for package libansilove
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


%global sover   1
%global libname %{name}%{sover}
Name:           libansilove
Version:        1.2.6
Release:        0
Summary:        Library for converting ANSI, ASCII, and other formats to PNG
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            https://www.ansilove.org
#Git-Clone:     https://github.com/ansilove/libansilove.git
Source:         https://github.com/ansilove/libansilove/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdlib)

%description
libansilove is a library to convert ANSi and artscene related file
formats into PNG images.

The following formats are supported:

- .ANS - ANSi (ANSI escape sequences: ANSI X3.64 standard)
- .PCB - PCBoard Bulletin Board System (BBS) own file format
- .BIN - Binary format (raw memory copy of text mode video memory)
- .ADF - Artworx format, supporting custom character sets and palettes
- .IDF - iCE Draw format, supporting custom character sets and palettes
- .TND - TundraDraw format, supporting 24-bit color mode
- .XB - The eXtended Binary XBin format, supporting custom character
        sets and palettes

%package -n %{libname}
Summary:        Library for converting ANSI, ASCII, and other formats to PNG
Group:          Productivity/Graphics/Other

%description -n %{libname}
This library contains shared code regarding the conversion of ANSI and
artscene related file formats into PNG images.

%package devel
Summary:        Library for converting ANSI, ASCII, and other formats to PNG
Group:          Productivity/Graphics/Other
Requires:       %{libname} = %{version}

%description devel
This library contains shared code regarding the conversion of ANSI and
artscene related file formats into PNG images.

This subpackage contains libraries and header files for developing
applications that want to make use of libansilove.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_libdir}/libansilove.so.%{sover}*

%files devel
%{_includedir}/ansilove.h
%{_libdir}/libansilove.so
%{_mandir}/man3/libansilove.3%{?ext_man}
%{_mandir}/man3/ansilove_*.3%{?ext_man}

%changelog
