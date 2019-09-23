#
# spec file for package rstart
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


Name:           rstart
Version:        1.0.5
Release:        0
Summary:        Sample implementation of a Remote Start client
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:         U_Fix-.-configure-error-sysconfdir-command-not-found.patch
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package includes both the client and server sides implementing
the protocol described in the "A Flexible Remote Execution Protocol
Based on rsh" paper found in the specs/ subdirectory.

This software has been deprecated in favor of the X11 forwarding
provided in common ssh implementations.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure --sysconfdir=/etc
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/rstart
%{_bindir}/rstartd
%dir %{_libdir}/X11
%{_libdir}/X11/rstart/
%{_mandir}/man1/rstart.1%{?ext_man}
%{_mandir}/man1/rstartd.1%{?ext_man}

%changelog
