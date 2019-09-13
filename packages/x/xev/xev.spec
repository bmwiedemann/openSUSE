#
# spec file for package xev
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xev
Version:        1.2.3
Release:        0
Summary:        Utility to print contents of X events
License:        X11
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        %name.keyring
Patch0:         u_Add-event-filter-for-motion-and-button-events.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xrandr) >= 1.2
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xev creates a window and then asks the X server to send it X11 events
whenever anything happens to the window (such as it being moved,
resized, typed in, clicked in, etc.). You can also attach it to an
existing window. It is useful for seeing what causes events to occur
and to display the information that they contain; it is essentially a
debugging and development tool, and should not be needed in normal
usage.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%{_bindir}/xev
%{_mandir}/man1/xev.1%{?ext_man}

%changelog
