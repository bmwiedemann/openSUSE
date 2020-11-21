#
# spec file for package glade
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


%define soname libgladeui-2-12

Name:           glade
Version:        3.36.0
Release:        0
Summary:        User Interface Builder for GTK+ 3
License:        GPL-2.0-or-later
Group:          Development/Tools/GUI Builders
URL:            https://glade.gnome.org/
Source0:        https://download.gnome.org/sources/glade/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.53.2
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.8.0
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.12.0

%description
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

%package -n %{soname}
Summary:        Core library of the GLADE User Interface Builder
Group:          System/Libraries

%description -n %{soname}
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

%package -n typelib-1_0-Gladeui-2_0
Summary:        Introspection bindins for libgladeui
Group:          System/Libraries

%description -n typelib-1_0-Gladeui-2_0
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

This package provides the GObject Introspection bindings for the
libgladeui library.

%package -n libgladeui-2-devel
Summary:        Development files for libgladeui
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       typelib-1_0-Gladeui-2_0 = %{version}
# The gtk-doc documentation is not parallel installable (bnc#646997)
Conflicts:      libgladeui-1-devel

%description -n libgladeui-2-devel
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

This subpackage contains the header files for developing
applications that want to make use of libgladeui.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-man-pages \
	PYTHON=python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files
%license COPYING COPYING.GPL COPYING.LGPL
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/glade
%{_bindir}/glade-previewer
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Glade.appdata.xml
%{_datadir}/applications/org.gnome.Glade.desktop
%{_datadir}/glade/
%{_datadir}/icons/hicolor/*/apps/*.*
%{_libdir}/glade/modules/libgladegtk.so
%{_libdir}/glade/modules/libgladepython.so
%{_libdir}/glade/modules/libgladewebkit2gtk.so
%{_mandir}/man1/glade-previewer.1%{?ext_man}
%{_mandir}/man1/glade.1%{?ext_man}

%files -n %{soname}
%{_libdir}/libgladeui*.so.*
# These directories are needed by third-party catalogs, and are explicitly
# referenced in the pkg-config file, so it makes sense to own them here
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%dir %{_datadir}/glade/pixmaps
%dir %{_datadir}/glade/pixmaps/hicolor
%dir %{_datadir}/glade/pixmaps/hicolor/*
%dir %{_datadir}/glade/pixmaps/hicolor/*/actions
%dir %{_libdir}/glade
%dir %{_libdir}/glade/modules

%files -n typelib-1_0-Gladeui-2_0
%{_libdir}/girepository-1.0/Gladeui-2.0.typelib

%files -n libgladeui-2-devel
%doc AUTHORS ChangeLog TODO
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/gladeui-2
%{_includedir}/libgladeui-2.0/
%{_libdir}/pkgconfig/gladeui-2.0.pc
%{_libdir}/libgladeui*.so
%{_datadir}/gir-1.0/*.gir

%files lang -f %{name}.lang

%changelog
