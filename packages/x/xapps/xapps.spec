#
# spec file for package xapps
#
# Copyright (c) 2022 SUSE LLC
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


%define typelib typelib-1_0-XApp-1_0
%define soname  libxapp
%define sover   1
Name:           xapps
Version:        2.4.1
Release:        0
Summary:        XApp library and common files
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/xapps
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/xapp-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  vala
BuildRequires:  xinit
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.22.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.37.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.37.3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(xkbfile)
%glib2_gsettings_schema_requires

%description
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

%package -n %{soname}%{sover}
Summary:        XApp library
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{name}-common

%description -n %{soname}%{sover}
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This library is used by several XApp applications.

%package -n %{typelib}
Summary:        XApp library -- Introspection bindings
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{typelib}
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This library is used by several XApp applications.

%package -n %{soname}-devel
Summary:        Development files of libxapp
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(xkbfile)

%description -n %{soname}-devel
The libxapp development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libxapp.

%package common
Summary:        Common files for XApp desktop applications
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          System/GUI/Other
Recommends:     %{name}-common-lang
BuildArch:      noarch

%description common
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This package includes files that are shared between several XApp
applications (i18n files and configuration schemas).

%package        mate
Summary:        Mate status applet with HIDPI support
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       %{soname}%{sover} = %{version}

%description    mate
Mate status applet with HIDPI support

%lang_package -n %{name}-common

%prep
%setup -q -n xapp-%{version}

%build
python3 -c 'import gi;print(gi._overridesdir)'
%meson \
  -Ddocs=true
%meson_build

%install
%meson_install

rm %{buildroot}%{_bindir}/{pastebin,upload-system-info}
%fdupes %{buildroot}%{_datadir}/icons/
%fdupes %{buildroot}%{python_sitearch}/ %{buildroot}%{python3_sitearch}/
%find_lang xapp

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post common
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files -n %{soname}%{sover}
%license debian/copyright
%doc debian/changelog
%{_libdir}/%{soname}.so.%{sover}*
%{_libdir}/libxapp.so.%{version}

%files -n %{typelib}
%{_libdir}/girepository-1.0/XApp-1.0.typelib
%{python3_sitearch}/gi/overrides/XApp.py

%files -n %{soname}-devel
%{_includedir}/xapp/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/xapp.pc
%{_datadir}/gir-1.0/XApp-1.0.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/xapp.*
%dir %{_datadir}/glade/
%dir %{_datadir}/glade/catalogs/
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml
%{_datadir}/gtk-doc/html/libxapp/
%{_libdir}/gtk-3.0/modules/libxapp-gtk3-module.so

%files common
%license debian/copyright
%doc debian/changelog
%dir %{_sysconfdir}/X11/xinit/
%dir %{_sysconfdir}/X11/xinit/xinitrc.d/
%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%{_sysconfdir}/X11/xinit/xinitrc.d/80xapp-gtk3-module.sh
%{_bindir}/xfce4-set-wallpaper
%{_datadir}/icons/hicolor/*/actions/*.*
%{_datadir}/icons/hicolor/*/categories/*.*
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service
%{_datadir}/icons/hicolor/scalable/emblems/emblem-xapp-favorite.svg
%{_datadir}/icons/hicolor/scalable/*/xapp-*.svg

%files mate
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_libexecdir}/xapps/
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%files common-lang -f xapp.lang

%changelog
