#
# spec file for package libgee
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2010 Luis Medinas, Portugal
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


Name:           libgee
Version:        0.20.8
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Libgee
Source0:        https://download.gnome.org/sources/libgee/0.20/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.25.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.36

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n libgee-0_8-2
Summary:        GObject-based library providing commonly used data structures
Group:          System/Libraries

%description -n libgee-0_8-2
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides Libgee's shared libraries.

%package -n typelib-1_0-Gee-0_8
Summary:        Introspection bindings for Libgee
Group:          System/Libraries

%description -n typelib-1_0-Gee-0_8
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for Libgee.

%package -n libgee-devel
Summary:        Development files for Libgee
Group:          Development/Libraries/GNOME
Requires:       libgee-0_8-2 = %{version}
Requires:       typelib-1_0-Gee-0_8 = %{version}

%description -n libgee-devel
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides all the files needed for development using Libgee.

%prep
%autosetup -p1
find -name '*.vala' -exec touch {} \;

%build
%configure \
	--disable-static \
	--enable-vala \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libgee-0_8-2

%check
make check

%files -n libgee-0_8-2
%license COPYING
%doc NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-Gee-0_8
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files -n libgee-devel
%doc AUTHORS ChangeLog MAINTAINERS
%{_includedir}/gee-0.8/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

%changelog
