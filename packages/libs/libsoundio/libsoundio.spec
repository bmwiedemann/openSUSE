#
# spec file for package libsoundio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover   2
Name:           libsoundio
Version:        2.0.1
Release:        0
Summary:        A C99 library for realtime audio input/output
License:        MIT
URL:            https://libsound.io/
# Upstream tags this release as 2.0.1-7 (zig packaging revision; CMake still 2.0.0)
Source:         https://github.com/andrewrk/libsoundio/archive/%{version}-7.tar.gz#/%{name}-%{version}-7.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)

%description
This library is an abstraction; however in the delicate balance between
performance and power, and API convenience, the scale is tipped closer to
the former. Features that only exist in some sound backends are exposed.

%package -n     libsoundio%{sover}
Summary:        A C99 library for realtime audio input/output

%description -n libsoundio%{sover}
This is appropriate for games, music players, digital audio workstations, and
various utilities.

This package contains the shared library.

%package devel
Summary:        Development files for libsoundio
Requires:       libsoundio%{sover} = %{version}

%description devel
A C99 library for realtime audio input/output.

This package contains header files and libraries needed to develop
applications that use libsoundio.

%prep
%setup -q -n %{name}-%{version}-7

%build
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_EXAMPLE_PROGRAMS=OFF \
    -DBUILD_TESTS=OFF \
    -DENABLE_COREAUDIO=OFF \
    -DENABLE_WASAPI=OFF

%make_build

%install
%cmake_install

%ldconfig_scriptlets -n libsoundio%{sover}

%files -n libsoundio%{sover}
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libsoundio.so.%{sover}*

%files devel
%{_includedir}/soundio/
%{_libdir}/libsoundio.so

%changelog
