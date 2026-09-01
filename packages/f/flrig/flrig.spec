#
# spec file for package flrig
#
# Copyright (c) 2026 SUSE LLC
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


Name:           flrig
Version:        2.0.12
Release:        0
Summary:        Hamradio transceiver control software
# Legal-Review-Notice: COPYING is a stale GPLv2 text; every source header grants
# GPL-3.0-or-later (Debian and Fedora concluded the same). Two sets of files in
# flrig_SOURCES carry a weaker grant and are compiled into the binary:
# src/xmlrpcpp (a bundled flxmlrpc copy, LGPL-3.0-or-later -- 2.0.12 has no
# system-flxmlrpc configure check) and the FLTK-derived
# src/widgets/Fl_Text_{Buffer,Display,Editor}_mod.cxx plus their headers, which
# grant "Library GPL version 2, or any later version" = LGPL-2.0-or-later.
# src/cmedia/hid_win.cxx (GPL-3.0-only) is __WIN32__-only and never built here.
License:        GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://sourceforge.net/projects/fldigi/
#Git-Clone:     https://git.code.sf.net/p/flrig/flrig
Source:         https://downloads.sourceforge.net/project/fldigi/%{name}/%{name}-%{version}.tar.gz
# also keeps glib2 in the build root; without it rpmlint's bundled
# desktop-file-validate cannot load libgio and reports a false invalid-desktopfile
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
# 2.0.12 removed the system-flxmlrpc configure check; src/xmlrpcpp is always compiled in
Provides:       bundled(flxmlrpc)
# configure auto-detects it and silently drops GPIO PTT/CW keying without it;
# every Leap 16.x / SLFO carries libgpiod 1.6.3, so gate on Tumbleweed/Factory
%if 0%{?suse_version} >= 1699
BuildRequires:  pkgconfig(libgpiod) >= 2.2.1
%endif

%description
FLRIG is a transceiver control program designed to be used either stand alone or
as an adjunct to FLDIGI. The supported transceivers all have some degree of CAT.
The FLRIG user interface changes to accommodate the degree of CAT support
available for the transceiver in use.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/flrig
%{_datadir}/applications/flrig.desktop
%{_datadir}/pixmaps/flrig.xpm

%changelog
