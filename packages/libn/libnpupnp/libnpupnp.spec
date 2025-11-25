#
# spec file for package libnpupnp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define so_ver  13
Name:           libnpupnp
Version:        6.2.3
Release:        0
Summary:        A C++ base UPnP library, derived from Portable UPnP, a.k.a libupnp
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.lesbonscomptes.com/upmpdcli/
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/libnpupnp-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/libnpupnp-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  c++_compiler
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

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{name}%{so_ver}

%files -n %{name}%{so_ver}
%license COPYING
%{_libdir}/*.so.*

%files -n libnpupnp-devel
%license COPYING
%{_includedir}/npupnp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
