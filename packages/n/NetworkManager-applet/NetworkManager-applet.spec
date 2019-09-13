#
# spec file for package NetworkManager-applet
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


%define sover   0
%define _name   network-manager-applet
%if 0%{?is_opensuse}
%bcond_without appindicator
%else
%bcond_with appindicator
%endif
%bcond_with meson
Name:           NetworkManager-applet
Version:        1.8.22
Release:        0
Summary:        GTK+ tray applet for use with NetworkManager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Url:            https://gnome.org/projects/NetworkManager
Source:         http://download.gnome.org/sources/network-manager-applet/1.8/%{_name}-%{version}.tar.xz
# PATCH-NEEDS-REBASE nm-applet-private-connection.patch boo#751211 bgo#646187 dimstar@opensuse.org -- Create private connections if the user is not authorised. Allows to create wifi connections without root access. Patch under discussion upstream. (WAS: PATCH-FIX-UPSTREAM)
Patch0:         nm-applet-private-connection.patch
# PATCH-FIX-OPENSUSE NetworkManager-gnome-bsc1003069-default-agent-owned-secrets.patch bsc#1003069 hpj@suse.com -- Make sure secrets default to agent-owned (encrypted keyring).
Patch1:         NetworkManager-gnome-bsc1003069-default-agent-owned-secrets.patch
# PATCH-FIX-UPSTREAM feature-app-indicator-desktop-file.patch sflees@suse.com --  nm-applet needs to be launched with --indicator and needs a startup delay incase its started before the systray
Patch2:         feature-app-indicator-desktop-file.patch

BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig
# Needed by Patch0.
BuildRequires:  polkit-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gck-1) >= 3.14
BuildRequires:  pkgconfig(gcr-3) >= 3.14
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(jansson) >= 2.3
BuildRequires:  pkgconfig(libnm) >= 1.7
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
Recommends:     %{name}-lang
Recommends:     NetworkManager-connection-editor
Provides:       NetworkManager-client
# NetworkManager-gnome was last used in openSUSE Leap 42.2.
Provides:       NetworkManager-gnome = %{version}
Obsoletes:      NetworkManager-gnome < %{version}
Obsoletes:      NetworkManager-gnome-debuginfo
Obsoletes:      NetworkManager-gnome-lang < %{version}
Provides:       NetworkManager-gnome-lang = %{version}
%if %{with meson}
BuildRequires:  meson >= 0.43.0
%else
BuildRequires:  libtool
%endif
%if %{with appindicator}
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4) >= 16.04.0
%endif

%description
This package contains utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.

%package -n NetworkManager-connection-editor
Summary:        GUI to configure connections for NetworkManager
Group:          System/GUI/GNOME

%description -n NetworkManager-connection-editor
NetworkManager Configuration tool - take control over your
connection settings.

%package -n libnma%{sover}
Summary:        NetworkManager UI dialog library
Group:          System/Libraries
Requires:       nma-data >= %{version}

%description -n libnma%{sover}
This library provides UI dialogs for NetworkManager integration.

%package -n nma-data
Summary:        NetworkManager UI dialogs
Group:          System/Libraries
Obsoletes:      libnma-data < %{version}
Provides:       libnma-data = %{version}
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description -n nma-data
This package provides GTK+ dialogs for NetworkManager integration.

%package -n typelib-1_0-NMA-1_0
Summary:        NetworkManager UI dialogs -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-NMA-1_0
This library provides GTK+ dialogs for NetworkManager integration
provided as introspection bindings.

%package -n libnma-devel
Summary:        NetworkManager UI dialogs -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libnma0 = %{version}
Requires:       typelib-1_0-NMA-1_0 = %{version}

%description -n libnma-devel
This library provides GTK+ dialogs for NetworkManager integration.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
# Needs rebase.
# %%patch0 -p1
%patch1 -p1
%if %{with appindicator}
%patch2 -p1
%endif
translation-update-upstream po network-manager-applet

%build
%if %{with meson}
%meson \
%if %{with appindicator}
    -Dappindicator=true \
%endif
    -Dselinux=false \
    -Dintrospection=true \
    -Dlibnm_gtk=false \
    %{nil}
%meson_build
%else
autoreconf -fiv
%configure \
    --disable-static \
%if %{with appindicator}
    --with-appindicator \
%endif
    --without-selinux \
    --without-libnm-gtk
%make_build
%endif

%install
%if %{with meson}
%meson_install
%else
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%endif
%suse_update_desktop_file -r nm-connection-editor GTK GNOME System X-SuSE-ServiceConfiguration
%find_lang network-manager-applet %{?no_lang_C}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%post -n nma-data
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%postun -n nma-data
%glib2_gsettings_schema_postun
%endif

%post -n libnma%{sover} -p /sbin/ldconfig
%postun -n libnma%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc CONTRIBUTING NEWS
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_bindir}/nm-applet
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/nm-applet.1%{?ext_man}

%files lang -f network-manager-applet.lang

%files -n NetworkManager-connection-editor
%{_bindir}/nm-connection-editor
%{_datadir}/applications/nm-connection-editor.desktop
%{_datadir}/metainfo/nm-connection-editor.appdata.xml
%{_mandir}/man1/nm-connection-editor.1%{?ext_man}

%files -n libnma%{sover}
%{_libdir}/libnma.so.%{sover}*

%files -n typelib-1_0-NMA-1_0
%{_libdir}/girepository-1.0/NMA-1.0.typelib

%files -n nma-data
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files -n libnma-devel
%doc %{_datadir}/gtk-doc/html/libnma/
%{_includedir}/libnma/
%{_libdir}/libnma.so
%{_libdir}/pkgconfig/libnma.pc
%{_datadir}/gir-1.0/NMA-1.0.gir

%changelog
