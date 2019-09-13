#
# spec file for package xbomb
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xbomb
Version:        2.2b
Release:        0
Summary:        Athena-based Minesweeper clone
License:        GPL-2.0+
Group:          Amusements/Games
Url:            http://gedanken.org.uk/software/xbomb/
Source:         http://gedanken.org.uk/software/xbomb/download/%name-%version.tgz
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)

%description
xbomb is a Minesweeper game using the X11 Athena widget set. It can
be played with the traditional square tiling, and also offers
hexagonal and triangle tiling.

%prep
%setup -q 

%build
make %{?_smp_mflags} CFLAGS="%optflags"

%install
b="%buildroot"
mkdir -p "$b/%_bindir" "$b/%_mandir/man6" "$b/%_datadir/X11/app-defaults"
cp -a xbomb "$b/%_bindir/"
cp -a xbomb.6 "$b/%_mandir/man6/"
cp -a xbomb.ad "$b/%_datadir/X11/app-defaults/XBomb"

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%_bindir/xbomb
%_mandir/man6/*
%_datadir/X11/

%changelog
