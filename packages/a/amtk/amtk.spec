#
# spec file for package amtk
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 Luciano Santos, luc14n0@linuxmail.org.
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


%define api_ver 5
%define libamtk libamtk-%{api_ver}-0
Name:           amtk
Version:        5.1.2
Release:        0
Summary:        An Actions, Menus and Toolbars Kit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Amtk
Source0:        https://download.gnome.org/sources/amtk/5.1/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel >= 1.42.0
BuildRequires:  gtk-doc >= 1.25
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.52
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
Requires:       %{libamtk} = %{version}

%description
“Actions, Menus and Toolbars Kit” or just AMTK is a basic
GtkUIManager replacement based on GAction, suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

%package -n %{libamtk}
Summary:        Shared Library for AMTK
# Make the lang package installable
Group:          System/Libraries
Provides:       %{name}-%{api_ver} = %{version}

%description -n %{libamtk}
“Actions, Menus and Toolbars Kit” or just AMTK is a basic
GtkUIManager replacement based on GAction, suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

This package provides the AMTK Shared Library

%package -n typelib-1_0-Amtk-%{api_ver}
Summary:        GObject Introspection Bindings for AMTK
Group:          System/Libraries

%description -n typelib-1_0-Amtk-%{api_ver}
“Actions, Menus and Toolbars Kit” or just AMTK is a basic
GtkUIManager replacement based on GAction, suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

This package provides the GObject Introspection Bindings for AMTK.

%package devel
Summary:        Development files for Tepl, a text editor framework
Group:          Development/Libraries/GNOME
Requires:       %{libamtk} = %{version}
Requires:       typelib-1_0-Amtk-%{api_ver} = %{version}

%description devel
“Actions, Menus and Toolbars Kit” or just AMTK is a basic
GtkUIManager replacement based on GAction, suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

This package provides all the necessary files for development
with AMTK.

%lang_package -n %{name}-%{api_ver}

%prep
%autosetup -p1

%build
%configure \
    --enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-%{api_ver}

%post   -n %{libamtk} -p /sbin/ldconfig
%postun -n %{libamtk} -p /sbin/ldconfig

%files -n %{libamtk}
%license COPYING
%doc NEWS
%{_libdir}/libamtk-%{api_ver}.so.*

%files -n typelib-1_0-Amtk-%{api_ver}
%{_libdir}/girepository-1.0/Amtk-%{api_ver}.typelib

%files devel
%doc ABOUT-NLS AUTHORS HACKING README
%doc %{_datadir}/gtk-doc/html/%{name}-%{api_ver}.0
%{_datadir}/gir-1.0/Amtk-%{api_ver}.gir
%{_includedir}/amtk-%{api_ver}/
%{_libdir}/pkgconfig/amtk-%{api_ver}.pc
%{_libdir}/libamtk-%{api_ver}.so

%files -n %{name}-%{api_ver}-lang -f %{name}-%{api_ver}.lang

%changelog
