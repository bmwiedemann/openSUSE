#
# spec file for package NetworkManager-applet
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.16.0
Release:        0
Summary:        GTK+ tray applet for use with NetworkManager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gnome.org/projects/NetworkManager
Source0:        %{_name}-%{version}.tar.xz

# PATCH-NEEDS-REBASE nm-applet-private-connection.patch boo#751211 bgo#646187 dimstar@opensuse.org -- Create private connections if the user is not authorised. Allows to create wifi connections without root access. Patch under discussion upstream. (WAS: PATCH-FIX-UPSTREAM)
Patch0:         nm-applet-private-connection.patch
# PATCH-FIX-OPENSUSE NetworkManager-gnome-bsc1003069-default-agent-owned-secrets.patch bsc#1003069 hpj@suse.com -- Make sure secrets default to agent-owned (encrypted keyring).
Patch1:         NetworkManager-gnome-bsc1003069-default-agent-owned-secrets.patch
# PATCH-FIX-UPSTREAM feature-app-indicator-desktop-file.patch sflees@suse.com --  nm-applet needs to be launched with --indicator and needs a startup delay incase its started before the systray
Patch2:         feature-app-indicator-desktop-file.patch

BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig
# Needed by Patch0.
#BuildRequires:  polkit-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4) >= 16.04.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(jansson) >= 2.3
BuildRequires:  pkgconfig(libnm) >= 1.7
BuildRequires:  pkgconfig(libnma) >= 1.8.28
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
Requires:       NetworkManager >= 0.9.3
Requires:       dbus(org.freedesktop.secrets)
# Needed for translated country names.
Requires:       iso-codes
# mobile-broadband-provider-info is required for DUN capabilities. The BT plugin crashes without it.
Requires:       mobile-broadband-provider-info
Requires:       nma-data
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
# Needs rebase.
# %%patch0 -p1
%patch1 -p1
%patch2 -p1
translation-update-upstream po nm-applet

%build
%meson \
	-Dappindicator=yes \
	-Dselinux=false \
	-Dintrospection=true \
	-Dlibnm_gtk=false \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r nm-connection-editor GTK GNOME System X-SuSE-ServiceConfiguration
%find_lang nm-applet %{?no_lang_C}

%files
%license COPYING
%doc CONTRIBUTING NEWS
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_bindir}/nm-applet
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/nm-applet.1%{?ext_man}
%{_datadir}/GConf/gsettings/nm-applet.convert

%files lang -f nm-applet.lang

%files -n NetworkManager-connection-editor
%{_bindir}/nm-connection-editor
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/metainfo/nm-connection-editor.appdata.xml
%{_mandir}/man1/nm-connection-editor.1%{?ext_man}

%changelog
