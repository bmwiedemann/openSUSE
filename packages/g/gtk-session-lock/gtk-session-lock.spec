#
# spec file for package gtk-session-lock
#
# Copyright (c) 2024 SUSE LLC
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

%define libname libgtk-session-lock0

Name:           gtk-session-lock
Version:        0.2.0
Release:        0
Summary:        A library to build screen lockers
License:        GPL-3.0 AND MIT
URL:            https://github.com/Cu3PO42/gtk-session-lock
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
This is a library to use GTK 3 to build screen lockers using the
secure ext-session-lock-v1 protocol. This Library is compatible
with C, C++ and any language that supports GObject introspection
files (Python, Vala, etc, see using the library below).

This library is a fork of the incredible gtk-layer-shell, which has
laid all the groundwork necessary to make this happen.

%package -n %{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       typelib-1_0-GtkSessionLock-0_1 = %{version}

%description -n %{name}-devel
Development files and headers for %{name}

%package -n %{libname}
Summary:        Library to build screen lockers with GTK
Group:          System/Libraries

%description -n %{libname}
Library to use GTK 3 to build screen lockers using the secure ext-session-lock-v1 protocol.

%package -n     typelib-1_0-GtkSessionLock-0_1
Summary:        Library to build screen lockers with GTK
Group:          System/Libraries

%description -n typelib-1_0-GtkSessionLock-0_1
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone..

This package provides the GObject Introspection bindings for gtk-session-lock.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE_GPL.txt LICENSE_MIT.txt
%doc README.md
%{_libdir}/libgtk-session-lock.so.0
%{_libdir}/libgtk-session-lock.so.0.?.?

%files -n %{name}-devel
%{_includedir}/%{name}/
%{_libdir}/libgtk-session-lock.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/gir-1.0/GtkSessionLock-0.1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtk-session-lock-0.deps
%{_datadir}/vala/vapi/gtk-session-lock-0.vapi

%files -n typelib-1_0-GtkSessionLock-0_1
%{_libdir}/girepository-1.0/GtkSessionLock-0.1.typelib

%changelog
