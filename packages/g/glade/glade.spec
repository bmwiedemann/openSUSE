#
# spec file for package glade
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


%define soname libgladeui-2-13

Name:           glade
Version:        3.40.0
Release:        0
Summary:        User Interface Builder for GTK+ 3
License:        GPL-2.0-or-later
Group:          Development/Tools/GUI Builders
URL:            https://glade.gnome.org/
Source0:        https://download.gnome.org/sources/glade/3.40/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.64.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.8.0
# Disable webkitgtk catalog support - pulls in soup2
#BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.28.0

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

%package docs
Summary:        Documentation for GLADE User Interface Builder
BuildArch:      noarch

%description docs
Glade is a RAD tool to develop user interfaces for the Gtk+ 3 toolkit
and the GNOME desktop environment.

This package contains the documentation for Glade.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D gtk_doc=true \
	-D webkit2gtk=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n %{soname}

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
%{_datadir}/gettext/its/glade-catalog.its
%{_datadir}/gettext/its/glade-catalog.loc
%{_datadir}/icons/hicolor/*/apps/*.*
%{_libdir}/glade/modules/libgladegjs.so
%{_libdir}/glade/modules/libgladegtk.so
%{_libdir}/glade/modules/libgladepython.so
# Disable webkitgtk catalog support - pulls in soup2
#%%{_libdir}/glade/modules/libgladewebkit2gtk.so
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
%doc AUTHORS TODO
%{_includedir}/libgladeui-2.0/
%{_libdir}/pkgconfig/gladeui-2.0.pc
%{_libdir}/libgladeui*.so
%{_datadir}/gir-1.0/*.gir

%files lang -f %{name}.lang

%files docs
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gladeui-2

%changelog
