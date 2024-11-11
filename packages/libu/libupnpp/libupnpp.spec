#
# spec file for package libupnpp
#
# Copyright (c) 2024 SUSE LLC
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


%define so_ver  16
Name:           libupnpp
Version:        0.26.7
Release:        0
Summary:        Library providing a higher level API over libnpupnp or libupnp
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.lesbonscomptes.com/upmpdcli/index.html
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/libupnpp-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/libupnpp-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/jf-at-dockes.org.pub#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnpupnp) >= 6.0.0

%description
Libupnpp is a C++ wrapper for libupnp a.k.a Portable UPnP (up to branch 0.17),
or its C++ descendant, libnpupnp (versions 0.18 and later).

Libupnpp can be used to implement UPnP devices and services, or Control Points.
The Control Point side of libupnpp, which is documented here,
allows a C++ program to discover UPnP devices, and exchange commands and status with them.

%package -n %{name}%{so_ver}
Summary:        Library providing a higher level C++ API over libnpupnp or libupnp
Group:          System/Libraries

%description -n %{name}%{so_ver}
Libupnpp is a C++ wrapper for libupnp a.k.a Portable UPnP (up to branch 0.17),
or its C++ descendant, libnpupnp (versions 0.18 and later).

Libupnpp can be used to implement UPnP devices and services, or Control Points.
The Control Point side of libupnpp, which is documented here,
allows a C++ program to discover UPnP devices, and exchange commands and status with them.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{so_ver} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
# fix version
sed -i 's/  soversion:.*/  version: '\''16.1.0'\'',/' meson.build

%build
%meson
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig -n %{name}%{so_ver}
%postun -p /sbin/ldconfig -n %{name}%{so_ver}

%files -n %{name}%{so_ver}
%license COPYING
%{_libdir}/*.so.*

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
