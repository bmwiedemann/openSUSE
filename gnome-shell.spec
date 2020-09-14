#
# spec file for package gnome-shell
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


%global __requires_exclude typelib\\(Meta\\)

Name:           gnome-shell
Version:        3.36.6
Release:        0
Summary:        GNOME Shell
# shew extension is LGPL 2.1; gnome-shell-extension-tool is GPL-3.0-or-later
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeShell
Source:         %{name}-%{version}.tar.xz
# SOURCE-FEATURE-SLE aboutMenu fate#314545 dliang@suse.com -- Add an applet on login UI to display suse icon, product name, hostname.
Source1:        aboutMenu.js

# PATCH-FIX-UPSTREAM gnome-shell-private-connection.patch bnc#751211 bgo#646187 dimstar@opensuse.org -- create private connections if the user is not authorized
Patch1:         gnome-shell-private-connection.patch
# PATCH-FIX-OPENSUSE gnome-shell-disable-ibus-when-not-installed.patch bsc#987360 qzhao@suse.com -- disable ibus start when outof Chinese, Japanese, Korean area
Patch2:         gnome-shell-disable-ibus-when-not-installed.patch
# PATCH-FEATURE-OPENSUSE gnome-shell-fate324570-Make-GDM-background-image-configurable.patch fate#324570, glgo#GNOME/gnome-shell#680, boo#1172826 qkzhu@suse.com -- make GDM background image configurable
Patch4:         gnome-shell-fate324570-Make-GDM-background-image-configurable.patch
# PATCH-NEEDS-REBASE gnome-shell-jscSLE9267-Remove-sessionList-of-endSessionDialog.patch jsc#SLE-9267 qkzhu@suse.com -- Remove sessionList of endSessionDialog (WAS: PATCH-FEATURE-OPENSUSE)
Patch5:         gnome-shell-jscSLE9267-Remove-sessionList-of-endSessionDialog.patch
# PATCH-FIX-UPSTREAM gnome-shell-Get-resource-scale-by-get_resource_scale.patch bsc#1169845 glgo#GNOME/gnome-shell!1206 xwang@suse.com -- Get resource scale by get_resource_scale
Patch6:         gnome-shell-Get-resource-scale-by-get_resource_scale.patch

## NOTE: Keep SLE-only patches at bottom (starting on 1000).
# PATCH-FEATURE-SLE gnome-shell-gdm-login-applet.patch fate#314545 dliang@suse.com -- Add an applet on login UI to display suse icon, product name, hostname.
Patch1001:      gnome-shell-gdm-login-applet.patch
# PATCH-FEATURE-SLE gnome-shell-domain.patch fate#307773 dliang@suse.com -- Active Directory Integration
Patch1002:      gnome-shell-domain.patch
# PATCH-FIX-SLE gnome-shell-screen-disappear.patch bnc#870217 dliang@suse.com -- screen disapper.
Patch1003:      gnome-shell-screen-disappear.patch
# PATCH-FIX-SLE endSession-dialog-update-time-label-every-sec.patch bnc#886132 cxiong@suse.com -- update time label every second in end session dialog
Patch1004:      endSession-dialog-update-time-label-every-sec.patch
# PATCH-FEATURE-SLE gnome-shell-864872-unlock-by-mouse-motion.patch bnc#864872 dliang@suse.com -- 10px mouse motion to lift screen shield.
Patch1005:      gnome-shell-864872-unlock-by-mouse-motion.patch
# PATCH-FIX-SLE gnome-shell-lock-bg-on-primay.patch bnc#894050 dliang@suse.com -- display background of lock dialog on the primary screen.
Patch1006:      gnome-shell-lock-bg-on-primary.patch
# PATCH-FIX-SLE gs-fate318433-prevent-same-account-multi-logins.patch fate#318433 cxiong@suse.com -- prevent multiple simultaneous login.
Patch1007:      gs-fate318433-prevent-same-account-multi-logins.patch
# PATCH-FEATURE-SLE gnome-shell-1007468-lock-screen-SUSE-logo-missing.patch xwang@suse.com -- Add SUSE logo on lock screen for GNOME theme.
Patch1008:      gnome-shell-1007468-lock-screen-SUSE-logo-missing.patch

# needed for directory ownership
BuildRequires:  asciidoc
BuildRequires:  dbus-1
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  translation-update-upstream
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gcr-base-3) >= 3.7.5
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.63.2
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= 3.9.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.34.2
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.49.1
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.33.1
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.13.2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libcroco-0.6) >= 0.6.8
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.1
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.17.2
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(libmutter-6) >= 3.36.1
BuildRequires:  pkgconfig(libnm) >= 1.10.4
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.11
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mutter-clutter-6) >= 3.36.1
BuildRequires:  pkgconfig(mutter-cogl-6) >= 3.36.1
BuildRequires:  pkgconfig(mutter-cogl-pango-6) >= 3.36.1
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.100
BuildRequires:  pkgconfig(x11)
BuildRequires:  python(abi) >= 3
Requires:       gdk-pixbuf-loader-rsvg
# "System settings" menu item
Requires:       gnome-control-center
Requires:       gnome-session
# For a GSettings schema and power system icon
Requires:       gnome-settings-daemon
# "High Contrast" in accessibility status icon
Requires:       gnome-themes-accessibility
Requires:       gsettings-desktop-schemas
Requires:       mutter >= 3.35.90
Requires:       typelib(Rsvg)
Recommends:     %{name}-calendar
## Finally, dependencies for session services that are needed for system icons and the user menu
# bluetooth system icon
# (lowered to recommends due to bsc#1067603, some setups without bluetooth might want to avoid this dependency)
Recommends:     gnome-bluetooth
# The dateTime applet in the panel launches gnome-clocks upon user request
Recommends:     gnome-clocks
# gnome-shell implements the dbus interface org.freedesktop.Notifications directly
Provides:       dbus(org.freedesktop.Notifications)
# gnome-shell-browser-plugin dropped in 3.31.4
Obsoletes:      gnome-shell-browser-plugin <= %{version}

