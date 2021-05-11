#
# spec file for package gnome-software
#
# Copyright (c) 2021 SUSE LLC
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


%define gs_plugin_api 16
%define _version 40_0
Name:           gnome-software
Version:        40.1
Release:        0
Summary:        GNOME Software Store
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Software
Source0:        https://download.gnome.org/sources/gnome-software/40/%{name}-%{version}.tar.xz
%if 0%{?sle_version}
# PATCH-FIX-OPENSUSE gnome-software-launch-gpk-update-viewer-for-updates.patch bsc#1077332 boo#1090042 sckang@suse.com -- Don't launch gnome-software when clicking the updates notification. Launch gpk-update-viewer instead.
Patch0:         gnome-software-launch-gpk-update-viewer-for-updates.patch
%endif
# PATCH-FIX-OPENSUSE gnome-software-no-static-lib.patch dimstar@opensuse.org -- convert libgnomesoftware.a to a shared lib
Patch2:         gnome-software-no-static-lib.patch

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  pkgconfig(appstream) >= 0.14.0
BuildRequires:  pkgconfig(flatpak) >= 0.6.12
BuildRequires:  pkgconfig(fwupd) >= 1.0.3
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.11.5
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.18.0
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.2
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.52.0
BuildRequires:  pkgconfig(malcontent-0) >= 0.3.0
BuildRequires:  pkgconfig(ostree-1)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.0
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-4)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(xmlb) >= 0.1.7
# boo#1090042
Requires:       PackageKit
Requires:       fwupd
Requires:       iso-codes
Requires:       (libzypp-plugin-appdata if PackageKit-backend-zypp)
Recommends:     flatpak
# bsc#1178768
%if 0%{?sle_version}
Recommends:     gnome-packagekit
%endif

%description
AppStore like management of Applications for your GNOME Desktop.

%package devel
Summary:        Development files for the GNOME software store
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
This subpackage contains the header files for developing
GNOME software store plugins.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dtests=false \
	-Dvalgrind=false \
	-Dmalcontent=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

# Remove any piece of doc that ends up in non-standard locations and use the doc macro instead
rm %{buildroot}%{_datadir}/doc/%{name}/README.md

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/xmls
%{_datadir}/app-info/xmls/org.gnome.Software.Featured.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Software.appdata.xml
%{_datadir}/metainfo/org.gnome.Software.Plugin.Flatpak.metainfo.xml
%{_datadir}/metainfo/org.gnome.Software.Plugin.Fwupd.metainfo.xml
%{_datadir}/metainfo/org.gnome.Software.Plugin.Odrs.metainfo.xml
%{_datadir}/applications/gnome-software-local-file.desktop
%{_datadir}/applications/org.gnome.Software.desktop
%{_datadir}/dbus-1/services/org.gnome.Software.service
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/glib-2.0/schemas/org.gnome.software.gschema.xml
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
%{_datadir}/icons/hicolor/*/*/*.svg
%dir %{_libdir}/gnome-software
%dir %{_libdir}/gnome-software/plugins-%{gs_plugin_api}
%{_libdir}/gnome-software/libgnomesoftware-%{gs_plugin_api}.so
%{_libdir}/gnome-software/plugins-%{gs_plugin_api}/*.so
#{_libexecdir}/gnome-software-service
%{_libexecdir}/gnome-software-cmd
%{_libexecdir}/gnome-software-restarter
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/gnome-software-service.desktop

%files devel
%doc AUTHORS
%dir %{_includedir}/%{name}
%{_datadir}/gtk-doc/html/%{name}/
%dir %{_datadir}/doc/gnome-software
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/gnome-software.pc

%files lang -f %{name}.lang

%changelog
