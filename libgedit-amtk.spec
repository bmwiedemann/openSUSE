#
# spec file for package libgedit-amtk
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

%define api_ver 5

Name:           libgedit-amtk
Version:        5.8.0
Release:        0
Summary:        An Actions, Menus and Toolbars Kit
License:        LGPL-3.0-or-later
URL:            https://gedit-technology.net
Source:         %name-%version.tar.xz
BuildRequires:  gtk-doc >= 1.25
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
“Actions, Menus and Toolbars Kit” or just AMTK is a basic
GtkUIManager replacement based on GAction, suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

%package -n libgedit-amtk-%{api_ver}-0
Summary:        Shared Library for AMTK
# Make the lang package installable
Group:          System/Libraries
Provides:       %{name}-%{api_ver} = %{version}

%description -n libgedit-amtk-%{api_ver}-0
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
Requires:       libgedit-amtk-%{api_ver}-0 = %{version}
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
%meson \
  -Dgtk_doc=true
%meson_build

%install
%meson_install
%find_lang %{name}-%{api_ver}

%ldconfig_scriptlets -n libgedit-amtk-%{api_ver}-0

%check
%meson_test

%files -n libgedit-amtk-%{api_ver}-0
%license LICENSES/*
%{_libdir}/%{name}-%{api_ver}.so.*

%files -n typelib-1_0-Amtk-%{api_ver}
%{_libdir}/girepository-1.0/Amtk-%{api_ver}.typelib

%files devel
%doc README.md NEWS
%doc %{_datadir}/gtk-doc/html/%{name}-%{api_ver}
%{_datadir}/gir-1.0/Amtk-%{api_ver}.gir
%{_includedir}/%{name}-%{api_ver}/
%{_libdir}/pkgconfig/%{name}-%{api_ver}.pc
%{_libdir}/%{name}-%{api_ver}.so

%files -n %{name}-%{api_ver}-lang -f %{name}-%{api_ver}.lang

%changelog

