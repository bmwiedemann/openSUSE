#
# spec file for package stalonetray
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


Name:           stalonetray
Version:        1.5.0
Release:        0
Summary:        Stand-alone freedesktop.org system tray
License:        GPL-2.0-or-later
URL:            https://github.com/d3adb5/stalonetray
Source:         https://github.com/d3adb5/stalonetray/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE stalonetray-docbook-root.patch -- Look for the docbook stylesheet in the openSUSE location
Patch0:         stalonetray-docbook-root.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray (notification
area) for X Window System/X11 (e.g. X.Org or XFree 86). It has full XEMBED
support and minimal dependencies: an X11 lib only. Stalonetray works with
virtually any EWMH-compliant window manager.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc AUTHORS README.md TODO stalonetrayrc.sample
%config(noreplace) %{_sysconfdir}/stalonetrayrc
%{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.1%{?ext_man}

%changelog
