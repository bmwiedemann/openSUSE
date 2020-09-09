#
# spec file for package gspell
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


%define shlib lib%{name}-1-2
Name:           gspell
Version:        1.8.4
Release:        0
Summary:        A spell checker library for GTK+ applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/gspell
Source0:        https://download.gnome.org/sources/gspell/1.8/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc >= 1.25
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enchant-2) >= 2.1.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(iso-codes) >= 0.35
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(vapigen)

%description
gspell provides a flexible API to implement the spell checking in a GTK+
application.

%package -n %{shlib}
Summary:        Spell checker library for GTK+
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{shlib}
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the shared libraries for gspell.

%package -n typelib-1_0-Gspell-1
Summary:        Introspection bindings for the GTK+ spell checker library
# typelib name was wrong until version 1.7.1; obsolete to ease upgrade path
Group:          System/Libraries
Obsoletes:      typelib-1_0-Gspell-1_0 < 1.7.1

%description -n typelib-1_0-Gspell-1
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the GObject Introspection bindings for gspell.

%package devel
Summary:        Development files for the GTK+ spell checker library
Group:          Development/Libraries/GNOME
Requires:       %{shlib} = %{version}
Requires:       typelib-1_0-Gspell-1 = %{version}

%description devel
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the files necessary for developing software using
gspell.

%lang_package

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-1 %{?no_lang_C}

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/gspell-app1

%files -n %{shlib}
%{_libdir}/lib%{name}-1.so.*

%files -n typelib-1_0-Gspell-1
%{_libdir}/girepository-1.0/Gspell-1.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/gspell-1.0/
%{_includedir}/gspell-1/
%{_libdir}/lib%{name}-1.so
%{_libdir}/pkgconfig/gspell-1.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gspell-1.*

%files lang -f %{name}-1.lang

%changelog
