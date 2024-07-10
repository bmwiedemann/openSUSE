#
# spec file for package libmediaart
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           libmediaart
Version:        1.9.6
Release:        0
Summary:        Media Art extraction library
# License note: src.rpm contains GPL-2.0+ (tests) and LGPL-2.1+ code
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Other
URL:            https://gitlab.gnome.org/GNOME/libmediaart
Source0:        https://download.gnome.org/sources/libmediaart/1.9/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.35.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:  pkgconfig(vapigen)

%description
The libmediaart library is the foundation for media art caching,
extraction and lookup for applications on the desktop.

%package -n libmediaart-2_0-0
# License note: the library is pure LGPL-2.1+
Summary:        Media Art extraction library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libmediaart-2_0-0
The libmediaart library is the foundation for media art caching,
extraction and lookup for applications on the desktop.

%package -n typelib-1_0-MediaArt-2_0
# License note: the library is pure LGPL-2.1+
Summary:        Introspection bindings for the Media Art extraction library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-MediaArt-2_0
The libmediaart library is the foundation for media art caching,
extraction and lookup for applications on the desktop.

%package devel
# License note: the library is pure LGPL-2.1+
Summary:        Development files for the Media Art extraction library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       libmediaart-2_0-0 = %{version}
Requires:       typelib-1_0-MediaArt-2_0 = %{version}

%description devel
The libmediaart library is the foundation for media art caching,
extraction and lookup for applications on the desktop.

%prep
%autosetup -p1

%build
%meson \
	-Dimage_library=gdk-pixbuf \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

%post -n libmediaart-2_0-0 -p /sbin/ldconfig
%postun -n libmediaart-2_0-0 -p /sbin/ldconfig

%files -n libmediaart-2_0-0
%license COPYING.LESSER
%{_libdir}/libmediaart-2.0.so.*

%files -n typelib-1_0-MediaArt-2_0
%{_libdir}/girepository-1.0/MediaArt-2.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/MediaArt-2.0.gir
%{_libdir}/libmediaart-2.0.so
%{_libdir}/pkgconfig/libmediaart-2.0.pc
%{_includedir}/libmediaart-2.0/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libmediaart-2.0.deps
%{_datadir}/vala/vapi/libmediaart-2.0.vapi

%changelog
