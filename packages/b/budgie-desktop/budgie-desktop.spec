#
# spec file for package budgie-desktop
#
# Copyright (c) 2021 SUSE LLC
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


#
Name:           budgie-desktop
Version:        10.5.2+08c9d7cf
Release:        0
Summary:        GTK3 Desktop Environment
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://getsol.us/solus/experiences/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE: Create a clean separation between Budgie and GNOME desktops
Patch0:         desktop-override.patch
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  (pkgconfig(libmutter-6) or pkgconfig(libmutter-7) or pkgconfig(libmutter-8))
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
Requires:       budgie-screensaver
Requires:       gnome-control-center
Requires:       gnome-session-core
Requires:       gnome-settings-daemon
Requires:       ibus
Recommends:     NetworkManager-applet
Recommends:     budgie-desktop-doc
Recommends:     gnome-backgrounds
Recommends:     gnome-software

%description
Budgie Desktop is the flagship desktop for the Solus Operating System.

%package -n typelib-1_0-Budgie-1_0
Summary:        Introspection bindings for the Budgie Desktop
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       typelib(PeasGtk) = 1.0

%description -n typelib-1_0-Budgie-1_0
This package provides GObject Introspection files required for
developing Budgie Applets using interpreted languages, such as Python
GObject Introspection bindings.

%package devel
Summary:        Development files for the Budgie Desktop
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}-%{release}
Requires:       typelib(Budgie) = 1.0

%description devel
This package provides development files required for software to be
able to use and link against the Budgie APIs, to create their own
applets for the Budgie Panel.

%package doc
Summary:        Documentation files for the Budgie Desktop
Group:          Documentation/HTML

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

%lang_package

%prep
%autosetup -p1

%build
%meson -Dxdg-appdir=%{_distconfdir}/xdg/autostart
%meson_build

%install
%meson_install

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%find_lang %{name}

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop 20

%postun
[ -f %{_datadir}/xsessions/budgie-desktop.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop

%post   -n libraven0 -p /sbin/ldconfig
%postun -n libraven0 -p /sbin/ldconfig
%post   -n libbudgietheme0 -p /sbin/ldconfig
%postun -n libbudgietheme0 -p /sbin/ldconfig
%post   -n libbudgie-plugin0 -p /sbin/ldconfig
%postun -n libbudgie-plugin0 -p /sbin/ldconfig
%post   -n libbudgie-private0 -p /sbin/ldconfig
%postun -n libbudgie-private0 -p /sbin/ldconfig

%files
%license LICENSE LICENSE.LGPL2.1
%{_datadir}/gnome-session
%{_bindir}/budgie-*
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop
%{_distconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop
%{_distconfdir}/xdg/autostart/budgie-desktop-nm-applet.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop

%files -n libraven0
%{_libdir}/libraven.so.*

%files -n libbudgietheme0
%{_libdir}/libbudgietheme.so.*

%files -n libbudgie-plugin0
%{_libdir}/libbudgie-plugin.so.*

%files -n libbudgie-private0
%{_libdir}/libbudgie-private.so.*

%files devel
%{_includedir}/budgie-desktop
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*

%files -n typelib-1_0-Budgie-1_0
%{_libdir}/girepository-1.0/Budgie-1.0.typelib

%files doc
%{_datadir}/gtk-doc/html/budgie-desktop

%files lang -f %{name}.lang

%changelog
