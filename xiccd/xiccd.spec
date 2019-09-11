#
# spec file for package xiccd
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


Name:           xiccd
Version:        0.2.4
Release:        0
Summary:        X11 ICC Daemon
License:        GPL-3.0+
Group:          System/X11/Utilities
Url:            https://github.com/agalakhov/xiccd
Source:         https://github.com/agalakhov/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(xrandr)

%description
xiccd is a bridge between colord and the X server. Its tasks are:

 * to enumerate displays and register them in colord,
 * to create default ICC profiles based on EDID data,
 * to apply ICC profiles provided by colord,
 * and to maintain user's private ICC storage directory.

It does basically the same as the gnome-settings-daemon colour plugin
or colord-kde without depending on any particular desktop nor the
GTK+ libraries.

The primary goal of xiccd is providing colour profile support for
desktop environments other than GNOME and KDE that do not support
native colour management yet, such as MATE, Xfce, LXDE, to name a
few.

%prep
%setup -q
# XDG autostart.
cat > %{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=X11 ICC Daemon
GenericName=X color management daemon
GenericName[en_GB]=X colour management daemon
Comment=Applies color management profiles to your session
Comment[en_GB]=Applies colour management profiles to your session
Categories=Utility;
Exec=%{name}
Icon=preferences-system
StartupNotify=false
Terminal=false
NoDisplay=true
EOF

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install

rm %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{name}.desktop \
  %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/xdg/autostart/
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
