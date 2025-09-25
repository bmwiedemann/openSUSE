#
# spec file for package gtk4-layer-shell
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


%define libname lib%{name}0
Name:           gtk4-layer-shell
Version:        1.2.0+git2.df49531
Release:        0
Summary:        Library to create desktop components for Wayland with GTK4
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/wmww/gtk4-layer-shell
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16.0

%description
Library for using the Layer Shell and Session Lock Wayland protocols with
GTK4. This Library is compatible with C, C++ and any language that supports
GObject introspection files (Python, Vala, etc).


%package -n     %{libname}
Summary:        Library to create components for Wayland and GTK4 using the Layer Shell
License:        MIT
Requires:       typelib-1_0-Gtk4LayerShell-1_0

%description -n %{libname}
Library for using the Layer Shell and Session Lock Wayland protocols with
GTK4. This Library is compatible with C, C++ and any language that supports
GObject introspection files (Python, Vala, etc).

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description    devel
Development files and headers for %{name}.

%package -n     typelib-1_0-Gtk4LayerShell-1_0
Summary:        Library to create desktop components for Wayland
Group:          System/Libraries

%description -n typelib-1_0-Gtk4LayerShell-1_0
This package provides the GObject Introspection bindings for %{name}.

%package -n     typelib-1_0-Gtk4SessionLock-1_0
Summary:        Library to create desktop components for Wayland
Group:          System/Libraries

%description -n typelib-1_0-Gtk4SessionLock-1_0
This package provides the GObject Introspection bindings for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE*
%doc README.md CHANGELOG.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/liblayer-shell-preload.so
%{_libdir}/pkgconfig/%{name}-0.pc
%{_datadir}/gir-1.0
%{_datadir}/vala
%{_includedir}/%{name}

%files -n typelib-1_0-Gtk4LayerShell-1_0
%{_libdir}/girepository-1.0/Gtk4LayerShell-1.0.typelib

%files -n typelib-1_0-Gtk4SessionLock-1_0
%{_libdir}/girepository-1.0/Gtk4SessionLock-1.0.typelib

%changelog

