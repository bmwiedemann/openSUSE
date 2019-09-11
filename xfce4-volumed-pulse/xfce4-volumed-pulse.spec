#
# spec file for package xfce4-volumed-pulse
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


Name:           xfce4-volumed-pulse
Version:        0.2.3
Release:        0
Summary:        Daemon Providing Support for Sound Volume Keys
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://git.xfce.org/apps/xfce4-volumed
Source:         http://archive.xfce.org/src/apps/xfce4-volumed-pulse/0.2/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(keybinder-3.0) >= 0.2.0
BuildRequires:  pkgconfig(libnotify) >= 0.1.3
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.19
BuildRequires:  pkgconfig(libxfconf-0)

%description
xfce4-volumed-pulse is a daemon providing support for sound volume keys present on
some keyboards. It can also display notifications on sound volume change and
mute using a notification server.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-libnotify
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file xfce4-volumed-pulse

%files
%doc AUTHORS COPYING NEWS README THANKS
%config %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}

%changelog
