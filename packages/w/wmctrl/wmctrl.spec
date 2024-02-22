#
# spec file for package wmctrl
#
# Copyright (c) 2024 SUSE LLC
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


Name:           wmctrl
Version:        1.07
Release:        0
Summary:        Command line tool to interact with an EWMH/NetWM compatible X Window Manager
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://sweb.cz/tripie/utils/wmctrl/
Source:         %{name}-%{version}.tar.bz2
Patch0:         wmctrl_1.07-6.diff.bz2
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)

%description
Wmctrl provides command line access to almost all the features defined
in the EWMH specification. Using it, it's possible to, for example,
obtain information about the window manager, get a detailed list of
desktops and managed windows, switch and resize desktops, change number
of desktops, make windows full-screen, always-above or sticky, and
activate, close, move, resize, maximize and minimize them.

The command line access makes it easy to automate these tasks and
execute them from any application that is able to run a command in
response to some event.

Please note that wmctrl only works with window managers which implement
this specification.

%prep
%autosetup -p1

%build
ls -lha .
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/wmctrl.1%{?ext_man}

%changelog
