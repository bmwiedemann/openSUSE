#
# spec file for package gnome-shell
#
# Copyright (c) 2024 SUSE LLC
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


%global __requires_exclude typelib\\(Meta|MetaTest|Soup|St|Cogl|Clutter|TelepathyGlib\\)
%define mutter_api 14
%define mutter_req 46.0

Name:           gnome-shell
Version:        46.3.1
Release:        0
Summary:        GNOME Shell
# shew extension is LGPL 2.1; gnome-shell-extension-tool is GPL-3.0-or-later
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeShell
# Source url disabled as we are using a git checkout via source service
Source0:        %{name}-%{version}.tar.zst
Source1:        libgnome-volume-control-0.gitmodule.tar.zst

# SOURCE-FEATURE-OPENSUSE noise-texture boo#1176418 qkzhu@suse.com -- Add noise-texture as the default greeter background, used by patch4.
Source100:      noise-texture.png

# PATCH-FIX-UPSTREAM gnome-shell-private-connection.patch bnc#751211 bgo#646187 dimstar@opensuse.org -- create private connections if the user is not authorized
Patch1:         gnome-shell-private-connection.patch
# PATCH-FIX-OPENSUSE gnome-shell-executable-path-not-absolute.patch bsc#1176051 xwang@suse.com --  Fix ExecStart is not absolute path
Patch7:         gnome-shell-executable-path-not-absolute.patch
# PATCH-FIX-UPSTREAM gnome-shell-exit-crash-workaround.patch bsc#1190878 glgo#GNOME/gnome-shell#4344 qkzhu@suse.com -- Workaround logout crashing
Patch8:         gnome-shell-exit-crash-workaround.patch
# PATCH-FIX-UPSTREAM gnome-shell-fix-cursor-on-hide-preedit.patch glgo#GNOME/gnome-shell!3318 alynx.zhou@suse.com -- Correctly reset cursor when hide preedit
Patch9:         gnome-shell-fix-cursor-on-hide-preedit.patch

## NOTE: Keep SLE-only patches at bottom (starting on 1000).
# PATCH-FEATURE-SLE gnome-shell-gdm-login-applet.patch fate#314545 dliang@suse.com -- Add an applet on login UI to display suse icon, product name, hostname.
Patch1001:      gnome-shell-gdm-login-applet.patch
# PATCH-FEATURE-SLE gnome-shell-domain.patch fate#307773 dliang@suse.com -- Active Directory Integration
Patch1002:      gnome-shell-domain.patch
# PATCH-FIX-SLE gnome-shell-screen-disappear.patch bnc#870217 dliang@suse.com -- screen disapper.
Patch1003:      gnome-shell-screen-disappear.patch
# PATCH-FIX-SLE endSession-dialog-update-time-label-every-sec.patch bnc#886132 cxiong@suse.com -- update time label every second in end session dialog
Patch1004:      endSession-dialog-update-time-label-every-sec.patch
# PATCH-FIX-SLE gs-fate318433-prevent-same-account-multi-logins.patch fate#318433 cxiong@suse.com -- prevent multiple simultaneous login.
Patch1007:      gs-fate318433-prevent-same-account-multi-logins.patch
# PATCH-FIX-SLE gnome-shell-disable-ibus-when-not-installed.patch bsc#987360 qzhao@suse.com -- disable ibus start when outof Chinese, Japanese, Korean area
Patch1008:      gnome-shell-disable-ibus-when-not-installed.patch
# PATCH-FEATURE-SLE gnome-shell-fate324570-Make-GDM-background-image-configurable.patch fate#324570, glgo#GNOME/gnome-shell#680, boo#1172826 qkzhu@suse.com -- make GDM background image configurable
Patch1009:      gnome-shell-fate324570-Make-GDM-background-image-configurable.patch
# PATCH-FIX-UPSTREAM gnome-shell-jsc#SLE-16051-Input-method-recommendation.patch jsc#SLE-16051 glgo#GNOME/gnome-shell!1563 qzhao@suse.com -- launch recommended input engines when Gnome-shell init in CJK regions.
Patch1010:      gnome-shell-jsc#SLE-16051-Input-method-recommendation.patch
# PATCH-FIX-SLE gnome-shell-disable-offline-update-dialog.patch bsc#944832 milachew@mail.lv -- Disable offline update suggestion before shutdown/reboot in SLE and openSUSE Leap.
Patch1011:      gnome-shell-disable-offline-update-dialog.patch
# PATCH-FEATURE-SLE gnome-shell-jscSLE9267-Remove-sessionList-of-endSessionDialog.patch jsc#SLE-9267 qkzhu@suse.com -- Remove sessionList of endSessionDialog
Patch1012:      gnome-shell-jscSLE9267-Remove-sessionList-of-endSessionDialog.patch
# PATCH-FIX-SLE gnome-shell-add-linkoption-dl.patch -- Need explicit -ldl build option with older gcc on SLE 15
Patch1013:      gnome-shell-add-linkoption-dl.patch

