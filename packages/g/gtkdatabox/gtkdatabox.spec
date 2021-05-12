#
# spec file for package gtkdatabox
#
# Copyright (c) 2021 SUSE LLC
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


%define libver 1
Name:           gtkdatabox
Version:        1.0.0
Release:        0
Summary:        GTK+-3 widget for fast data display
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/gtkdatabox
Source0:        %{URL}/files/gtkdatabox-1/%{name}-%{version}.tar.gz
BuildRequires:  gtk-doc >= 1.14
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4

%description
GtkDatabox is a widget for the Gtk+-3 library designed to display large
amounts of numerical data fast and easy.

%package devel
Summary:        Development files for GtkDatabox
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libver} = %{version}
Suggests:       glade-catalog-%{name} = %{version}
# Conflict with GTK-2 version, which is named like this
Conflicts:      lib%{name}-devel

%description devel
The libgtkdatabox-devel package contains libraries, header files and
documentation for developing applications that use libgtkdatabox.

%package devel-examples
Summary:        Example code for using the library
Requires:       %{name}-devel = %{version}

%description devel-examples
GtkDatabox is a widget for the Gtk+-3 library designed to display large
amounts of numerical data fast and easy.
This package contains some example code for developing using GTKDataBox.

%package gtk-doc
Summary:        Documentation for GTKDataBox

%description gtk-doc
GtkDatabox is a widget for the Gtk+-3 library designed to display large
amounts of numerical data fast and easy.

%package -n glade-catalog-%{name}
Summary:        Glade catalog for GTKDataBox
Enhances:       glade >= 3.0

%description -n glade-catalog-%{name}
GtkDatabox is a widget for the Gtk+-3 library designed to display large
amounts of numerical data fast and easy.

%package -n lib%{name}%{libver}
Summary:        GTK+ widget for fast data display

%description -n lib%{name}%{libver}
GtkDatabox is a widget for the Gtk+-3 library designed to display large
amounts of numerical data fast and easy.

%prep
%setup -q

%build
autoreconf -fi
%configure \
  --disable-static \
  --enable-gtk-doc \
  --enable-glade
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files -n lib%{name}%{libver}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README TODO
%doc examples/*.c
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/gtkdatabox.pc

%files devel-examples
%doc examples/*.c

%files gtk-doc
%doc %{_datadir}/gtk-doc/html/gtkdatabox-1

%files -n glade-catalog-%{name}
%{_datadir}/glade/catalogs/gtkdatabox.xml
%{_libdir}/glade/modules/libgladedatabox.so
%{_datadir}/icons/hicolor/scalable/apps/widget-gladedatabox-gtk_databox*.svg

%changelog
