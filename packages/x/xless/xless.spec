#
# spec file for package xless
#
# Copyright (c) 2021 SUSE LLC
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
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix %{_prefix}
Name:           xless
Version:        1.7
Release:        0
Summary:        Text browser
License:        MIT
Group:          Productivity/Text/Utilities
URL:            http://freeware.sgi.com/source/xless/
Source:         xless-1.7.tar.bz2
Patch0:         xless-1.7.diff
Patch1:         xless-1.7-fonts.diff
Patch2:         xless-1.7-bindir.diff
Patch3:         xless-1.7-exit.diff
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Provides:       xless17

%description
xless 1.7 -- the well-known text browser. Necessary for displaying the
various HOWTOs.

%prep
%autosetup -p0

%build
xmkmf -a
%make_build CCOPTIONS="%{optflags}"

%install
install -d -m 755 %{buildroot}%{_prefix}/%{_xorg7bin}/
install -d -m 755 %{buildroot}/%{_xorg7_mandir}/man1
install -d -m 755 %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/app-defaults
install -m 755 xless %{buildroot}%{_prefix}/%{_xorg7bin}/
install -m 644 xless.help %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/
install -m 644 XLess.ad  %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/app-defaults/XLess
install -m 644 XLess-co.ad %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/app-defaults/XLess-color
install -m 644 xless.man %{buildroot}/%{_xorg7_mandir}/man1/xless.1x

%files
%docdir %{_xorg7_mandir}
%docdir %{_prefix}/openwin/man
%{_prefix}/%{_xorg7bin}/xless
%dir %{_prefix}/%{_xorg7libshare}/X11/app-defaults
%config %{_prefix}/%{_xorg7libshare}/X11/app-defaults/XLess
%config %{_prefix}/%{_xorg7libshare}/X11/app-defaults/XLess-color
%doc %{_prefix}/%{_xorg7libshare}/X11/xless.help
%{_xorg7_mandir}/man1/xless.1x*

%changelog
