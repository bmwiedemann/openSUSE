#
# spec file for package sessreg
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


Name:           sessreg
Version:        1.1.2
Release:        0
Summary:        Utility to manage utmp/wtmp entries for X sessions
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
BuildRequires:  pkgconfig(xproto) >= 7.0.25
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sessreg is a simple program for managing utmp/wtmp entries for X sessions.
It was originally written for use with xdm, but may also be used with
other display managers such as gdm or kdm.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/sessreg
%{_mandir}/man1/sessreg.1%{?ext_man}

%changelog
