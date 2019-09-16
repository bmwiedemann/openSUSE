#
# spec file for package pixmap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pixmap
Version:        2.6
Release:        0
Summary:        XPM Pixel Editor for the X Window System
License:        BSD-3-Clause
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://ftp.gwdg.de/pub/x11/x.org/contrib/applications/pixmap/
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
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  rgb
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
Conflicts:      mmextra
Provides:       pixmap26
Provides:       pixmp = %{version}
Obsoletes:      pixmp <= %{version}

%description
Pixmap is a program which enables you to edit XPM-files (colour
bitmaps). You can use them with every commonly used iconmanager and
even incorporate them in your own desktop environment.

%define _xorg7libs %{_lib}
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %{_mandir}
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb %{_datadir}/X11/xkb
%define _xorg7_termcap %{_prefix}/lib/X11%{_sysconfdir}
%define _xorg7_serverincl %{_includedir}/xorg
%define _xorg7_fonts %{_datadir}/fonts
%define _xorg7_prefix %{_prefix}

%prep
%setup -q -n pixmap
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
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
xmkmf -a
make %{?_smp_mflags} -C SelFile CCOPTIONS="%{optflags} -DPIC -fPIC"
make %{?_smp_mflags} CCOPTIONS="%{optflags} -DPIC -fPIC"

%install
%make_install
make DESTDIR=%{buildroot} install.man

%files
%license COPYRIGHT
%doc README CHANGES
%config %{_prefix}/%{_xorg7libshare}/X11/app-defaults/Pixmap
%dir %{_prefix}/%{_xorg7libshare}/X11/app-defaults
%doc %{_xorg7_mandir}/man1/pixmap.1x.gz
%{_prefix}/%{_xorg7bin}/pixmap
%{_prefix}/%{_xorg7libs32}/X11/Pixmap
%{_prefix}/%{_xorg7libs}/libXgnu.a

%changelog
