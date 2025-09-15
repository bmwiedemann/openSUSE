#
# spec file for package ttyplot
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2023-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           ttyplot
Version:        1.7.4
Release:        0
Summary:        Realtime plotting utility for terminals
License:        Apache-2.0
URL:            https://github.com/tenox7/ttyplot
Source:         https://github.com/tenox7/ttyplot/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

%description
A realtime plotting utility for terminals. It takes data from stdin, and
plots on a terminal or console.
It supports rate calculation for counters, and up to two plots on a single
display using reverse video for the second line.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags} $(pkg-config --cflags --libs ncursesw)"

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANPREFIX=%{_mandir}

%files
%license LICENSE
%doc README.md
%{_bindir}/ttyplot
%{_mandir}/man1/ttyplot.1%{?ext_man}

%changelog
