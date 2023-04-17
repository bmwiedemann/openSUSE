#
# spec file for package NetworkManager-applet
#
# Copyright (c) 2023 SUSE LLC
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


%define _name   network-manager-applet

Name:           NetworkManager-applet
Version:        1.32.0
Release:        0
Summary:        GTK+ tray applet for use with NetworkManager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gnome.org/projects/NetworkManager
Source0:        https://download.gnome.org/sources/network-manager-applet/1.32/%{_name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM feature-app-indicator-desktop-file.patch sflees@suse.com --  nm-applet needs to be launched with --indicator and needs a startup delay incase its started before the systray
Patch1:         feature-app-indicator-desktop-file.patch

BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig
# Needed by Patch0.
#BuildRequires:  polkit-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4) >= 16.04.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(jansson) >= 2.3
BuildRequires:  pkgconfig(libnm) >= 1.15
BuildRequires:  pkgconfig(libnma) >= 1.8.28
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
Requires:       NetworkManager >= 0.9.3
Requires:       dbus(org.freedesktop.secrets)
# Needed for translated country names.
Requires:       iso-codes
# mobile-broadband-provider-info is required for DUN capabilities. The BT plugin crashes without it.
Requires:       mobile-broadband-provider-info
Conflicts:      nma-data < 1.8.28
# libnma was (wronlgy) carrying the glib-schema for org.gnome.nm-applet, now moved back here
Conflicts:      libnma0 < 1.10.4
Requires:       timezone
Recommends:     NetworkManager-connection-editor
Provides:       NetworkManager-client
# NetworkManager-gnome was last used in openSUSE Leap 42.2.
Provides:       NetworkManager-gnome = %{version}
Obsoletes:      NetworkManager-gnome < %{version}
Obsoletes:      NetworkManager-gnome-debuginfo
Obsoletes:      NetworkManager-gnome-lang < %{version}
Provides:       NetworkManager-gnome-lang = %{version}

%description
This package contains utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%package -n NetworkManager-connection-editor
Summary:        GUI to configure connections for NetworkManager
Group:          System/GUI/GNOME
Requires:       mobile-broadband-provider-info

%description -n NetworkManager-connection-editor
NetworkManager Configuration tool - take control over your
connection settings.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
%patch1 -p1

%build
%meson \
	-Dappindicator=yes \
	-Dselinux=false \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r nm-connection-editor GTK GNOME System X-SuSE-ServiceConfiguration
%find_lang nm-applet %{?no_lang_C}

%files
%license COPYING
%doc CONTRIBUTING NEWS
%{_bindir}/nm-applet
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/nm-applet.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/nm-applet.desktop

%files lang -f nm-applet.lang

%files -n NetworkManager-connection-editor
%{_bindir}/nm-connection-editor
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/metainfo/nm-connection-editor.appdata.xml
%{_mandir}/man1/nm-connection-editor.1%{?ext_man}

%changelog
