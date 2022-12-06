#
# spec file for package pasystray
#
# Copyright (c) 2022 SUSE LLC
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


Name:           pasystray
Version:        0.8.1
Release:        0
Summary:        PulseAudio system tray
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://github.com/christophgysin/pasystray
Source:         https://github.com/christophgysin/pasystray/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(avahi-ui-gtk3)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-broadway-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-broadway-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)
%if 0%{?sle_version} && 0%{?sle_version} < 150300
Requires:       pulseaudio
%else
Requires:       pulseaudio-daemon
%endif
Suggests:       paman
Suggests:       paprefs
Suggests:       pavucontrol
Suggests:       pavumeter

%description
A replacement for the deprecated padevchooser

Pasystray allows setting the default PulseAudio source/sink and moving streams on the fly between sources/sinks without restarting the client applications.

%prep
%setup -q

%build
autoreconf -fi
%configure --sysconfdir=%{_sysconfdir}
%make_build

%install
%make_install
%suse_update_desktop_file  -u -r %{buildroot}%{_datadir}/applications/pasystray.desktop AudioVideo Mixer
%suse_update_desktop_file  -u -r %{buildroot}%{_sysconfdir}/xdg/autostart/pasystray.desktop AudioVideo Mixer

%files
%license LICENSE
%doc AUTHORS README.md TODO
%dir %{_datadir}/pasystray
%{_sysconfdir}/xdg/autostart/pasystray.desktop
%{_bindir}/pasystray
%{_datadir}/applications/pasystray.desktop
%{_datadir}/icons/hicolor/scalable/apps/pasystray.svg
%{_mandir}/man1/pasystray.1%{?ext_man}
%{_datadir}/pasystray/pasystray.gtk3.glade
%{_datadir}/pixmaps/pasystray.png

%changelog
