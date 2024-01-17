#
# spec file for package libavtp
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libavtp
Version:        0.2.0
Release:        0
Summary:        Audio Video Transport Protocol (AVTP) Support Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/AVnu/libavtp.git
Source:         https://github.com/Avnu/libavtp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)

%description
An implementation of Audio Video Transport Protocol (AVTP) as specified
in IEEE 1722-2016.

%package -n libavtp0
Summary:        Audio Video Transport Protocol (AVTP) Support Library
Group:          System/Libraries

%description -n libavtp0
An implementation of Audio Video Transport Protocol (AVTP) as specified
in IEEE 1722-2016.

%package devel
Summary:        Header files for the Audio/Video Transport Protocol support library
Group:          Development/Libraries/C and C++
Requires:       libavtp0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libavtp.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -n libavtp0 -p /sbin/ldconfig
%postun -n libavtp0 -p /sbin/ldconfig

%files -n libavtp0
%{_libdir}/libavtp.so.0
%{_libdir}/libavtp.so.0.*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/*.h
%{_libdir}/libavtp.so
%{_libdir}/pkgconfig/avtp.pc

%changelog
