#
# spec file for package cinnamon-menus
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover   0
Name:           cinnamon-menus
Version:        6.4.0
Release:        0
Summary:        A menu system for the Cinnamon Desktop
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxmint/cinnamon-menus
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(python3)

%description
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

%package -n libcinnamon-menu-3-%{sover}
Summary:        A menu system for the Cinnamon desktop environment
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libcinnamon-menu-3-%{sover}
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

%package -n typelib-1_0-CMenu-3_0
Summary:        Libcinnamon-menu API -- Introspection bindings
# typelib-1_0-CinnamonMenu-3_0 was last used in openSUSE Leap 42.2.
Group:          System/Libraries
Provides:       typelib-1_0-CinnamonMenu-3_0 = %{version}
Obsoletes:      typelib-1_0-CinnamonMenu-3_0 < %{version}

%description -n typelib-1_0-CMenu-3_0
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

This package provides the GObject Introspection bindings for
cinnamon-menus.

%package -n libcinnamon-menu-3-devel
Summary:        Libraries and development headers for cinnamon-menus
Group:          Development/Libraries/Other
Requires:       libcinnamon-menu-3-%{sover} = %{version}
Requires:       typelib-1_0-CMenu-3_0 = %{version}

%description -n libcinnamon-menu-3-devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
This package ships the HTML documentation for %{name}

%prep
%autosetup

%build
%meson \
  -Ddeprecated_warnings=true \
  -Denable_debug=false \
  -Denable_docs=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libcinnamon-menu-3-%{sover}

%files -n libcinnamon-menu-3-%{sover}
%license COPYING COPYING.LIB
%doc AUTHORS README debian/changelog
%{_libdir}/libcinnamon-menu-3.so.%{sover}*

%files -n libcinnamon-menu-3-devel
%{_includedir}/%{name}-3.0/
%{_libdir}/libcinnamon-menu-3.so
%{_libdir}/pkgconfig/libcinnamon-menu-3.0.pc
%{_datadir}/gir-1.0/CMenu-3.0.gir

%files -n typelib-1_0-CMenu-3_0
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files doc
%{_datadir}/gtk-doc/html/cmenu

%changelog
