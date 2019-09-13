#
# spec file for package xgrabsc
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xgrabsc
Url:            ftp://ftp.x.org/contrib/applications/
BuildRequires:  imake
BuildRequires:  ncurses-devel
BuildRequires:  openmotif
BuildRequires:  openmotif-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Version:        2.41
Release:        0
Summary:        A Screen Grabber for the X Window System
License:        HPND
Group:          System/X11/Utilities
Source:         xgrabsc-%{version}.tar.bz2
Source1:        xgrabsc.desktop
Patch:          xgrabsc-%{version}.patch
Patch1:         xgrabsc-%{version}-gcc4.patch
Patch2:         xgrabsc-%{version}-implicit_decl.patch
Patch3:         xgrabsc-%{version}-no_xrdb.patch
Patch4:         xgrabsc-%{version}-new_ncurses.patch
# PATCH-FIX-OPENSUSE xgrabsc-2.41-memoryleak.patch bnc#542498
Patch5:         xgrabsc-%{version}-memoryleak.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
You need screenshots?

xgrab and xgrabsc are powerful tools to save screenshots in files (ps,
xpm, and more) or to print them. xgrabsc is invoked from a shell and
sends the rectangle grabbed on the screen to standard output. xgrab is
a menu-driven front-end to xgrabsc.

This program works only in PPM, XPM, and non-color PostScript formats
for display larger then 8 bits per pixel deep.

Documentation may be obtained by typing man xgrab and man xgrabsc. The
author's original comments can be found in
/usr/share/doc/packages/xgrabsc.

%prep
%setup -q
%patch
%patch1 -p1
%patch2
%patch3
%patch4
%patch5

%build
xmkmf
make clean
make %{?_smp_mflags} 

%install
make install install.man DESTDIR=%buildroot
%suse_update_desktop_file -i %name Utility DesktopUtility

%files
%defattr(-,root,root)
%doc Acks Bugs README README.2_4
%doc %_mandir/man1/*.gz
%config %_datadir/X11/app-defaults/XGrab
%_datadir/applications/*.desktop
%_bindir/xgrab
%_bindir/xgrabsc

%changelog
