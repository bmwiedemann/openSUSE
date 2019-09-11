#
# spec file for package orbit2
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


%define _name ORBit2
Name:           orbit2
Version:        2.14.19
Release:        0
Summary:        CORBA Object Request Broker
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.gnome.org/
Source:         ftp://ftp.gnome.org/pub/gnome/sources/ORBit2/2.14/%{_name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  gtk-doc
BuildRequires:  libidl-devel
Provides:       ORBit2

%description
ORBit is a CORBA (Common Object Request Broker
Architecture) ORB (Object Request Broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they are written in or the operating system they run on.

You will need to install this package if you want to run programs that
use the CORBA technology ORBit implementation.

%package devel
Summary:        Development files for the orbit2 CORBA implementation
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libidl-devel
Requires:       pkgconfig(glib-2.0)
Provides:       ORBit2-devel

%description devel
ORBit is a CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they are written in or the operating system they run on.

You will need to install this package if you want to run programs that
use the ORBit implementation of the CORBA technology.

%package doc
Summary:        Documentation for the orbit2 CORBA implementation
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Provides:       ORBit2-doc
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
ORBit is a CORBA (Common Object Request Broker Architecture) ORB
(Object Request Broker).

You will need to install this package if you want to run programs that
use the CORBA technology ORBit implementation.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure\
	--disable-static
echo "#undef G_DISABLE_DEPRECATED" >> config.h
# Do not use parallel make since there is a .deps directory creation
# race in idl-compiler/orbit-idl-c-backend.c:out_for_pass
make -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_bindir}/linc-cleanup-sockets
%{_libdir}/*.so.*
%{_libdir}/orbit-2.0/

%files devel
%{_bindir}/ior-decode-2
%{_bindir}/orbit-idl-2
%{_bindir}/orbit2-config
%{_bindir}/typelib-dump
%{_includedir}/orbit-2.0/
%{_libdir}/*.so
%{_libdir}/libname-server-2.a
%{_libdir}/pkgconfig/ORBit-*.pc
%{_datadir}/aclocal/ORBit2.m4
%{_datadir}/idl/orbit-2.0/

%files doc
%doc %{_datadir}/gtk-doc/html/ORBit2/

%changelog
