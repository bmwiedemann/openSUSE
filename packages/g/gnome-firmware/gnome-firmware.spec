#
# spec file for package gnome-firmware
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gnome-firmware
Version:        3.34.0
Release:        0
Summary:        Install firmware on devices
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.gnome.org/hughsie/gnome-firmware-updater
Source0:        %{name}-%{version}.tar.xz
Patch0:         do-not-call-gtk_init-manually.patch
BuildRequires:  gobject-introspection
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  perl-forks
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xmlb)
Recommends:     %{name}-lang = %{version}
Provides:       gnome-firmware-updater = %{version}-%{release}
Obsoletes:      gnome-firmware-updater < %{version}-%{release}
Provides:       gnome-firmware-updater-lang = %{version}-%{release}
Obsoletes:      gnome-firmware-updater-lang < %{version}-%{release}
%lang_package

%description
This application can update, reinstall and downgrade firmware on devices
supported by fwupd.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r -G "Install firmware on devices" org.gnome.Firmware "GTK;GNOME;Settings;HardwareSettings;"

%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/gnome-firmware
%{_datadir}/applications/org.gnome.Firmware.desktop
%{_datadir}/metainfo/org.gnome.Firmware.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Firmware.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Firmware-symbolic.svg
%{_mandir}/man1/gnome-firmware.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
