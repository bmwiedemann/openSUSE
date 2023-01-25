#
# spec file for package goffice
#
# Copyright (c) 2023 SUSE LLC
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


Name:           goffice
Version:        0.10.54
Release:        0
Summary:        GLib/GTK+ Set of Document-Centric Objects and Utilities
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/GUI/GNOME
URL:            http://www.gnumeric.org/
Source:         https://download.gnome.org/sources/goffice/0.10/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  ghostscript-devel >= 9.06
BuildRequires:  intltool
BuildRequires:  libgsf-devel >= 1.14.24
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-pdf) >= 1.10.0
BuildRequires:  pkgconfig(cairo-ps) >= 1.10.0
BuildRequires:  pkgconfig(cairo-svg) >= 1.10.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.22.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.7
BuildRequires:  pkgconfig(lasem-0.4) >= 0.4.1
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.22.0
BuildRequires:  pkgconfig(libspectre) >= 0.2.6
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.12
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pango) >= 1.24.0
BuildRequires:  pkgconfig(pangocairo) >= 1.24.0

%description
GOffice is a GLib/GTK+ set of document-centric objects and utilities.

These are common operations for document-centric applications that are
conceptually simple, but complex to implement fully: plug-ins, load and
save documents, undo and redo.

%package -n libgoffice-0_10-10
Summary:        GLib/GTK+ Set of Document-Centric Objects and Utilities
# To make lang package installable
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgoffice-0_10-10
GOffice is a GLib/GTK+ set of document-centric objects and utilities.

These are common operations for document-centric applications that are
conceptually simple, but complex to implement fully: plug-ins, load and
save documents, undo and redo.

%if 0%{?suse_version} > 1210
%package -n typelib-1_0-GOffice-0_10
Summary:        Introspection bindings for GOffice
Group:          System/Libraries

%description -n typelib-1_0-GOffice-0_10
GOffice is a GLib/GTK+ set of document-centric objects and utilities.

This package provides the GObject Introspection bindings for GOffice.
%endif

%package devel
Summary:        Development files for GOffice
Group:          Development/Libraries/GNOME
Requires:       libgoffice-0_10-10 = %{version}
Obsoletes:      goffice-doc < %{version}
Provides:       goffice-doc = %{version}
%if 0%{?suse_version} > 1210
Requires:       typelib-1_0-GOffice-0_10 = %{version}
%endif

%description devel
GOffice is a GLib/GTK+ set of document-centric objects and utilities.

This package contains files needed to develop applications using
goffice.

%lang_package

%prep
%setup -q

%build
%configure \
    --disable-static\
    --enable-introspection
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Create directory for extern plugins
mkdir -p %{buildroot}%{_libdir}/goffice/0.10/plugins
%find_lang %{name}-%{version}
%fdupes %{buildroot}%{_datadir}

%post -n libgoffice-0_10-10 -p /sbin/ldconfig
%postun -n libgoffice-0_10-10 -p /sbin/ldconfig

%files -n libgoffice-0_10-10
%license COPYING COPYING-gpl2 COPYING-gpl3
%doc AUTHORS BUGS NEWS README
%{_libdir}/libgoffice-0.10.so.*
%dir %{_libdir}/goffice
%{_libdir}/goffice/%{version}/
%dir %{_datadir}/goffice
%{_datadir}/goffice/%{version}/
# Directory for external plugins
%dir %{_libdir}/goffice/0.10
%dir %{_libdir}/goffice/0.10/plugins

%files -n typelib-1_0-GOffice-0_10
%{_libdir}/girepository-1.0/GOffice-0.10.typelib

%files devel
%doc ChangeLog MAINTAINERS
%{_includedir}/libgoffice-0.10/
%{_libdir}/libgoffice-0.10.so
%{_libdir}/pkgconfig/libgoffice-0.10.pc
%{_datadir}/gir-1.0/GOffice-0.10.gir
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/goffice-0.10/

%files lang -f %{name}-%{version}.lang

%changelog
