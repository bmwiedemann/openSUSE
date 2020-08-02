#
# spec file for package stalonetray
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


Name:           stalonetray
Version:        0.8.3
Release:        0
Summary:        Stand-alone freedesktop.org system tray
#
License:        GPL-2.0+
Group:          System/GUI/Other
#
Url:            http://stalonetray.sourceforge.net/
Source:         http://downloads.sourceforge.net/stalonetray/stalonetray-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM stalonetray-fix-compile-error.diff bernhard@bwalle.de
Patch0:         stalonetray-fix-compile-error.diff
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray (notification
area) for X Window System/X11 (e.g. X.Org or XFree 86). It has full XEMBED
support and minimal dependencies: an X11 lib only. Stalonetray works with
virtually any EWMH-compliant window manager.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS stalonetrayrc.sample
%{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.1%{ext_man}

