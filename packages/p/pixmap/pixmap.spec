#
# spec file for package pixmap
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pixmap
Url:            ftp://ftp.x.org/contrib/applications/pixmap
BuildRequires:  imake
BuildRequires:  rgb
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
Provides:       pixmap26
Conflicts:      mmextra
Version:        2.6
Release:        0
Provides:       pixmp = %version
Obsoletes:      pixmp <= %version
Summary:        XPM Pixel Editor for the X Window System
License:        BSD-3-Clause
Group:          Productivity/Graphics/Bitmap Editors
Source:         pixmap2.6.tar.gz
# upstream patches
Patch0:         pixmap_2.6.patch1.gz
Patch1:         pixmap_2.6.patch2.gz
Patch2:         pixmap_2.6.patch3.gz
Patch3:         pixmap_2.6.patch4.gz
# end of upstream patches
Patch4:         pixmap2.6.patch
Patch5:         pixmap2.6-ia64.patch
Patch6:         pixmap-nonvoid.patch
Patch7:         pixmap-xorg7.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pixmap is a program which enables you to edit XPM-files (colour
bitmaps). You can use them with every commonly used iconmanager and
even incorporate them in your own desktop environment.

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
%define _xorg7_prefix /usr

%prep
%setup -n pixmap
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
# use this patch only if new X.org 7.x or higher is present
%patch7
# contains data used for earlier versions of X.
rm -rf X11

%build
xmkmf -a
make -C SelFile CCOPTIONS="$RPM_OPT_FLAGS -DPIC -fPIC"
make CCOPTIONS="$RPM_OPT_FLAGS -DPIC -fPIC"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%files
%defattr(-,root,root)
/usr/%{_xorg7bin}/pixmap
/usr/%{_xorg7libs32}/X11/Pixmap
%dir /usr/%{_xorg7libshare}/X11/app-defaults
%config /usr/%{_xorg7libshare}/X11/app-defaults/Pixmap
/usr/%{_xorg7libs}/libXgnu.a
%doc %{_xorg7_mandir}/man1/pixmap.1x.gz
%doc README COPYRIGHT CHANGES  

%clean
rm -rf "$RPM_BUILD_ROOT"

%changelog
