#
# spec file for package libupnp
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
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


%define pnpver 17
%define ixmlver 11
Name:           libupnp
Version:        1.14.15
Release:        0
Summary:        An implementation of Universal Plug and Play (UPnP)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/pupnp/pupnp
Source:         https://github.com/pupnp/pupnp/releases/download/release-%version/libupnp-%version.tar.bz2
Source3:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%package -n %name%pnpver
Summary:        An implementation of Universal Plug and Play (UPnP)
Group:          System/Libraries

%description -n %name%pnpver
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems

%package -n libixml%ixmlver
Summary:        The Portable UPnP SDK's XML library
Group:          System/Libraries

%description -n libixml%ixmlver
A C XML parsing library originally created for the Intel UPnP SDK for Linux.

%package devel
Summary:        The Portable Universal Plug and Play (UPnP) SDK
Group:          Development/Libraries/C and C++
Provides:       libixml-devel = %version-%release
Requires:       %name%pnpver = %version
Requires:       libixml%ixmlver = %version

%description devel
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%prep
%autosetup

%build
# the openssl simply does not compile
%configure \
    --disable-samples \
    --enable-ipv6 \
    --disable-static \
    --enable-reuseaddr \
    --disable-open_ssl \
    --enable-unspecified_server
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -p /sbin/ldconfig -n %name%pnpver
%postun -p /sbin/ldconfig -n %name%pnpver
%post   -p /sbin/ldconfig -n libixml%ixmlver
%postun -p /sbin/ldconfig -n libixml%ixmlver

%files -n %name%pnpver
%license COPYING
%_libdir/libupnp.so.%{pnpver}*

%files -n libixml%ixmlver
%license COPYING
%_libdir/libixml.so.%{ixmlver}*

%files devel
%doc ChangeLog
%_libdir/pkgconfig/libupnp.pc
%_libdir/libixml.so
%_libdir/libupnp.so
%_includedir/upnp/

%changelog
