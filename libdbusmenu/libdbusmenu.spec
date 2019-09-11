#
# spec file for package libdbusmenu
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname_glib 4
%define soname_gtk2 4
%define soname_gtk3 4
%define soname_jsonloader 4
Name:           libdbusmenu
Version:        16.04.0
Release:        0
Summary:        Small library that passes a menu structure across DBus
License:        GPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
Group:          System/Libraries
URL:            https://launchpad.net/dbusmenu
Source:         https://launchpad.net/libdbusmenu/16.04/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(x11)

%description
A small little library that was created by pulling out some common
code out of mate-indicator-applet. It passes a menu structure
across D-Bus so that a program can create a menu simply without
worrying about how it is displayed on the other side of the bus.

%package tools
Summary:        Development tools for the dbusmenu libraries
Group:          Development/Tools/Other
Requires:       %{name}-glib%{soname_glib} = %{version}

%description tools
This packages contains the development tools for the dbusmenu libraries.

%package glib%{soname_glib}
Summary:        Small library that passes a menu structure across D-Bus
Group:          System/Libraries

%description glib%{soname_glib}
This package contains the shared libraries for the dbusmenu-glib library.

%package -n typelib-1_0-Dbusmenu-0_4
Summary:        Small library that passes a menu structure across D-Bus -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Dbusmenu-0_4
This package contains the GObject Introspection bindings for the dbusmenu
library.

%package glib-devel
Summary:        Development files for libdbusmenu-glib
Group:          Development/Libraries/C and C++
Requires:       %{name}-glib%{soname_glib} = %{version}
Requires:       pkgconfig(dbus-glib-1)

%description glib-devel
This package contains the development files for the dbusmenu-glib library.

%package glib-doc
Summary:        Documentation for libdbusmenu-glib%{soname_glib}
Group:          Documentation/HTML
BuildArch:      noarch

%description glib-doc
This package includes the documentation for the dbusmenu-glib library.

%package gtk%{soname_gtk2}
Summary:        Small library that passes a menu structure across D-Bus -- GTK+ 2 version
Group:          System/Libraries
Requires:       gtk2

%description gtk%{soname_gtk2}
This package contains the shared libraries for the dbusmenu-gtk2 library.

%package -n typelib-1_0-DbusmenuGtk-0_4
Summary:        Small library that passes a menu structure across D-Bus -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-DbusmenuGtk-0_4
This package contains the GObject Introspection bindings for the GTK+ 2 version
of the dbusmenu-gtk library.

%package gtk-devel
Summary:        Development files for libdbusmenu-gtk%{soname_gtk2}
Group:          Development/Libraries/C and C++
Requires:       %{name}-glib-devel = %{version}
Requires:       %{name}-gtk%{soname_gtk2} = %{version}
Requires:       pkgconfig(dbus-glib-1)
Requires:       pkgconfig(gtk+-2.0)

%description gtk-devel
This package contains the development files for the dbusmenu-gtk2 library.

%package gtk3-%{soname_gtk3}
Summary:        Small library that passes a menu structure across DBus -- GTK+ 3 version
Group:          System/Libraries

%description gtk3-%{soname_gtk3}
This package contains the shared libraries for the dbusmenu-gtk3 library.

%package -n typelib-1_0-DbusmenuGtk3-0_4
Summary:        Small library that passes a menu structure across D-Bus -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-DbusmenuGtk3-0_4
This package contains the GObject Introspection bindings for the GTK+ 3 version
of the dbusmenu-gtk library.

%package gtk3-devel
Summary:        Development files for libdbusmenu-gtk3-%{soname_gtk3}
Group:          Development/Libraries/C and C++
Requires:       %{name}-glib-devel = %{version}
Requires:       %{name}-gtk3-%{soname_gtk3} = %{version}
Requires:       pkgconfig(dbus-glib-1)
Requires:       pkgconfig(gtk+-3.0)

%description gtk3-devel
This package contains the development files for the dbusmenu-gtk3 library.

%package gtk-doc
Summary:        Documentation for libdbusmenu-gtk%{soname_gtk2} and libdbusmenu-gtk3-%{soname_gtk3}
Group:          Documentation/HTML
BuildArch:      noarch

%description gtk-doc
This package contains the documentation for the dbusmenu-gtk2 and dbusmenu-gtk3
libraries.

%package jsonloader%{soname_jsonloader}
Summary:        Small library that passes a menu structure across DBus -- Test library
Group:          System/Libraries

%description jsonloader%{soname_jsonloader}
This package contains the shared libraries for dbusmenu-jsonloader, a library
meant for test suites.

%package jsonloader-devel
Summary:        Development files for libdbusmenu-jsonloader%{soname_jsonloader}
Group:          Development/Libraries/C and C++
Requires:       %{name}-glib-devel = %{version}
Requires:       %{name}-jsonloader%{soname_jsonloader} = %{version}
Requires:       pkgconfig(dbus-glib-1)
Requires:       pkgconfig(json-glib-1.0)

%description jsonloader-devel
This package contains the development files for the dbusmenu-jsonloader library.

%prep
%setup -q

%build
%global _configure ../configure
NOCONFIGURE=1 gnome-autogen.sh --enable-gtk-doc
for ver in 2 3; do
    mkdir build-gtk$ver
    pushd build-gtk$ver
    %configure \
      --disable-static       \
      --disable-scrollkeeper \
      --enable-gtk-doc       \
      --enable-introspection \
      --with-gtk=$ver
    make %{?_smp_mflags}
    popd
done

