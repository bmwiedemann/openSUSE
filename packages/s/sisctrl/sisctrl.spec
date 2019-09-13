#
# spec file for package sisctrl
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


Name:           sisctrl
Version:        0.0.20051202
Release:        0
# src/sisctrlext.c is licensed under the GPL-2.0 "only". Hence the below license
Summary:        SiS Display Control Panel
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            http://www.winischhofer.net/
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE sisctrl.diff bnc#218755 bnc#483401 -- Add missing return value - Define functions, which don't return anything, as void - Fix build by linking with libm - Fix rpmlint warning "no-return-in-nonvoid-function"
Patch0:         sisctrl.diff
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utility to set some display properties during server runtime.

%define _xorglibdir %(pkg-config --variable prefix x11 || echo /usr/X11R6)/%{_lib}

%prep
%setup -q
%patch0

%build
autoreconf -fi
%configure --with-xv-path=%{_xorglibdir}
make %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-,root,root,-)
%{_bindir}/sisctrl
%{_mandir}/man1/sisctrl.1x.gz

%changelog
