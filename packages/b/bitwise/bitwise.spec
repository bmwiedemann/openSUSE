#
# spec file for package bitwise
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           bitwise
Version:        0.42
Release:        0
Summary:        Interactive bitwise operation in ncurses
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/mellowcandle/bitwise
Source:         https://github.com/mellowcandle/bitwise/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(readline)

%description
Bitwise is a multi base interactive calculator supporting dynamic base
conversion and bit manipulation. It's a handy tool for low level
hackers, kernel developers and device drivers developers.

Some of the features include:
 * Interactive ncurses interface command line calculator.
 * Individual bit manipulator.
 * Bitwise operations such as NOT, OR, AND, XOR, and shifts.

%prep
%setup -q

%build
autoreconf -fiv
export CFLAGS="%{optflags} $(pkg-config --cflags --libs ncursesw)"
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README README.md
%{_bindir}/bitwise
%{_mandir}/man1/bitwise.1%{?ext_man}

%changelog
