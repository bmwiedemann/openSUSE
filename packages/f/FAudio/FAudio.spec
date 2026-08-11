#
# spec file for package FAudio
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


%define sover 0
Name:           FAudio
Version:        26.08
Release:        0
Summary:        Accuracy-focused XAudio reimplementation
License:        Zlib
URL:            https://fna-xna.github.io
Source0:        https://github.com/FNA-XNA/FAudio/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig
# Upstream README: "FAudio depends solely on SDL 3.2.0 or newer"
BuildRequires:  cmake(SDL3) >= 3.2.0

%description
FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project,
including XAudio2, X3DAudio, XAPO and XACT3.

%package -n libFAudio%{sover}
Summary:        Accuracy-focused XAudio reimplementation

%description -n libFAudio%{sover}
FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project,
including XAudio2, X3DAudio, XAPO and XACT3.

%package devel
Summary:        Development files for FAudio
Requires:       libFAudio%{sover} = %{version}

%description devel
Header files, pkg-config and CMake package files needed to build
applications against FAudio.

%prep
%autosetup -p1

%build
%cmake \
  -DBUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
# The unit tests exercise the XAudio2 API surface and only need an audio
# device to open, not to produce sound - the SDL dummy driver is enough.
SDL_AUDIODRIVER=dummy build/faudio_tests

%ldconfig_scriptlets -n libFAudio%{sover}

%files -n libFAudio%{sover}
%license LICENSE
%{_libdir}/libFAudio.so.%{sover}
%{_libdir}/libFAudio.so.%{sover}.*

%files devel
%license LICENSE
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FACT3D.h
%{_includedir}/FAPO.h
%{_includedir}/FAPOBase.h
%{_includedir}/FAPOFX.h
%{_includedir}/FAudio.h
%{_includedir}/FAudioFX.h
%{_libdir}/libFAudio.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/FAudio/
%{_libdir}/pkgconfig/FAudio.pc

%changelog
