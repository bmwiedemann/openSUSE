#
# spec file for package libupnpp
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define so_ver  17
Name:           libupnpp
Version:        1.0.3
Release:        0
Summary:        Library providing a higher level API over libnpupnp or libupnp
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.lesbonscomptes.com/upmpdcli/index.html
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/libupnpp-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/libupnpp-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  c++_compiler
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{name}%{so_ver}

%files -n %{name}%{so_ver}
%license COPYING LICENSE
%{_libdir}/*.so.%{so_ver}
%{_libdir}/*.so.%{version}

%files devel
%license COPYING LICENSE
%{_includedir}/libupnpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
