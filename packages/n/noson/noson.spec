#
# spec file for package noson
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


Name:           noson
Version:        2.10.1
Release:        0
Summary:        C++ library for accessing sonos devices
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/janbar/noson/
Source0:        https://github.com/janbar/noson/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM noson-include-time.h.patch gh#janbar/noson#16 -- Fix build with gcc 12.1
Patch0:         noson-include-time.h.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libpulse-devel
BuildRequires:  zlib-devel

%description
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package -n libnoson2
Summary:        C++ library for accessing sonos devices
Group:          System/Libraries

%description -n libnoson2
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package devel
Summary:        Development files for noson library
Group:          Development/Libraries/C and C++
Requires:       libnoson2 = %{version}

%description devel
Development files for noson library. The noson library supports basic features
to browse music index and control playback in any zones.

%prep
%autosetup -p1

%build
  %cmake \
    -DCMAKE_INSTALL_FULL_LIBDIR=%{_libdir}
  %make_jobs

%install
  %make_install -C build

%post -n libnoson2 -p /sbin/ldconfig
%postun -n libnoson2 -p /sbin/ldconfig

%files -n libnoson2
%license LICENSE
%doc README.md
%{_libdir}/libnoson.so.%{version}
%{_libdir}/libnoson.so.2

%files devel
%{_includedir}/noson
%{_libdir}/pkgconfig/noson.pc
%{_libdir}/cmake/noson/
%{_libdir}/libnoson.so

%changelog
