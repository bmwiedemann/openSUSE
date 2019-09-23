#
# spec file for package libunique1
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   libunique
%define debug_package_requires libunique-1_0-0 = %{version}
Name:           libunique1
Version:        1.1.6
Release:        0
Summary:        A library for writing single instance applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://live.gnome.org/LibUnique
Source:         %{_name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM libunique1-gcc46.patch dimstar@opensuse.org -- Backport commit f791ed from master to unique-1.1.
Patch0:         libunique1-gcc46.patch
# PATCH-FIX-UPSTREAM libunique1-no_g_const_return.patch dimstar@opensuse.org -- Use const instead of G_CONST_RETURN. Not send upstream, as libunique1 is obsoleted.
Patch1:         libunique1-no_g_const_return.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%package -n libunique-1_0-0
Summary:        A library for writing single instance applications
Group:          System/Libraries

%description -n libunique-1_0-0
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%package -n typelib-1_0-Unique-1_0
Summary:        Introspection bindings for libunique
Group:          System/Libraries

%description -n typelib-1_0-Unique-1_0
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

This package provides the GObject Introspection bindings for libunique.

%package devel
Summary:        Development files for libunique
Group:          Development/Libraries/GNOME
Requires:       libunique-1_0-0 = %{version}
Requires:       typelib-1_0-Unique-1_0 = %{version}
Provides:       unique-doc = %{version}
Obsoletes:      unique-doc < %{version}
Provides:       unique-devel = %{version}
Obsoletes:      unique-devel < %{version}

%description devel
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
# We use --disable-maintainer-flags to allow building with deprecated API
%configure \
    --enable-debug=no \
    --enable-static=no \
    --enable-dbus=yes \
    --disable-maintainer-flags
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libunique-1_0-0 -p /sbin/ldconfig
%postun -n libunique-1_0-0 -p /sbin/ldconfig

%files -n libunique-1_0-0
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.0*

%files -n typelib-1_0-Unique-1_0
%{_libdir}/girepository-1.0/Unique-1.0.typelib

%files devel
%{_includedir}/unique-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/unique

%changelog
