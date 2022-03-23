#
# spec file for package libportal
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


%define sover 1

Name:           libportal
Version:        0.6
Release:        0
Summary:        A GIO-style async APIs for most Flatpak portals
License:        LGPL-3.0-or-later
URL:            https://github.com/flatpak/libportal
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)

%description
A GIO-style async APIs for most Flatpak portals.

%package     -n %{name}-%{sover}
Summary:        Shared library for %{name}

%description -n %{name}-%{sover}
A GIO-style async APIs for most Flatpak portals.
This package contains the shared library of %{name}.

%package     -n %{name}-gtk3-%{sover}
Summary:        Shared library for %{name}

%description -n %{name}-gtk3-%{sover}
A GIO-style async APIs for most Flatpak portals.
This package contains the shared library of %{name}.

%package     -n %{name}-gtk4-%{sover}
Summary:        Shared library for %{name}

%description -n %{name}-gtk4-%{sover}
A GIO-style async APIs for most Flatpak portals.
This package contains the shared library of %{name}.

%package     -n %{name}-qt5-%{sover}
Summary:        Shared library for %{name}

%description -n %{name}-qt5-%{sover}
A GIO-style async APIs for most Flatpak portals.
This package contains the shared library of %{name}.

%package -n     typelib-1_0-Xdp-1_0
Summary:        Introspections files for libportal

%description -n typelib-1_0-Xdp-1_0
A GIO-style async APIs for most Flatpak portals.
This package contains the introspection files of %{name}.

%package -n     typelib-1_0-XdpGtk3-1_0
Summary:        Introspections files for libportal

%description -n typelib-1_0-XdpGtk3-1_0
A GIO-style async APIs for most Flatpak portals.
This package contains the introspection files of %{name}.

%package -n     typelib-1_0-XdpGtk4-1_0
Summary:        Introspections files for libportal

%description -n typelib-1_0-XdpGtk4-1_0
A GIO-style async APIs for most Flatpak portals.
This package contains the introspection files of %{name}.

%package devel
Summary:        A GIO-style async APIs for most Flatpak portals -- Development files
Requires:       %{name}-%{sover} = %{version}
Requires:       typelib-1_0-Xdp-1_0 = %{version}

%description devel
The %{name}-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%package gtk3-devel
Summary:        A GIO-style async APIs for most Flatpak portals -- Development files
Requires:       %{name}-gtk3-%{sover} = %{version}
Requires:       typelib-1_0-XdpGtk3-1_0 = %{version}

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%package gtk4-devel
Summary:        A GIO-style async APIs for most Flatpak portals -- Development files
Requires:       %{name}-gtk4-%{sover} = %{version}
Requires:       typelib-1_0-XdpGtk4-1_0 = %{version}

%description gtk4-devel
The %{name}-gtk4-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%package qt5-devel
Summary:        A GIO-style async APIs for most Flatpak portals -- Development files
Requires:       %{name}-qt5-%{sover} = %{version}

%description qt5-devel
The %{name}-qt5-devel package contains libraries, build data, and
header files for developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{name}-%{sover}
%ldconfig_scriptlets -n %{name}-gtk3-%{sover}
%ldconfig_scriptlets -n %{name}-gtk4-%{sover}
%ldconfig_scriptlets -n %{name}-qt5-%{sover}

%files -n %{name}-%{sover}
%license COPYING
%{_libdir}/libportal.so.%{sover}*

%files -n %{name}-gtk3-%{sover}
%{_libdir}/libportal-gtk3.so.%{sover}*

%files -n %{name}-gtk4-%{sover}
%{_libdir}/libportal-gtk4.so.%{sover}*

%files -n %{name}-qt5-%{sover}
%{_libdir}/libportal-qt5.so.%{sover}*

%files -n typelib-1_0-Xdp-1_0
%{_libdir}/girepository-1.0/Xdp-1.0.typelib

%files -n typelib-1_0-XdpGtk3-1_0
%{_libdir}/girepository-1.0/XdpGtk3-1.0.typelib

%files -n typelib-1_0-XdpGtk4-1_0
%{_libdir}/girepository-1.0/XdpGtk4-1.0.typelib

%files devel
%doc NEWS README.md
%doc %{_datadir}/doc/libportal-1
%{_includedir}/%{name}
%{_libdir}/libportal.so
%{_libdir}/pkgconfig/libportal.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libportal.deps
%{_datadir}/vala/vapi/libportal.vapi
%{_datadir}/gir-1.0/Xdp-1.0.gir

%files gtk3-devel
%{_includedir}/libportal-gtk3
%{_libdir}/libportal-gtk3.so
%{_libdir}/pkgconfig/libportal-gtk3.pc
%{_datadir}/gir-1.0/XdpGtk3-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libportal-gtk3.deps
%{_datadir}/vala/vapi/libportal-gtk3.vapi

%files gtk4-devel
%{_includedir}/libportal-gtk4
%{_libdir}/libportal-gtk4.so
%{_libdir}/pkgconfig/libportal-gtk4.pc
%{_datadir}/gir-1.0/XdpGtk4-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libportal-gtk4.deps
%{_datadir}/vala/vapi/libportal-gtk4.vapi

%files qt5-devel
%{_includedir}/libportal-qt5
%{_libdir}/libportal-qt5.so
%{_libdir}/pkgconfig/libportal-qt5.pc

%changelog
