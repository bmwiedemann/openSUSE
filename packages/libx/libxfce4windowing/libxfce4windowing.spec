#
# spec file for package libxfce4windowing
#
# Copyright (c) 2024 SUSE LLC

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

%define api        0
%define major      0
%define libname    libxfce4windowing-%{api}-%{major}
%define libnameui  libxfce4windowingui-%{api}-%{major}
%define girname    typelib-1_0-Libxfce4windowing-%{api}_%{major}
%define girnameui  typelib-1_0-Libxfce4windowingui-%{api}_%{major}
%define devname    %{name}-devel
%define docname    %{devname}-doc

Name:           libxfce4windowing
Summary:        Windowing concept abstraction library for X11 and Wayland
Version:        4.20.0
Release:        0
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://gitlab.xfce.org/xfce/libxfce4windowing
Source0:        https://archive.xfce.org/src/xfce/libxfce4windowing/4.20/libxfce4windowing-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE 0001-relax-x11-version.patch -- Allow build for Leap with its ancient but sufficient X11 packages.
Patch1:         0001-relax-x11-version.patch
BuildRequires:  automake
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson
BuildRequires:  xfce4-dev-tools >= 4.19.3
BuildRequires:  pkgconfig(libdisplay-info) >= 0.1.1
BuildRequires:  pkgconfig(gdk-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.42.8
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.72.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.10
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.20
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(x11) >= 1.6.5
BuildRequires:  pkgconfig(xrandr) >= 1.5.0

%description
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck. Wayland is partially supported,
through various Wayland protocol extensions. However, the full range of
operations available on X11 is not available on Wayland, due to missing
features in these protocol extensions.

%package -n %{libname}
Summary:        X11/Wayland windowing utility library for Xfce
Group:          System/Libraries
# Make lang package installable
Provides:       %{name} = %{version}
Recommends:     %{name}-lang = %{version}

%description -n %{libname}
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

%package -n %{libnameui}
Summary:        X11/Wayland windowing utility library for Xfce - extra widgets
Group:          System/Libraries

%description -n %{libnameui}
Libxfce4windowingui is a UI widget utility library that makes use of
libxfce4windowing primitives.

%package -n %{girname}
Summary:        GObject Introspection interface description for Libxfce4windowing
Group:          System/Libraries

%description -n %{girname}
GObject Introspection interface description for Libxfce4windowing.

%package -n %{girnameui}
Summary:        GObject Introspection interface description for Libxfce4windowingui
Group:          System/Libraries

%description -n %{girnameui}
GObject Introspection interface description for Libxfce4windowingui.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{libnameui} = %{version}
Requires:       %{girname} = %{version}
Requires:       %{girnameui} = %{version}

%description -n %{devname}
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck. Wayland is partially supported,
through various Wayland protocol extensions. However, the full range of
operations available on X11 is not available on Wayland, due to missing
features in these protocol extensions.

%package -n %{docname}
Summary:       Documentation for libxfce4windowing
Group:         Documentation/HTML
BuildArch:     noarch
Supplements:   (%{devname} and patterns-base-documentation)

%description -n %{docname}
Provides documentation for libxfce4windowing,
an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

%lang_package

%prep
%autosetup -p1
aclocal
automake

%build
%configure \
	--disable-static
    
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -print -delete

%find_lang %{name} %{?no_lang_C}

%ldconfig_scriptlets -n %{libname}
%ldconfig_scriptlets -n %{libnameui}

%files -n %{libname}
%license COPYING
%{_libdir}/libxfce4windowing-%{api}.so.%{major}{,.*}

%files -n %{libnameui}
%license COPYING
%{_libdir}/libxfce4windowingui-%{api}.so.%{major}{,.*}

%files -n %{girname}
%license COPYING
%{_libdir}/girepository-1.0/Libxfce4windowing-%{api}.%{major}.typelib

%files -n %{girnameui}
%license COPYING
%{_libdir}/girepository-1.0/Libxfce4windowingui-%{api}.%{major}.typelib

%files -n %{devname}
%dir %{_includedir}/xfce4/
%{_includedir}/xfce4/libxfce4windowing{,ui}/
%{_libdir}/libxfce4windowing{,ui}-%{api}.so
%{_libdir}/pkgconfig/libxfce4windowing{,ui}-%{api}.pc
%{_libdir}/pkgconfig/libxfce4windowing-x11-%{api}.pc
%{_datadir}/gir-1.0/Libxfce4windowing-%{api}.%{major}.gir
%{_datadir}/gir-1.0/Libxfce4windowingui-%{api}.%{major}.gir

%files -n %{docname}
%doc NEWS README*
%{_datadir}/gtk-doc/html/libxfce4windowingui
%{_datadir}/gtk-doc/html/libxfce4windowing

%files lang -f %{name}.lang

%changelog
