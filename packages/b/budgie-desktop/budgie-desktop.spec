#
# spec file for package budgie-desktop
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013-2016 Ikey Doherty <ikey@solus-project.com>
# Copyright (c) 2021 Callum Farmer <gmbr3@opensuse.org>
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


%if 0%{?suse_version} < 1550
%define _distconfdir %{_sysconfdir}
%endif
Name:           budgie-desktop
Version:        10.7.1+20
Release:        0
Summary:        GTK3 Desktop Environment
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-desktop
Source0:        %{name}-%{version}.tar.xz
# Solus stupid 1000
BuildRequires:  budgie-screensaver
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 41.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  (pkgconfig(libmutter-12) or pkgconfig(libmutter-11) or pkgconfig(libmutter-10))
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
# flatpak/snap
Recommends:     (xdg-desktop-portal-gnome if (flatpak or snapd))
# https://discuss.getsol.us/d/6970-cant-lock-my-screen/3
Conflicts:      gnome-shell
#
# rebrand and gnome porting
Requires:       budgie-desktop-view >= 1.2.1+0
Requires:       budgie-screensaver >= 5.1.0+0
Requires:       typelib-1_0-Budgie-1_0 >= %{version}
Requires:       typelib-1_0-BudgieRaven-1_0 >= %{version}
Requires:       budgie-desktop-branding >= 20220627.1
Requires:       budgie-control-center >= 1.2.0+0
#
# unchanged SOVER but new APIs
Requires:       libraven0 >= %{version}
Requires:       libbudgietheme0 >= %{version}
Requires:       libbudgie-plugin0 >= %{version}
Requires:       libbudgie-private0 >= %{version}
Requires:       libbudgie-appindexer0 >= %{version}
Requires:       libbudgie-raven-plugin0 >= %{version}
#
Requires:       gnome-session-core
Requires:       gnome-settings-daemon
Requires:       gnome-bluetooth = 3.34.5
Requires:       ibus
Requires:       libgnomesu
Requires:       xdg-user-dirs-gtk
Requires:       NetworkManager-applet
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
Budgie Desktop is the flagship desktop for the Solus Operating System.

%package -n typelib-1_0-Budgie-1_0
Summary:        Main Introspection bindings for the Budgie Desktop
Group:          System/Libraries
Requires:       typelib-1_0-PeasGtk-1_0

%description -n typelib-1_0-Budgie-1_0
This package provides GObject Introspection files required for
developing Budgie Applets using interpreted languages, such as Python
GObject Introspection bindings.

%package -n typelib-1_0-BudgieRaven-1_0
Summary:        Raven Introspection bindings for the Budgie Desktop
Group:          System/Libraries

%description -n typelib-1_0-BudgieRaven-1_0
This package provides GObject Introspection files required for
developing Budgie Raven plugins using interpreted languages, such as Python
GObject Introspection bindings.

%package devel
Summary:        Development files for the Budgie Desktop
Group:          Development/Libraries/GNOME
Requires:       libraven0 = %{version}
Requires:       libbudgietheme0 = %{version}
Requires:       libbudgie-plugin0 = %{version}
Requires:       libbudgie-private0 = %{version}
Requires:       libbudgie-appindexer0 = %{version}
Requires:       libbudgie-raven-plugin0 = %{version}

%description devel
This package provides development files required for software to be
able to use and link against the Budgie APIs, to create their own
applets for the Budgie Panel.

%package doc
Summary:        Documentation files for the Budgie Desktop
Group:          Documentation/HTML
Supplements:    (budgie-desktop and patterns-base-documentation)

%description doc
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.

%package -n libraven0
Summary:        Shared library for Raven
Group:          System/Libraries

%description -n libraven0
Budgie Desktop Notification Center.

%package -n libbudgietheme0
Summary:        Shared library for Budgie theming
Group:          System/Libraries

%description -n libbudgietheme0
Budgie theming engine shared library package.

%package -n libbudgie-plugin0
Summary:        Shared library for Budgie plugins
Group:          System/Libraries

%description -n libbudgie-plugin0
Shared library for budgie plugins to link against.

%package -n libbudgie-private0
Summary:        Private library for Budgie
Group:          System/Libraries

%description -n libbudgie-private0
Private library for Budgie desktop to link against.

%package -n libbudgie-appindexer0
Summary:        Private library for Budgie Menu
Group:          System/Libraries

%description -n libbudgie-appindexer0
Private library for Budgie menu to link against.

%package -n libbudgie-raven-plugin0
Summary:        Shared library for Budgie raven plugins
Group:          System/Libraries

%description -n libbudgie-raven-plugin0
Shared library for budgie raven plugins to link against.

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -Wno-pedantic"
%meson -Dc_std=none -Dxdg-appdir=%{_sysconfdir}/xdg/autostart
%meson_build

%install
%meson_install

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

rm %{buildroot}%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.BudgieDesktopScreensaver.desktop

%find_lang %{name}

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop 20

%postun
[ -f %{_datadir}/xsessions/budgie-desktop.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop

%ldconfig_scriptlets -n libraven0
%ldconfig_scriptlets -n libbudgietheme0
%ldconfig_scriptlets -n libbudgie-plugin0
%ldconfig_scriptlets -n libbudgie-private0
%ldconfig_scriptlets -n libbudgie-appindexer0
%ldconfig_scriptlets -n libbudgie-raven-plugin0

%files
%license LICENSE LICENSE.LGPL2.1
%{_bindir}/budgie-*
%{_bindir}/org.buddiesofbudgie*
%{_libexecdir}/budgie-desktop
%{_mandir}/man1/*%{?ext_man}
%{_datadir}/budgie
%{_datadir}/applications/*.desktop
%{_datadir}/backgrounds
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/glib-2.0/schemas/*.gschema.override
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/gnome-session
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop
%{_sysconfdir}/xdg/autostart/*.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop

%files -n libraven0
%{_libdir}/libraven.so.*

%files -n libbudgietheme0
%{_libdir}/libbudgietheme.so.*

%files -n libbudgie-plugin0
%dir %{_libdir}/budgie-desktop
%dir %{_libdir}/budgie-desktop/plugins
%{_libdir}/libbudgie-plugin.so.*

%files -n libbudgie-private0
%{_libdir}/libbudgie-private.so.*

%files -n libbudgie-appindexer0
%{_libdir}/libbudgie-appindexer.so.*

%files -n libbudgie-raven-plugin0
%{_libdir}/libbudgie-raven-plugin.so.*

%files devel
%{_includedir}/budgie-desktop
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/gir-1.0/BudgieRaven-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*
%{_datadir}/vala/vapi/budgie-raven-plugin-1.0.*

%files -n typelib-1_0-Budgie-1_0
%{_libdir}/girepository-1.0/Budgie-1.0.typelib

%files -n typelib-1_0-BudgieRaven-1_0
%{_libdir}/girepository-1.0/BudgieRaven-1.0.typelib

%files doc
%{_datadir}/gtk-doc/html/budgie-desktop

%files lang -f %{name}.lang

%changelog