%description
The GNOME Shell redefines user interactions with the GNOME desktop. In
particular, it offers new paradigms for launching applications, accessing
documents, and organizing open windows in GNOME.

%package devel
Summary:        Development files for GNOME Shell
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
The GNOME Shell redefines user interactions with the GNOME desktop. In
particular, it offers new paradigms for launching applications, accessing
documents, and organizing open windows in GNOME.

%package calendar
Summary:        Evolution Calendar support for GNOME Shell
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# The clock / calendar applet in the panel requires e-d-s (bnc#795793).
Requires:       evolution-data-server
Supplements:    packageand(%{name}:evolution-data-server)

%description calendar
This package adds support for Evolution Calendar, such as appointments
into GNOME Shell calendar.

%package -n gnome-extensions
Summary:        Extensions app for GNOME Shell
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}

%description -n gnome-extensions
This package contains an optional extensions app for managing GNOME Shell extensions.

%lang_package

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch4 -p1
#patch5 -p1
%patch6 -p1

translation-update-upstream

%if 0%{?sle_version}
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%endif

%if 0%{?sle_version}
cp %{SOURCE1} js/ui/
%endif

%build
%meson \
	--libexecdir=%{_libexecdir}/%{name} \
	-Dgtk_doc=true \
	-Dman=true \
	-Dnetworkmanager=true \
	-Dsystemd=true \
	%{nil}
%meson_build

%install
%meson_install
# This is the directory where extensions get installed
install -d %{buildroot}%{_datadir}/gnome-shell/extensions
# This is the directory where search providers get installed
install -d %{buildroot}%{_datadir}/gnome-shell/search-providers
%find_lang %{name} %{?no_lang_C}
# Work around race, as reported in bnc#844891 & bgo#709313.
install -d %{buildroot}%{_datadir}/gnome-shell/modes
%fdupes %{buildroot}%{_prefix}
# Not needed, only used for nightly git snapshots
rm -f %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions.Devel.svg

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/gnome-shell
%{_bindir}/gnome-shell-extension-prefs
%dir %{_libdir}/gnome-shell
%dir %{_libexecdir}/gnome-shell
%exclude %{_libexecdir}/gnome-shell/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell/gnome-shell-portal-helper
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
#%%{_libdir}/gnome-shell/ShellMenu-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_libdir}/gnome-shell/libgnome-shell-menu.so
%{_libdir}/gnome-shell/libgnome-shell.so
%{_libdir}/gnome-shell/libgvc.so
%{_libdir}/gnome-shell/libst-1.0.so
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/org.gnome.Shell.Extensions.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
# Own these dirs for extensions, search-providers and work around a race condition
%dir %{_datadir}/gnome-shell/extensions
%dir %{_datadir}/gnome-shell/search-providers
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/gnome-shell-dbus-interfaces.gresource
%{_datadir}/gnome-shell/gnome-shell-theme.gresource
%{_datadir}/gnome-shell/gnome-shell-osk-layouts.gresource
%{_datadir}/gnome-shell/perf-background.xml
%{_mandir}/man?/gnome-shell.?%{ext_man}
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_userunitdir}/gnome-shell-wayland.target
%{_userunitdir}/gnome-shell-x11.target
%{_userunitdir}/gnome-shell-wayland.service
%{_userunitdir}/gnome-shell-x11.service
%{_userunitdir}/gnome-shell-disable-extensions.service
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%{_libexecdir}/gnome-shell/gnome-shell-overrides-migration.sh
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg

%dir %{_libdir}/gnome-shell/girepository-1.0
%{_libdir}/gnome-shell/girepository-1.0/Shew-0.typelib

%{_libdir}/gnome-shell/libshew-0.so

%{_datadir}/dbus-1/services/org.gnome.Shell.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Notifications.service

%{_datadir}/gnome-shell/org.gnome.Shell.Extensions
%{_datadir}/gnome-shell/org.gnome.Shell.Extensions.src.gresource
%{_datadir}/gnome-shell/org.gnome.Shell.Notifications
%{_datadir}/gnome-shell/org.gnome.Shell.Notifications.src.gresource

%files devel
%doc HACKING.md
%doc %{_datadir}/gtk-doc/html
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-perf-tool
%{_datadir}/gnome-shell/*.gir
%dir %{_datadir}/gnome-shell/gir-1.0
%{_datadir}/gnome-shell/gir-1.0/Shew-0.gir

%files calendar
%{_datadir}/applications/evolution-calendar.desktop
%{_libexecdir}/gnome-shell/gnome-shell-calendar-server
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service

%files -n gnome-extensions
%{_bindir}/gnome-extensions
%{_bindir}/gnome-extensions-app
%{_datadir}/applications/org.gnome.Extensions.desktop
%{_mandir}/man?/gnome-extensions.?%{ext_man}
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
%{_datadir}/bash-completion/completions/gnome-extensions
%{_datadir}/dbus-1/services/org.gnome.Extensions.service
%{_datadir}/gnome-shell/org.gnome.Extensions
%{_datadir}/gnome-shell/org.gnome.Extensions.data.gresource
%{_datadir}/gnome-shell/org.gnome.Extensions.src.gresource
%{_datadir}/metainfo/org.gnome.Extensions.metainfo.xml

%files lang -f %{name}.lang

%changelog
