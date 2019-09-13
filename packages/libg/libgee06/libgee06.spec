#
# spec file for package libgee
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libgee06
%define _name libgee
Version:        0.6.6
Release:        0
Summary:        GObject-based library providing commonly used data structures
License:        LGPL-2.1+
Group:          Development/Libraries/GNOME
Url:            http://live.gnome.org/Libgee
Source:         http://download.gnome.org/sources/libgee/0.6/%{_name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE libgee-gir.patch dimstar@opensuse.org -- The typelib file should not reference libgee, but libgee.so.2. The patch is not clean for upstream, but discussion has started at bgo#667529.
Patch0:         libgee-gir.patch
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n libgee2
Summary:        GObject-based library providing commonly used data structures
Group:          System/Libraries
%if 0%{?suse_version} <= 1210
Requires:       typelib-1_0-Gee-1_0
%endif

%description -n libgee2
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n typelib-1_0-Gee-1_0
Summary:        GObject-based library providing commonly used data structures -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gee-1_0
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package provides the GObject Introspection bindings for libgee.

%package -n libgee06-devel
Summary:        GObject-based library providing useful data structures - Development Files
Group:          Development/Libraries/GNOME
Requires:       libgee2 = %{version}
Requires:       typelib-1_0-Gee-1_0 = %{version}

%description -n libgee06-devel
Libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
rm %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -n libgee2 -p /sbin/ldconfig

%postun -n libgee2 -p /sbin/ldconfig

%files -n libgee2
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-Gee-1_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Gee-1.0.typelib

%files -n libgee06-devel
%defattr(-, root, root)
%{_includedir}/gee-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

%changelog
