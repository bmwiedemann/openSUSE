#
# spec file for package cinnamon-menus
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


%define typelib typelib-1_0-CMenu-3_0
%define soname  libcinnamon-menu-3
%define sover   0
Name:           cinnamon-menus
Version:        5.6.0
Release:        0
Summary:        A menu system for the Cinnamon Desktop
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/linuxmint/cinnamon-menus
Source:         https://github.com/linuxmint/cinnamon-menus/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

%package -n %{soname}-%{sover}
Summary:        A menu system for the Cinnamon desktop environment
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{soname}-%{sover}
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

%package -n %{typelib}
Summary:        Libcinnamon-menu API -- Introspection bindings
# typelib-1_0-CinnamonMenu-3_0 was last used in openSUSE Leap 42.2.
Group:          System/Libraries
Provides:       typelib-1_0-CinnamonMenu-3_0 = %{version}
Obsoletes:      typelib-1_0-CinnamonMenu-3_0 < %{version}

%description -n %{typelib}
cinnamon-menus is an implementation of the draft "Desktop Menu
Specification" from freedesktop.org. This package also contains
the Cinnamon menu layout configuration files, .directory files and
assorted menu related utility programs, Python bindings, and a
simple menu editor.

This package provides the GObject Introspection bindings for
cinnamon-menus.

%package -n %{soname}-devel
Summary:        Libraries and development headers for cinnamon-menus
Group:          Development/Libraries/Other
Requires:       %{soname}-%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description -n %{soname}-devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}-%{sover} -p /sbin/ldconfig
%postun -n %{soname}-%{sover} -p /sbin/ldconfig

%files -n %{soname}-%{sover}
%license COPYING*
%doc AUTHORS README debian/changelog
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname}-devel
%{_includedir}/%{name}-3.0/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/libcinnamon-menu-3.0.pc
%{_datadir}/gir-1.0/CMenu-3.0.gir

%files -n %{typelib}
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%changelog
