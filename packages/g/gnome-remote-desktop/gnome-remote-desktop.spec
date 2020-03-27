#
# spec file for package gnome-remote-desktop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global systemd_unit gnome-remote-desktop.service

Name:           gnome-remote-desktop
Version:        0.1.8
Release:        0
Summary:        GNOME Remote Desktop screen sharing service
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.gnome.org/jadahl/gnome-remote-desktop
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.10.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libvncserver) >= 0.9.10
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

Requires:       pipewire >= 0.1.3

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_user_post %{systemd_unit}

%preun
%systemd_user_preun %{systemd_unit}

%postun
%systemd_user_postun_with_restart %{systemd_unit}

%files
%license COPYING
%doc README
%{_libexecdir}/gnome-remote-desktop-daemon
%{_userunitdir}/gnome-remote-desktop.service
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml

%changelog
