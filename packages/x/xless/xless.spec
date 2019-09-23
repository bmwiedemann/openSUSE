#
# spec file for package xless
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


Name:           xless
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Provides:       xless17
Version:        1.7
Release:        0
Summary:        Text browser
License:        MIT
Group:          Productivity/Text/Utilities
Url:            http://freeware.sgi.com/source/xless/
Source:         xless-1.7.tar.bz2
Patch0:         xless-1.7.diff
Patch1:         xless-1.7-fonts.diff
Patch2:         xless-1.7-bindir.diff
Patch3:         xless-1.7-exit.diff
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
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
xless 1.7 -- the well-known text browser. Necessary for displaying the
various HOWTOs.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
xmkmf -a
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
install -d -m 755 ${RPM_BUILD_ROOT}/usr/%{_xorg7bin}/
install -d -m 755 ${RPM_BUILD_ROOT}/%{_xorg7_mandir}/man1
install -d -m 755 ${RPM_BUILD_ROOT}/usr/%{_xorg7libshare}/X11/app-defaults
install -m 755 xless ${RPM_BUILD_ROOT}/usr/%{_xorg7bin}/
install -m 644 xless.help ${RPM_BUILD_ROOT}/usr/%{_xorg7libshare}/X11/
install -m 644 XLess.ad  ${RPM_BUILD_ROOT}/usr/%{_xorg7libshare}/X11/app-defaults/XLess
install -m 644 XLess-co.ad ${RPM_BUILD_ROOT}/usr/%{_xorg7libshare}/X11/app-defaults/XLess-color
install -m 644 xless.man ${RPM_BUILD_ROOT}/%{_xorg7_mandir}/man1/xless.1x

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%docdir %{_xorg7_mandir}
%docdir /usr/openwin/man
/usr/%{_xorg7bin}/xless
%dir /usr/%{_xorg7libshare}/X11/app-defaults
%config /usr/%{_xorg7libshare}/X11/app-defaults/XLess
%config /usr/%{_xorg7libshare}/X11/app-defaults/XLess-color
%doc /usr/%{_xorg7libshare}/X11/xless.help
%doc %{_xorg7_mandir}/man1/xless.1x.gz

%changelog
