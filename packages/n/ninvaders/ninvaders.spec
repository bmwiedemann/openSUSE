#
# spec file for package ninvaders
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


Name:           ninvaders
Version:        0.1.2
Release:        0
Summary:        A space invaders-like game using ncurses
License:        GPL-2.0-or-later
URL:            https://dettus.net/ninvaders/
Source:         https://dettus.net/ninvaders/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM ninvaders-obey-cflags.patch -- don't clear pre-set CFLAGS
Patch0:         ninvaders-obey-cflags.patch
# PATCH-FIX-UPSTREAM ninvaders-sighandler_t.patch -- fix gcc15 build
Patch1:         ninvaders-sighandler_t.patch
# PATCH-FIX-UPSTREAM ninvaders-fix-doSleep-decl.patch -- fix gcc15 build
Patch2:         ninvaders-fix-doSleep-decl.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(ticw)
BuildRequires:  pkgconfig(tinfo)

%description
A Space Invaders type game with text-only graphics.

%prep
%autosetup -p1

%build
%make_build

%install
install -Dm 0755 nInvaders %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog README
%license gpl.txt
%{_bindir}/%{name}

%changelog
