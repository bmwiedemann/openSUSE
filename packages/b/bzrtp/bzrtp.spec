#
# spec file for package bzrtp
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   0
Name:           bzrtp
Version:        5.3.105
Release:        0
Summary:        ZRTP keys exchange protocol implementation
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/bzrtp/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bzrtp-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install libbzrtp.pc.
Patch0:         bzrtp-fix-pkgconfig.patch
# PATCH-FIX-UPSTREAM
Patch1:         set_current_version.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
%if 0%{?suse_version} >= 1600
BuildRequires:  liboqs-devel
# At the time of writing (13/Dec/2023), PQCE is only available on Tumbleweed.
BuildRequires:  postquantumcryptoengine-devel >= 5.3.0~git.20230802
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= %{version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)

%description
bzrtp is an implementation of the ZRTP key exchange protocol.
The library written in C89.

%package -n lib%{name}%{sover}
Summary:        ZRTP key exchange protocol implementation
Group:          Productivity/Telephony/Utilities

%description -n lib%{name}%{sover}
bzrtp is an implementation of the ZRTP key exchange protocol.
The library written in C89.

%package devel
Summary:        Development files for libbzrtp
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The libbzrtp development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libbzrtp.

%prep
%autosetup -p1

%build
%cmake \
%if 0%{?suse_version} >= 1600
  -DENABLE_PQCRYPTO=ON \
%endif
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%dir %{_datadir}/BZRTP
%dir %{_datadir}/BZRTP/cmake
%{_datadir}/BZRTP/cmake/*.cmake

%changelog
