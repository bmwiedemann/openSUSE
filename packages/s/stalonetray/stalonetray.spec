#
# spec file for package stalonetray
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


Name:           stalonetray
Version:        0.8.4
Release:        0
Summary:        Stand-alone freedesktop.org system tray
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://kolbusa.github.io/stalonetray/
Source:         https://github.com/kolbusa/stalonetray/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-docbook-root.patch -- Fix docbook stylesheet root
Patch0:         fix-docbook-root.patch
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray (notification
area) for X Window System/X11 (e.g. X.Org or XFree 86). It has full XEMBED
support and minimal dependencies: an X11 lib only. Stalonetray works with
virtually any EWMH-compliant window manager.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build stalonetrayrc.sample

%install
%make_install

%files
%license COPYING
%doc AUTHORS BUGS stalonetrayrc.sample
%{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.1%{?ext_man}

%changelog