%install
for ver in 2 3; do
    pushd build-gtk$ver
    %make_install
    popd
done

find %{buildroot} -type f -name "*.la" -delete -print

# Put documentation in correct directory.
mkdir -p %{buildroot}%{_docdir}/%{name}-tools/
mv -f %{buildroot}%{_datadir}/doc/%{name}/README.dbusmenu-bench \
  %{buildroot}%{_docdir}/%{name}-tools/

# Put examples in correct documentation directory.
mkdir -p %{buildroot}%{_docdir}/%{name}-glib-devel/examples/
mv -f %{buildroot}%{_datadir}/doc/%{name}/examples/glib-server-nomenu.c \
  %{buildroot}%{_docdir}/%{name}-glib-devel/examples/

%post glib%{soname_glib} -p /sbin/ldconfig
%postun glib%{soname_glib} -p /sbin/ldconfig
%post gtk%{soname_gtk2} -p /sbin/ldconfig
%postun gtk%{soname_gtk2} -p /sbin/ldconfig
%post gtk3-%{soname_gtk3} -p /sbin/ldconfig
%postun gtk3-%{soname_gtk3} -p /sbin/ldconfig
%post jsonloader%{soname_jsonloader} -p /sbin/ldconfig
%postun jsonloader%{soname_jsonloader} -p /sbin/ldconfig

%files tools
%license COPYING*
%doc NEWS
%{_libexecdir}/dbusmenu-bench
%{_libexecdir}/dbusmenu-dumper
%{_libexecdir}/dbusmenu-testapp
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/json/
%{_datadir}/%{name}/json/test-gtk-label.json
%doc %dir %{_docdir}/%{name}-tools/
%doc %{_docdir}/%{name}-tools/README.dbusmenu-bench

%files glib%{soname_glib}
%license COPYING*
%doc NEWS
%{_libdir}/libdbusmenu-glib.so.%{soname_glib}*

%files -n typelib-1_0-Dbusmenu-0_4
%license COPYING*
%doc NEWS
%{_libdir}/girepository-1.0/Dbusmenu-0.4.typelib

%files glib-devel
%license COPYING*
%doc NEWS
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/client.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/dbusmenu-glib.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/enum-types.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/menuitem-proxy.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/menuitem.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/server.h
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-glib/types.h
%{_libdir}/pkgconfig/dbusmenu-glib-0.4.pc
%{_libdir}/libdbusmenu-glib.so
%{_datadir}/gir-1.0/Dbusmenu-0.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/Dbusmenu-0.4.vapi
%doc %dir %{_docdir}/%{name}-glib-devel/
%doc %dir %{_docdir}/%{name}-glib-devel/examples/
%doc %{_docdir}/%{name}-glib-devel/examples/glib-server-nomenu.c

%files glib-doc
%license COPYING*
%doc NEWS
%doc %{_datadir}/gtk-doc/html/libdbusmenu-glib/

%files gtk%{soname_gtk2}
%license COPYING*
%doc NEWS
%{_libdir}/libdbusmenu-gtk.so.%{soname_gtk2}*

%files -n typelib-1_0-DbusmenuGtk-0_4
%license COPYING*
%doc NEWS
%{_libdir}/girepository-1.0/DbusmenuGtk-0.4.typelib

%files gtk-devel
%license COPYING*
%doc NEWS
%dir %{_includedir}/libdbusmenu-gtk-0.4/
%dir %{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/client.h
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/dbusmenu-gtk.h
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/menu.h
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/menuitem.h
%{_includedir}/libdbusmenu-gtk-0.4/libdbusmenu-gtk/parser.h
%{_libdir}/pkgconfig/dbusmenu-gtk-0.4.pc
%{_libdir}/libdbusmenu-gtk.so
%{_datadir}/gir-1.0/DbusmenuGtk-0.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/DbusmenuGtk-0.4.vapi

%files gtk3-%{soname_gtk3}
%license COPYING*
%doc NEWS
%{_libdir}/libdbusmenu-gtk3.so.%{soname_gtk3}*

%files -n typelib-1_0-DbusmenuGtk3-0_4
%license COPYING*
%doc NEWS
%{_libdir}/girepository-1.0/DbusmenuGtk3-0.4.typelib

%files gtk3-devel
%license COPYING*
%doc NEWS
%dir %{_includedir}/libdbusmenu-gtk3-0.4/
%dir %{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/client.h
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/dbusmenu-gtk.h
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/menu.h
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/menuitem.h
%{_includedir}/libdbusmenu-gtk3-0.4/libdbusmenu-gtk/parser.h
%{_libdir}/pkgconfig/dbusmenu-gtk3-0.4.pc
%{_libdir}/libdbusmenu-gtk3.so
%{_datadir}/gir-1.0/DbusmenuGtk3-0.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/DbusmenuGtk3-0.4.vapi

%files gtk-doc
%license COPYING*
%doc NEWS
%doc %{_datadir}/gtk-doc/html/libdbusmenu-gtk/

%files jsonloader%{soname_jsonloader}
%license COPYING*
%doc NEWS
%{_libdir}/libdbusmenu-jsonloader.so.%{soname_jsonloader}*

%files jsonloader-devel
%license COPYING*
%doc NEWS
%dir %{_includedir}/libdbusmenu-glib-0.4/
%dir %{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/
%{_includedir}/libdbusmenu-glib-0.4/libdbusmenu-jsonloader/json-loader.h
%{_libdir}/pkgconfig/dbusmenu-jsonloader-0.4.pc
%{_libdir}/libdbusmenu-jsonloader.so

%changelog
