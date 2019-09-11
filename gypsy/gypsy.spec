#
# spec file for package gypsy
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gypsy
Version:        0.9
Release:        0
Summary:        GPS multiplexing daemon
License:        LGPL-2.1
Group:          Hardware/Other
Url:            http://gypsy.freedesktop.org/
Source0:        http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM gypsy-g_type_init.patch dimstar@opensuse.org -- Fix build with glib 2.36; g_type_init is deprecated and implicit.
Patch0:         gypsy-g_type_init.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bluez-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gudev-1.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to access
GPS data from multiple GPS sources concurrently.

Without some sort of multiplexing system, a GPS device can only safely be
accessed by one client. In a server situation this may not cause any
problems, but on modern desktop which could potentially have multiple
location aware devices, this could be an issue.

%package -n libgypsy0
Summary:        GPS multiplexing daemon library
Group:          System/Libraries

%description -n libgypsy0
Gypsy is a GPS multiplexing daemon which allows multiple clients to access
GPS data from multiple GPS sources concurrently.

Without some sort of multiplexing system, a GPS device can only safely be
accessed by one client. In a server situation this may not cause any
problems, but on modern desktop which could potentially have multiple
location aware devices, this could be an issue.

%package -n libgypsy-devel
Summary:        Development files for gyps, a GPS multiplexing daemon
Group:          Development/Libraries/C and C++
Requires:       dbus-1-glib-devel
Requires:       libgypsy0 = %{version}

%description -n libgypsy-devel
Gypsy is a GPS multiplexing daemon which allows multiple clients to access
GPS data from multiple GPS sources concurrently.

This subpackage contains the header files for developing
applications that want to make use of libgypsy.

%prep
%setup -q
%patch0 -p1

%build
sed -i "s/-Werror/-Wno-format-security/g" configure*
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgypsy0 -p /sbin/ldconfig
%postun -n libgypsy0 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING TODO
%{_libexecdir}/gypsy-daemon
%{_sysconfdir}/dbus-1/system.d/*.conf
%config(noreplace) %{_sysconfdir}/gypsy.conf
%{_datadir}/dbus-1/system-services/*.service

%files -n libgypsy0
%defattr(-, root, root)
%doc COPYING.lib
%{_libdir}/*.so.*

%files -n libgypsy-devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gypsy
%{_datadir}/gtk-doc/html/gypsy
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%changelog
