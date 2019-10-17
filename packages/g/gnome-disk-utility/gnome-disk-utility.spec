#
# spec file for package gnome-disk-utility
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


Name:           gnome-disk-utility
Version:        3.34.0
Release:        0
Summary:        Disks application for dealing with storage devices
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://wiki.gnome.org/Apps/Disks
Source0:        https://download.gnome.org/sources/gnome-disk-utility/3.34/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(dvdread) >= 4.2.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.0
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.1
BuildRequires:  pkgconfig(liblzma) >= 5.0.5
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libsecret-1) >= 0.7
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(pwquality) >= 1.0.0
BuildRequires:  pkgconfig(udisks2) >= 2.7.6
Requires:       udisks2

%description
The gnome-disk-utility project provides the Disks application for
dealing with storage devices.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po %{name}

%build
%meson \
	-Dlibsystemd=true \
	-Dgsd_plugin=true \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r -G "Disk Utility" org.gnome.DiskUtility GNOME GTK System HardwareSettings
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS HACKING NEWS README.md TODO
%{_bindir}/gnome-disks
%{_bindir}/gnome-disk-image-mounter
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/icons/hicolor/
%{_mandir}/man1/gnome-disk-image-mounter.1%{?ext_man}
%{_mandir}/man1/gnome-disks.1%{?ext_man}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.DiskUtility.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
# The session / settings daemon plugin:
%{_libexecdir}/gsd-disk-utility-notify
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop

%files lang -f %{name}.lang

%changelog