# needed for directory ownership
BuildRequires:  asciidoc
BuildRequires:  dbus-1
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gcr-4) >= 3.90.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.71.1
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.49.1
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 46.beta
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.19
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.13.2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.1
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.1
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(libmutter-%{mutter_api}) >= %{mutter_req}
BuildRequires:  pkgconfig(libnm) >= 1.10.4
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.11
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mutter-clutter-%{mutter_api}) >= %{mutter_req}
BuildRequires:  pkgconfig(mutter-cogl-%{mutter_api}) >= %{mutter_req}
BuildRequires:  pkgconfig(mutter-cogl-pango-%{mutter_api}) >= %{mutter_req}
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.100
BuildRequires:  pkgconfig(x11)
BuildRequires:  python(abi) >= 3
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gstreamer-plugin-pipewire
# "System settings" menu item
Requires:       gnome-control-center
Requires:       gnome-session
# For a GSettings schema and power system icon
Requires:       gnome-settings-daemon
# "High Contrast" in accessibility status icon
Requires:       gnome-themes-accessibility
Requires:       gsettings-desktop-schemas
# ScreenSaver needs this.
Requires:       gjs >= 1.71.1
Requires:       mutter >= %{mutter_req}
Requires:       typelib(Soup) = 3.0
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
Supplements:    (%{name} and evolution-data-server)

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
%autosetup -N
pushd subprojects
tar xf %{SOURCE1}
mv libgnome-volume-control-0.gitmodule gvc
popd
%patch -P 1 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1

%if 0%{?sle_version}
%patch -P 1001 -p1
%patch -P 1002 -p1
%patch -P 1003 -p1
%patch -P 1004 -p1
%patch -P 1007 -p1
%patch -P 1008 -p1
%patch -P 1009 -p1
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%patch -P 1010 -p1
%patch -P 1011 -p1
%endif
%patch -P 1012 -p1
%patch -P 1013 -p1
%endif

cp %{SOURCE100} data/theme/

%build
%meson \
	--libexecdir=%{_libexecdir}/%{name} \
	-D gtk_doc=true \
	-D man=true \
	-D networkmanager=true \
	-D systemd=true \
	-D tests=false \
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
%python3_fix_shebang

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/gnome-shell
%{_bindir}/gnome-extensions
%{_bindir}/gnome-shell-extension-prefs
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-test-tool
%dir %{_libdir}/gnome-shell
%dir %{_libexecdir}/gnome-shell
%exclude %{_libexecdir}/gnome-shell/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell/gnome-shell-portal-helper
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-%{mutter_api}.typelib
%{_libdir}/gnome-shell/St-%{mutter_api}.typelib
%{_libdir}/gnome-shell/libgnome-shell-menu.so
%{_libdir}/gnome-shell/libshell-%{mutter_api}.so
%{_libdir}/gnome-shell/libgvc.so
%{_libdir}/gnome-shell/libst-%{mutter_api}.so
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/glib-2.0/schemas/org.gnome.Extensions.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-launchers.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-screenshots.xml
# Own these dirs for extensions, search-providers and work around a race condition
%dir %{_datadir}/gnome-shell/extensions
%dir %{_datadir}/gnome-shell/search-providers
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/gnome-shell-dbus-interfaces.gresource
%{_datadir}/gnome-shell/gnome-shell-theme.gresource
%{_datadir}/gnome-shell/gnome-shell-osk-layouts.gresource
%{_datadir}/gnome-shell/perf-background.xml
%{_datadir}/gnome-shell/gnome-shell-icons.gresource
%{_mandir}/man?/gnome-shell.?%{ext_man}
%{_userunitdir}/org.gnome.Shell.target
%{_userunitdir}/org.gnome.Shell@wayland.service
%{_userunitdir}/org.gnome.Shell@x11.service
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override

%dir %{_libdir}/gnome-shell/girepository-1.0
%{_libdir}/gnome-shell/girepository-1.0/Shew-0.typelib

%{_libdir}/gnome-shell/libshew-0.so

%{_datadir}/dbus-1/services/org.gnome.Shell.Notifications.service
%{_datadir}/gnome-shell/org.gnome.Shell.Notifications
%{_datadir}/gnome-shell/org.gnome.Shell.Notifications.src.gresource

%{_datadir}/dbus-1/services/org.gnome.Shell.Screencast.service
%{_datadir}/gnome-shell/org.gnome.Shell.Screencast
%{_datadir}/gnome-shell/org.gnome.Shell.Screencast.src.gresource

%{_datadir}/dbus-1/services/org.gnome.ScreenSaver.service
%{_datadir}/gnome-shell/org.gnome.ScreenSaver
%{_datadir}/gnome-shell/org.gnome.ScreenSaver.src.gresource

%{_mandir}/man?/gnome-extensions.?%{ext_man}
%{_datadir}/bash-completion/completions/gnome-extensions
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg
%{_userunitdir}/org.gnome.Shell-disable-extensions.service
%{_datadir}/applications/org.gnome.Shell.Extensions.desktop
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.Extensions.service
%{_datadir}/gnome-shell/org.gnome.Shell.Extensions
%{_datadir}/gnome-shell/org.gnome.Shell.Extensions.src.gresource

%files devel
%doc %{_datadir}/doc/shell/
%doc %{_datadir}/doc/st/
%{_datadir}/gnome-shell/*.gir
%dir %{_datadir}/gnome-shell/gir-1.0
%{_datadir}/gnome-shell/gir-1.0/Shew-0.gir

%files calendar
%{_libexecdir}/gnome-shell/gnome-shell-calendar-server
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service

%files -n gnome-extensions
%{_bindir}/gnome-extensions-app
%{_datadir}/applications/org.gnome.Extensions.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
%{_datadir}/dbus-1/services/org.gnome.Extensions.service
%{_datadir}/gnome-shell/org.gnome.Extensions
%{_datadir}/gnome-shell/org.gnome.Extensions.data.gresource
%{_datadir}/gnome-shell/org.gnome.Extensions.src.gresource
%{_datadir}/metainfo/org.gnome.Extensions.metainfo.xml

%files lang -f %{name}.lang

%changelog
