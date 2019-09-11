#
# spec file for package xfce4-volumed
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


Name:           xfce4-volumed
Version:        0.1.13
Release:        0
Summary:        Daemon Providing Support for Sound Volume Keys
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://git.xfce.org/apps/xfce4-volumed
Source:         http://archive.xfce.org/src/apps/xfce4-volumed/0.1/%{name}-%{version}.tar.bz2
Patch1:         xfce4-mixer-alsa.patch
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     xfce4-mixer

%description
xfce4-volumed is a daemon providing support for sound volume keys present on
some keyboards. It can also display notifications on sound volume change and
mute using a notification server.

%prep
%setup -q
%patch1 -p1
autoreconf -fi

%build
%configure --with-libnotify
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file xfce4-volumed

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README THANKS
%config %{_sysconfdir}/xdg/autostart/xfce4-volumed.desktop
%{_bindir}/xfce4-volumed

%changelog
