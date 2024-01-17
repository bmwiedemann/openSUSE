#
# spec file for package ois
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 1_5_0
Name:           ois
Version:        1.5.1
Release:        0
Summary:        Object Oriented Input System
License:        Zlib
Group:          System/Libraries
URL:            https://wgois.github.io/OIS/
Source0:        https://github.com/wgois/OIS/archive/refs/tags/v%{version}.tar.gz#/OIS-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)

%description
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%package -n libOIS%{sover}
Summary:        Object Oriented Input System development package
Group:          System/Libraries

%description -n libOIS%{sover}
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%package -n libOIS-devel
Summary:        Object Oriented Input System development package
Group:          Development/Libraries/C and C++
Requires:       libOIS%{sover} = %{version}

%description -n libOIS-devel
Object Oriented Input System (OIS) is a solution for using all kinds
of Input Devices (Keyboards, Mice, Joysticks, etc) and feedback
devices (e.g. forcefeedback).

%prep
%autosetup -p1 -n OIS-%{version}

%build
%cmake \
%if 0%{?sle_version} == 150200
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
%endif
  -DOIS_BUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%post   -n libOIS%{sover} -p /sbin/ldconfig
%postun -n libOIS%{sover} -p /sbin/ldconfig

%files -n libOIS%{sover}
%license LICENSE.md
%{_libdir}/libOIS.so.*

%files -n libOIS-devel
%{_includedir}/ois
%{_libdir}/libOIS.so
%{_libdir}/pkgconfig/OIS.pc

%changelog
