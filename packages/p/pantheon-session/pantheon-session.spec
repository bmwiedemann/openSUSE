#
# spec file for package pantheon-session
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


Name:           pantheon-session
Version:        8.0.1
Release:        0
Summary:        The Pantheon Session Handler
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/session-settings
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         remove-onboard.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gnome-keyring
BuildRequires:  meson
%if 0%{?suse_version} > 1600
BuildRequires:  onboard
%endif
BuildRequires:  orca
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildArch:      noarch

%description
Provides a session entry for display managers such as gdm or lightdm.

%prep
%autosetup -N -n session-settings-%{version}
%if 0%{?suse_version} <= 1600
%patch -P0 -p1
%endif

%build
%meson \
  -Dmimeapps-list=true \
  -Dfallback-session=icewom \
  -Ddetect-program-prefixes=false \
  -Dsystemd=true \
  -Dwayland=true
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%if 0%{?suse_version} >= 1600
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/
%endif

%files
%license LICENSE
%doc README.md
%{_userunitdir}/gnome-session@{pantheon-wayland,pantheon}.target.d/session.conf
%{_datadir}/applications/pantheon-mimeapps.list
%{_datadir}/gnome-session/sessions/pantheon{,-wayland}.session
%{_datadir}/wayland-sessions/pantheon-wayland.desktop
%{_datadir}/xsessions/pantheon.desktop
%if 0%{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/*
%else
%{_sysconfdir}/xdg/autostart/*
%endif
%dir %{_datadir}/{gnome-session,gnome-session/sessions,wayland-sessions}
%dir %{_userunitdir}/gnome-session@pantheon{,-wayland}.target.d

%changelog
