#
# spec file for package pantheon-settings-daemon
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         appid io.elementary.settings-daemon
Name:           pantheon-settings-daemon
Version:        8.5.0
Release:        0
Summary:        A daemon for the Pantheon Desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/settings-daemon
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{appid}.check-for-firmware-updates.service
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(packagekit-glib2)

%description
%{summary}.

%lang_package

%prep
%autosetup -n settings-daemon-%{version}

%build
%meson \
  -Dubuntu_drivers=false
%meson_build

%install
%meson_install
%find_lang %{appid}

# install our own systemd unit file
install -Dm0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{appid}.check-for-firmware-updates.service

%post
%service_add_post %{appid}.check-for-firmware-updates.service

%pre
%service_add_pre %{appid}.check-for-firmware-updates.service

%postun
%service_del_postun %{appid}.check-for-firmware-updates.service

%preun
%service_del_preun %{appid}.check-for-firmware-updates.service

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/{accountsservice,accountsservice/interfaces}
%dir %{_datadir}/{xdg-desktop-portal,xdg-desktop-portal/portals}
%{_bindir}/%{appid}
%{_datadir}/accountsservice/interfaces/io.elementary.SettingsDaemon.AccountsService.xml
%{_datadir}/dbus-1/interfaces/io.elementary.SettingsDaemon.AccountsService.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.settings-daemon.service
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/xdg-desktop-portal/portals/%{appid}.portal
%{_libexecdir}/%{appid}.xdg-desktop-portal
%{_unitdir}/%{appid}.check-for-firmware-updates.service
%{_unitdir}/%{appid}.check-for-firmware-updates.timer
%{_userunitdir}/%{appid}.service
%{_userunitdir}/%{appid}.system-update.service
%{_userunitdir}/%{appid}.system-update.timer
%{_userunitdir}/%{appid}.xdg-desktop-portal.service

%files lang -f %{appid}.lang

%changelog
