#
# spec file for package libspnav
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.1
Release:        0
Summary:        Library for accessing 3D connexion devices
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/spacenav/
Source0:        https://github.com/FreeSpacenav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
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
%autosetup -p1

# Set libdir properly
sed -i 's#libdir=lib#libdir=%{_lib}#' configure

%build
%configure
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libspnav.a

# the pkgconfig file shall be in %%_libdir/pkgconfig
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/spnav.pc %{buildroot}%{_libdir}/pkgconfig/

%post -n libspnav0 -p /sbin/ldconfig
%postun -n libspnav0 -p /sbin/ldconfig

%files -n libspnav0
%license LICENSE
%doc README.md examples
%{_libdir}/libspnav.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libspnav.so
%{_libdir}/pkgconfig/spnav.pc

%changelog
