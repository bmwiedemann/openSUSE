#
# spec file for package ministream
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define sover 1

Name:           ministream
Version:        0.99.1
Release:        0
Summary:        A very small alternative to appstream 
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/ministream
Source:         %{name}-%{version}.tar.xz

BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
ministream is a very small alternative to appstream just for
libadwaita, that only depends on glib and gobject.

%package -n lib%{name}%{sover}
Summary:        Shared library for ministream

%description -n lib%{name}%{sover}
ministream is a very small alternative to appstream just for
libadwaita, that only depends on glib and gobject.

This package contains the shared library.

%package -n typelib-1_0-Ministream-1
Summary:        Introspection files for ministream

%description -n typelib-1_0-Ministream-1
ministream is a very small alternative to appstream just for
libadwaita, that only depends on glib and gobject.

This package contains instrospection files for ministream.

%package devel
Summary:        Develfiles for ministream
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-Ministream-1 = %{version}

%description devel
ministream is a very small alternative to appstream just for
libadwaita, that only depends on glib and gobject.
 
This package contains the development files for ministream.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%check
%meson_test

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n typelib-1_0-Ministream-1
%{_libdir}/girepository-1.0/Ministream-1.typelib

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}-version.h
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Ministream-1.gir

%changelog

