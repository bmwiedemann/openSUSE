#
# spec file for package pika-backup
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


%define         appname org.gnome.World.PikaBackup
Name:           pika-backup
Version:        0.7.5
Release:        0
Summary:        Simple backups based on borg
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/pika-backup
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         disable-gtk-test.patch
Patch1:         pika-backup-function-depends-on-never-type-fallback-being.patch
BuildRequires:  borgbackup
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson >= 0.57
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12.5
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
Requires:       borgbackup
Requires:       python3-msgpack
Requires:       python3-pyfuse3

%lang_package

%description
Doing backups the easy way. Plugin your USB drive and let the Pika do the rest for you.

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{appname}
%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/pika-backup
%{_bindir}/pika-backup-monitor
%config %{_sysconfdir}/xdg/autostart/%{appname}.Monitor.desktop
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}.Monitor.desktop
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/dbus-1/services/%{appname}.{Api,Monitor}.service

%files lang -f %{name}.lang

%changelog
