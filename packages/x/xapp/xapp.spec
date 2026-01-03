#
# spec file for package xapp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         sover   1
%define         typelib typelib-1_0-XApp-1_0
Name:           xapp
Version:        3.2.1
Release:        0
Summary:        Library files for the Xapp ecosystem
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/xapp
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
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
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(xkbfile)

%description
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

%package -n lib%{name}%{sover}
Summary:        XApp library
License:        GPL-2.0-or-later
Requires:       %{name}-common

%description -n lib%{name}%{sover}
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This library is used by several XApp applications.

%package -n %{typelib}
Summary:        XApp library -- Introspection bindings
License:        GPL-2.0-or-later

%description -n %{typelib}
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This library is used by several XApp applications.

%package -n lib%{name}-devel
Summary:        Development files of libxapp
License:        GPL-2.0-or-later
Requires:       %{typelib} = %{version}
Requires:       lib%{name}%{sover} = %{version}
Requires:       pkgconfig(xkbfile)

%description -n lib%{name}-devel
The libxapp development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libxapp.

%package common
Summary:        Common files for XApp desktop applications
License:        GPL-2.0-or-later AND GPL-3.0-only
BuildArch:      noarch
Provides:       xapps-common = %{version}
Obsoletes:      xapps-common < %{version}

%description common
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This package includes files that are shared between several XApp
applications (i18n files and configuration schemas).

%package        mate
Summary:        Mate status applet with HIDPI support
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       lib%{name}%{sover} = %{version}
Provides:       xapps-mate = %{version}
Obsoletes:      xapps-mate < %{version}

%description    mate
Mate status applet with HIDPI support

%lang_package -n %{name}-common

%prep
%autosetup

%build
%meson \
  -Ddocs=true \
  -Ddeprecated_warnings=true \
  -Dstatus-notifier=true \
  -Dapp-lib-only=false \
  -Ddebian_derivative=false \
  -Dmate=true \
  -Dxfce=true
%meson_build

%install
%meson_install

# remove unnecessary binaries
rm -f %{buildroot}%{_bindir}/{pastebin,upload-system-info}

%if %{?suse_version} >= 1600
# install xdg autostart file in /usr/etc
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%endif

%fdupes %{buildroot}
%find_lang %{name}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license COPYING COPYING.LESSER
%doc ChangeLog README.md
%dir %{_libdir}/%{name}s
%{_libdir}/lib%{name}.so.%{sover}*
%{_libdir}/libxapp.so.%{version}
%{_libdir}/xapps/xapp-sn-watcher

%files -n %{typelib}
%{_libdir}/girepository-1.0/XApp-1.0.typelib
%{python3_sitearch}/gi/overrides/XApp.py

%files -n lib%{name}-devel
%{_includedir}/xapp/
%{_libdir}/lib%{name}.so
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
%if %{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%else
%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%endif
%{_sysconfdir}/X11/xinit/xinitrc.d/80xapp-gtk3-module.sh
%{_bindir}/xfce4-set-wallpaper
%{_bindir}/xapp-gpu-offload
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service

%files mate
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_libexecdir}/xapps/
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%files common-lang -f xapp.lang

%changelog
