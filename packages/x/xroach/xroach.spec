#
# spec file for package xroach
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xroach
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Version:        12.6.97
Release:        0
Summary:        Some cockroaches on your root window
License:        GPL-2.0+
Group:          Amusements/Toys/Background
Source:         %{name}.tar.bz2
Source1:        toon_root.c
Source2:        README.SUSE
Patch:          xroach.dif
Patch1:         xroach-return.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
Xroach displays disgusting cockroaches on your root window. These
creepy crawlies scamper around until they find a window to hide under.
Whenever you move or iconify a window, the exposed orthopteras again
scamper for cover.

%prep
%setup -q -n xroach
%patch
%patch1
cp %{S:1} %{S:2} .

%build
export CFLAGS="$RPM_OPT_FLAGS"
xmkmf -a
make %{?jobs:-j%jobs}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
make DESTDIR="$RPM_BUILD_ROOT" install.man

%files
%defattr(-,root,root)
%doc README.SUSE
/usr/%{_xorg7bin}/xroach
%doc %{_xorg7_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
