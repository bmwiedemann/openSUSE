#
# spec file for package libwnck
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


Name:           libwnck
Version:        43.0
Release:        0
Summary:        Window Navigator Construction Kit (Library Package)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://git.gnome.org/browse/libwnck
Source0:        https://download.gnome.org/sources/libwnck/43/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM handle-avoid-segfault-in-invalidate-icons.patch glgo#GNOME/libwnck#46 -- avoid segfault in invalidate_icons
Patch0:         handle-avoid-segfault-in-invalidate-icons.patch

BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)

%description
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

%package -n libwnck-3-0
Summary:        Window Navigator Construction Kit (Library Package)
Group:          Development/Libraries/GNOME
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
#

%description -n libwnck-3-0
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

%package -n typelib-1_0-Wnck-3_0
Summary:        Window Navigator Construction Kit (Library Package) -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Wnck-3_0
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

This package provides the GObject Introspection bindings for libwnck.

%package tools
Summary:        Window Navigator Construction Kit -- Tools
Group:          Development/Libraries/GNOME

%description tools
The Window Navigator Construction Kit is a library that can be used to
write task lists, pagers, and similar GNOME programs.

This package provides some utilities based on libwnck.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       libwnck-3-0 = %{version}
Requires:       typelib-1_0-Wnck-3_0 = %{version}
Obsoletes:      libwnck-doc < %{version}
Provides:       libwnck-doc = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dintrospection=enabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}-3.0
%fdupes %{buildroot}/{_prefix}

%post -n libwnck-3-0 -p /sbin/ldconfig
%postun -n libwnck-3-0 -p /sbin/ldconfig

%files tools
%{_bindir}/wnck-urgency-monitor
%{_bindir}/wnckprop

%files lang -f %{name}-3.0.lang

%files -n libwnck-3-0
%license COPYING
%{_libdir}/*.so.*

%files -n typelib-1_0-Wnck-3_0
%{_libdir}/girepository-1.0/Wnck-3.0.typelib

%files devel
%doc AUTHORS README NEWS ChangeLog
%{_includedir}/libwnck-3.0/
%{_libdir}/pkgconfig/libwnck-3.0.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Wnck-3.0.gir

%changelog
