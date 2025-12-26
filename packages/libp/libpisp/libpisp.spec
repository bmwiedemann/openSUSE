#
# spec file for package libpisp
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define soversion 1

Name:           libpisp
Version:        1.3.0
Release:        0
Summary:        RPi ISP helper library
Group:          System/Libraries
License:        BSD-2-Clause
URL:            https://github.com/raspberrypi/libpisp
Source:         https://github.com/raspberrypi/libpisp/archive/refs/tags/v%{version}.tar.gz#/libpisp-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  libboost_log-devel
%if 0%{?suse_version} <= 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libboost_thread-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(nlohmann_json)

%description
A helper library to generate run-time configuration for the Raspberry Pi
ISP (PiSP), consisting of the Frontend and Backend hardware components.

%package -n libpisp%{soversion}
Summary:        RPi ISP helper library

%description -n libpisp%{soversion}
A helper library to generate run-time configuration for the Raspberry Pi
ISP (PiSP), consisting of the Frontend and Backend hardware components.

%package devel
Summary:        Development files for the RPi ISP helper library
Group:          Development/Libraries/C and C++
Requires:       libpisp%{soversion} = %{version}

%description devel
A helper library to generate run-time configuration for the Raspberry Pi
ISP (PiSP), consisting of the Frontend and Backend hardware components.

This package contains the header files and other files required for development.

%prep
%autosetup -p1

%build
%meson \
    -Dlogging=enabled \
    -Dexamples=false \
    %{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libpisp%{soversion}

%files -n libpisp%{soversion}
%license LICENSE
%{_libdir}/libpisp.so.%{soversion}.*
%{_libdir}/libpisp.so.%{soversion}
%{_datadir}/libpisp

%files devel
%doc README.md
%{_includedir}/libpisp
%{_libdir}/libpisp.so
%{_libdir}/pkgconfig/libpisp.pc

%changelog

