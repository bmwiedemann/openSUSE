#
# spec file for package gnome-firmware-updater
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


Name:           gnome-firmware-updater
Version:        0.0.1~git.20190830
Release:        0
Summary:        User interface for installing firmware on devices
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.gnome.org/hughsie/gnome-firmware-updater
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xmlb)

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
%suse_update_desktop_file -r -G "Install firmware on devices" org.gnome.FirmwareUpdater "GTK;GNOME;Settings;HardwareSettings;"

%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/gnome-firmware-updater
%{_datadir}/applications/org.gnome.FirmwareUpdater.desktop
%{_datadir}/metainfo/org.gnome.FirmwareUpdater.metainfo.xml

%files lang -f %{name}.lang


%changelog
