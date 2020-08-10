#
# spec file for package budgie-desktop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2016 Ikey Doherty <ikey@solus-project.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           budgie-desktop
Version:        10.5.1
Release:        0
Summary:        GTK3 Desktop Environment
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://solus-project.com/budgie/
Source:         https://github.com/solus-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/solus-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM: Add support for mutter 3.36 gh#solus-project/budgie-desktop#1918
Patch:          support-libmutter6.patch
BuildRequires:  intltool
BuildRequires:  meson >= 0.41.2
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen) >= 0.28
Requires:       gnome-session
Requires:       gnome-settings-daemon
#Recommends:     gnome-screensaver
Recommends:     NetworkManager-applet
Recommends:     gnome-backgrounds
Recommends:     gnome-control-center
Recommends:     budgie-desktop-doc
BuildRequires:  (pkgconfig(libmutter-5) or pkgconfig(libmutter-6))
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(alsa)
%define vala_version %(rpm -q --queryformat='%%{VERSION}' vala | sed 's/\.[0-9]*$//g')

%description
Budgie Desktop is the flagship desktop for the Solus Operating System.

%package -n typelib-1_0-Budgie-1_0
Summary:        Introspection bindings for the Budgie Desktop
Group:          System/Libraries 
Requires:       %{name} = %{version}-%{release}

%description -n typelib-1_0-Budgie-1_0
This package provides GObject Introspection files required for
developing Budgie Applets using interpreted languages, such as Python
GObject Introspection bindings.

%package devel
Summary:        Development files for the Budgie Desktop
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}-%{release}
Requires:       typelib-1_0-Budgie-1_0 = %{version}-%{release}

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
%meson
%meson_build

%install
export LANG=en_US.UTF-8
%meson_install

# GNOME Screensaver missing in openSUSE
rm %{buildroot}/%{_sysconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop

# Correct vala directory
mkdir -pv %{buildroot}%{_datadir}/vala-%{vala_version}/
mv %{buildroot}%{_datadir}/vala/* %{buildroot}%{_datadir}/vala-%{vala_version}/
rm -Rf %{buildroot}%{_datadir}/vala/

%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_post
%icon_theme_cache_postun
%endif

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
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_bindir}/budgie-*
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop/
%{_sysconfdir}/xdg/autostart/budgie-desktop-nm-applet.desktop

%files -n libraven0
%{_libdir}/libraven.so.*

%files -n libbudgietheme0
%{_libdir}/libbudgietheme.so.*

%files -n libbudgie-plugin0
%{_libdir}/libbudgie-plugin.so.*

%files -n libbudgie-private0
%{_libdir}/libbudgie-private.so.*

%files devel
%dir %{_includedir}/budgie-desktop
%{_includedir}/budgie-desktop/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala-%{vala_version}/vapi/budgie-1.0.*

%files -n typelib-1_0-Budgie-1_0
%{_libdir}/girepository-1.0/Budgie-1.0.typelib

%files doc
%{_datadir}/gtk-doc/html/budgie-desktop/

%files lang -f %{name}.lang

%changelog
