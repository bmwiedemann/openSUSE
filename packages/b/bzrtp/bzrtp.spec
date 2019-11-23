#
# spec file for package bzrtp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.0.6
Release:        0
Summary:        ZRTP keys exchange protocol implementation
License:        GPL-2.0-or-later
URL:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bzrtp-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install libbzrtp.pc.
Patch0:         bzrtp-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)

%description
bzrtp is a FOSS implementation of ZRTP keys exchange protocol.
The library written in C 89, is fully portable, and can be executed
on many platforms including x86 and ARM processors.

%package -n lib%{name}%{sover}
Summary:        ZRTP keys exchange protocol implementation

%description -n lib%{name}%{sover}
bzrtp is a FOSS implementation of ZRTP keys exchange protocol.
The library written in C 89, is fully portable, and can be executed
on many platforms including x86 and ARM processors.

%package devel
Summary:        Development files of libbzrtp
Requires:       lib%{name}%{sover} = %{version}

%description devel
The libbzrtp development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libbzrtp.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%doc AUTHORS NEWS README.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
