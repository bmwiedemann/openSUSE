#
# spec file for package libgexiv2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define pythons python3

Name:           gexiv2
Version:        0.16.0
Release:        0
Summary:        A GObject-based Exiv2 wrapper
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/%{name}/0.16/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  gobject-introspection
BuildRequires:  libtool
BuildRequires:  meson >= 0.48
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  pkgconfig(exiv2) >= 0.26
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n libgexiv2-0_16-4
Summary:        A GObject-based Exiv2 wrapper
Group:          System/Libraries

%description -n libgexiv2-0_16-4
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n typelib-1_0-GExiv2-0_16
Summary:        A GObject-based Exiv2 wrapper - Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GExiv2-0_16
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides the GObject Introspection bindings for the
libgexiv2 library.

%package devel
Summary:        A GObject-based Exiv2 wrapper -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libgexiv2-0_16-4 = %{version}
Requires:       typelib-1_0-GExiv2-0_16 = %{version}

%description devel
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

%package -n python3-gexiv2
Summary:        A GObject-based Exiv2 wrapper
Group:          Development/Libraries/Python
Requires:       python3-gobject
BuildArch:      noarch

%description -n python3-gexiv2
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes the
basic features of Exiv2 available to GNOME applications.

This package provides the Python 3 bindings for the libgexiv2 library.

%prep
%autosetup -p1

%build
%meson \
	-Dintrospection=true \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libgexiv2-0_16-4

%files -n libgexiv2-0_16-4
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/libgexiv2-0.16.so.*

%files -n typelib-1_0-GExiv2-0_16
%{_libdir}/girepository-1.0/GExiv2-0.16.typelib

%files devel
%{_datadir}/gir-1.0/GExiv2-0.16.gir
%{_includedir}/gexiv2-0.16/
%{_libdir}/libgexiv2-0.16.so
%{_libdir}/pkgconfig/gexiv2-0.16.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2-0.16.vapi
%{_datadir}/vala/vapi/gexiv2-0.16.deps

%files -n python3-gexiv2
%{python3_sitelib}/*

%changelog
