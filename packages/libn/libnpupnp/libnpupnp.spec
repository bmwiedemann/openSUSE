#
# spec file for package libnpupnp
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


%define so_ver  13
Name:           libnpupnp
Version:        6.1.2
Release:        0
Summary:        A C++ base UPnP library, derived from Portable UPnP, a.k.a libupnp
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.lesbonscomptes.com/upmpdcli/
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/libnpupnp-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/libnpupnp-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/jf-at-dockes.org.pub#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)

%description
A C++ base UPnP library, derived from Portable UPnP, a.k.a libupnp

%package -n %{name}%{so_ver}
Summary:        A C++ base UPnP library, derived from Portable UPnP, a.k.a libupnp
Group:          System/Libraries

%description -n %{name}%{so_ver}
A C++ base UPnP library, derived from Portable UPnP, a.k.a libupnp

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
sed -i 's/  soversion:.*/  version: '\''13.1.0'\'',/' meson.build

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

%files -n libnpupnp-devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
