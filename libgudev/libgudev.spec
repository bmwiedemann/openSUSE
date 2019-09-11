#
# spec file for package libgudev
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


Name:           libgudev
Version:        232
Release:        0
Summary:        Library that provides GObject bindings for libudev
License:        LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc) >= 1.18
BuildRequires:  pkgconfig(libudev) >= 199
# FIXME - not yet in openSUSE
#BuildRequires:  pkgconfig(umockdev-1.0)

%description
Library provides GObject bindings for libudev. It used to be part
of udev, then merged into systemd. It's now a project on its own.

%package -n libgudev-1_0-0
Summary:        GObject library, to access udev device information
Group:          System/Libraries

%description -n libgudev-1_0-0
This package contains the GObject library libgudev, which provides
access to udev device information.

%package -n typelib-1_0-GUdev-1_0
Summary:        GObject library, to access udev device information -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GUdev-1_0
This package provides the GObject Introspection bindings for libgudev, which
provides access to udev device information.

%package -n libgudev-1_0-devel
Summary:        Devel package for libgudev
Group:          Development/Libraries/C and C++
Requires:       libgudev-1_0-0 = %{version}
Requires:       typelib-1_0-GUdev-1_0 = %{version}

%description -n libgudev-1_0-devel
This is the devel package for the GObject library libgudev, which
provides GObject access to udev device information.

%prep
%setup -q

%build
%configure \
    --disable-static \
    --disable-umockdev \
    --enable-gtk-doc
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgudev-1_0-0 -p /sbin/ldconfig
%postun -n libgudev-1_0-0 -p /sbin/ldconfig

%files -n libgudev-1_0-0
%license COPYING

%{_libdir}/libgudev-1.0.so.*

%files -n typelib-1_0-GUdev-1_0
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files -n libgudev-1_0-devel
%{_includedir}/gudev-1.0/
%{_libdir}/libgudev-1.0.so
%{_libdir}/pkgconfig/gudev-1.0.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gudev/
%{_datadir}/gir-1.0/GUdev-1.0.gir

%changelog
