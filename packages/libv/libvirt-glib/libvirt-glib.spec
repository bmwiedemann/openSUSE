#
# spec file for package libvirt-glib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           libvirt-glib
Version:        2.0.0
Release:        0
Summary:        GLib and GObject mapping of libvirt
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://libvirt.org
Source0:        http://libvirt.org/sources/glib/%{name}-%{version}.tar.gz
Source1:        http://libvirt.org/sources/glib/%{name}-%{version}.tar.gz.asc

BuildRequires:  fdupes
BuildRequires:  intltool >= 0.35.0
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.8
BuildRequires:  pkgconfig(gthread-2.0) >= 2.36.0
BuildRequires:  pkgconfig(libvirt) >= 1.2.5
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0

%description
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%package -n libvirt-glib-1_0-0
Summary:        GLib and GObject mapping of libvirt
Group:          System/Libraries

%description -n libvirt-glib-1_0-0
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%package -n typelib-1_0-LibvirtGConfig-1_0
Summary:        GLib and GObject mapping of libvirt - gi-bindings
Group:          System/Libraries

%description -n typelib-1_0-LibvirtGConfig-1_0
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%package -n typelib-1_0-LibvirtGLib-1_0
Summary:        GLib and GObject mapping of libvirt - gi-bindings
Group:          System/Libraries

%description -n typelib-1_0-LibvirtGLib-1_0
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%package -n typelib-1_0-LibvirtGObject-1_0
Summary:        GLib and GObject mapping of libvirt - gi-bindings
Group:          System/Libraries

%description -n typelib-1_0-LibvirtGObject-1_0
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%package devel
Summary:        GLib and GObject mapping of libvirt - Development files
Group:          Development/Languages/C and C++
Requires:       libvirt-glib-1_0-0 = %{version}
Requires:       typelib-1_0-LibvirtGConfig-1_0 = %{version}
Requires:       typelib-1_0-LibvirtGLib-1_0 = %{version}
Requires:       typelib-1_0-LibvirtGObject-1_0 = %{version}

%description devel
libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). It is free software
available under the GNU Lesser General Public License. Virtualization on
the Linux Operating System means the ability to run multiple instances of
Operating Systems concurrently on a single hardware system where the basic
resources are driven by a Linux instance. The library aim at providing
long term stable C API initially for the Xen paravirtualization but
should be able to integrate other virtualization mechanisms if needed

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes %{buildroot}/%{_datadir}/gtk-doc/

%post -n libvirt-glib-1_0-0 -p /sbin/ldconfig
%postun -n libvirt-glib-1_0-0 -p /sbin/ldconfig

%files -n libvirt-glib-1_0-0 -f %{name}.lang
%license COPYING
%doc README ChangeLog
%{_libdir}/libvirt-gconfig-1.0.so.*
%{_libdir}/libvirt-glib-1.0.so.*
%{_libdir}/libvirt-gobject-1.0.so.*

%files -n typelib-1_0-LibvirtGConfig-1_0
%{_libdir}/girepository-1.0/LibvirtGConfig-1.0.typelib

%files -n typelib-1_0-LibvirtGLib-1_0
%{_libdir}/girepository-1.0/LibvirtGLib-1.0.typelib

%files -n typelib-1_0-LibvirtGObject-1_0
%{_libdir}/girepository-1.0/LibvirtGObject-1.0.typelib

%files devel
%{_libdir}/libvirt-gconfig-1.0.so
%{_libdir}/libvirt-glib-1.0.so
%{_libdir}/libvirt-gobject-1.0.so
%{_datadir}/gir-1.0/LibvirtGConfig-1.0.gir
%{_datadir}/gir-1.0/LibvirtGLib-1.0.gir
%{_datadir}/gir-1.0/LibvirtGObject-1.0.gir
%{_includedir}/libvirt-gconfig-1.0/
%{_includedir}/libvirt-glib-1.0/
%{_includedir}/libvirt-gobject-1.0/
%{_libdir}/pkgconfig/libvirt-gconfig-1.0.pc
%{_libdir}/pkgconfig/libvirt-glib-1.0.pc
%{_libdir}/pkgconfig/libvirt-gobject-1.0.pc
%{_datadir}/gtk-doc/html/Libvirt-gconfig/
%{_datadir}/gtk-doc/html/Libvirt-glib/
%{_datadir}/gtk-doc/html/Libvirt-gobject/
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libvirt-gconfig-1.0.vapi
%{_datadir}/vala/vapi/libvirt-glib-1.0.vapi
%{_datadir}/vala/vapi/libvirt-gobject-1.0.vapi
%{_datadir}/vala/vapi/libvirt-gobject-1.0.deps

%changelog
