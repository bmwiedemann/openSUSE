#
# spec file for package noopenh264
#
# Copyright (c) 2025 Bjørn Lie
# Copyright (c) 2025 Neal Gompa
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

%define somajor 8
%define origname openh264
%define libname lib%{origname}-%{somajor}
%define devname lib%{origname}-devel
%define basever 2.6.0

Name:           noopenh264
# Mangle the version to allow the real implementation to upgrade over it
Version:        %{basever}~noopenh264
Release:        0
Summary:        Fake implementation of the OpenH264 library
License:        BSD-2-Clause and LGPL-2.1-or-later
URL:            https://codeberg.org/distro-openh264/noopenh264
Source0:        %{url}/archive/v%{basever}.tar.gz#/%{name}-%{basever}.tar.gz

Source10:       baselibs.conf

BuildRequires:  c++_compiler
BuildRequires:  meson

%description
Fake implementation of the OpenH264 library we can link from
regardless of the actual library being available.

%package        -n %{libname}
Summary:        H.264 codec library (dummy implementation)

%description    -n %{libname}
OpenH264 is a codec library which supports H.264 encoding and
decoding. It is suitable for use in real time applications such as
WebRTC.

This package contains a dummy implementation for applications to
link to OpenH264.

%package        -n %{devname}
Summary:        Development files for OpenH264 (dummy implementation)
Provides:       %{name}-devel = %{basever}
Requires:       %{libname} = %{version}-%{release}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use OpenH264 through this dummy
implementation.

%prep
%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install
# Remove static library
find %{buildroot} -type f -name "*.a" -delete -print

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING*
%doc README
%{_libdir}/libopenh264.so.%{somajor}
%{_libdir}/libopenh264.so.%{basever}

%files -n %{devname}
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%changelog
