#
# spec file for package libspnav
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009,2011 Herbert Graeber
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


Name:           libspnav
Version:        0.2.3
Release:        0
Summary:        Library for accessing 3D connexion devices
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            http://sourceforge.net/projects/spacenav/
Source:         https://github.com/FreeSpacenav/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        LICENSE
Patch0:         libspnav-0.2.3-lib_links.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)

%description
The libspnav library is provided as a replacement of the magellan library.
It provides a cleaner, and more orthogonal interface. libspnav supports
both the original X11 protocol for communicating with the driver, and the
new alternative non-X protocol. Programs that choose to use the X11
protocol, are automatically compatible with either the free spacenavd
driver or the official 3dxserv, as if they were using the magellan SDK.

Also, libspnav provides a magellan API wrapper on top of the new API. So,
any applications that were using the magellan library, can switch to
libspnav without any changes. And programmers that are familliar with the
magellan API can continue using it with a free library without the
restrictions of the official SDK.

%package -n libspnav0
Summary:        Library for accessing 3D connexion devices
Group:          Hardware/Other
Suggests:       spacenavd

%description -n libspnav0
The libspnav library is provided as a replacement of the magellan library.
It provides a cleaner, and more orthogonal interface. libspnav supports
both the original X11 protocol for communicating with the driver, and the
new alternative non-X protocol. Programs that choose to use the X11
protocol, are automatically compatible with either the free spacenavd
driver or the official 3dxserv, as if they were using the magellan SDK.

Also, libspnav provides a magellan API wrapper on top of the new API. So,
any applications that were using the magellan library, can switch to
libspnav without any changes. And programmers that are familliar with the
magellan API can continue using it with a free library without the
restrictions of the official SDK.

%package devel
Summary:        Include files for libspnav
Group:          Development/Libraries/C and C++
Requires:       libspnav0 = %{version}-%{release}

%description devel
The libspnav library is provided as a replacement of the magellan library.
It provides a cleaner, and more orthogonal interface. libspnav supports
both the original X11 protocol for communicating with the driver, and the
new alternative non-X protocol. Programs that choose to use the X11
protocol, are automatically compatible with either the free spacenavd
driver or the official 3dxserv, as if they were using the magellan SDK.

Also, libspnav provides a magellan API wrapper on top of the new API. So,
any applications that were using the magellan library, can switch to
libspnav without any changes. And programmers that are familliar with the
magellan API can continue using it with a free library without the
restrictions of the official SDK.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
# Set libdir properly
sed -i "s/libdir=lib/libdir=%{_lib}/g" configure
%configure
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a

%post -n libspnav0 -p /sbin/ldconfig
%postun -n libspnav0 -p /sbin/ldconfig

%files -n libspnav0
%license LICENSE
%doc README examples
%{_libdir}/libspnav.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libspnav.so

%changelog
