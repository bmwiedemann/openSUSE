#
# spec file for package libupnp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pnpver 22
Name:           libupnp
Version:        22.0.4
Release:        0
Summary:        An implementation of Universal Plug and Play (UPnP)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/pupnp/pupnp
Source:         https://github.com/pupnp/pupnp/releases/download/release-%version/%name-%version.tar.bz2
Source3:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.11
BuildRequires:  pkg-config

%description
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%package -n libupnp%pnpver
Summary:        An implementation of Universal Plug and Play (UPnP)
Group:          System/Libraries

%description -n libupnp%pnpver
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems

%package -n libixml%pnpver
Summary:        The Portable UPnP SDK's XML library
Group:          System/Libraries

%description -n libixml%pnpver
A C XML parsing library originally created for the Intel UPnP SDK for Linux.

%package devel
Summary:        The Portable Universal Plug and Play (UPnP) SDK
Group:          Development/Libraries/C and C++
Provides:       libixml-devel = %version-%release
Requires:       libixml%pnpver = %version
Requires:       libupnp%pnpver = %version

%description devel
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%prep
%autosetup -p1

%build
# the openssl simply does not compile
%cmake \
	-DUPNP_BUILD_SAMPLES=OFF \
	-DUPNP_ENABLE_IPV6=ON \
	-DUPNP_BUILD_STATIC=OFF \
	-DUPNP_MINISERVER_REUSEADDR=ON \
	-DUPNP_ENABLE_OPEN_SSL=OFF \
	-DUPNP_ENABLE_UNSPECIFIED_SERVER=ON \
	-DUPNP_ENABLE_TESTING=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libupnp%pnpver
%ldconfig_scriptlets -n libixml%pnpver

%files -n libupnp%pnpver
%license COPYING
%_libdir/libupnp.so.%{pnpver}*

%files -n libixml%pnpver
%license COPYING
%_libdir/libixml.so.%{pnpver}*

%files devel
%doc ChangeLog
%_libdir/pkgconfig/libupnp.pc
%_libdir/libixml.so
%_libdir/libupnp.so
%_includedir/upnp/
%_libdir/cmake/

%changelog
