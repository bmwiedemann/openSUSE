#
# spec file for package sonivox
#
# Copyright (c) 2024 SUSE LLC
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


%define soversion 3
Name:           sonivox
Version:        3.6.16
Release:        0
Summary:        Fork of the AOSP 'platform_external_sonivox' project
License:        Apache-2.0
URL:            https://github.com/pedrolcl/sonivox
Source:         https://github.com/pedrolcl/sonivox/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.14
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
BuildRequires:  gcc13-PIE
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(GTest)

%description
Sonivox is a fork of the Android Open Source Project 'platform_external_sonivox'
including a CMake based build system to be used not on Android, but on any other
Operating System.

This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.
It may be indicated in projects for small embedded devices. There is neither
MIDI input nor Audio output facilities included in the library. You need to
provide your own input/output.

%package -n libsonivox%{soversion}
Summary:        Fork of the AOSP 'platform_external_sonivox' project

%description -n libsonivox%{soversion}
Sonivox is a fork of the Android Open Source Project 'platform_external_sonivox'
including a CMake based build system to be used not on Android, but on any other
Operating System.

This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.
It may be indicated in projects for small embedded devices. There is neither
MIDI input nor Audio output facilities included in the library. You need to
provide your own input/output.

%package devel
Summary:        Sonivox library - Development files
Requires:       libsonivox%{soversion} = %{version}

%description devel
Development files for the sonivox library.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
export CC=gcc-13 CXX=g++-13
%endif

%cmake -DBUILD_SONIVOX_STATIC:BOOL=FALSE \
       -DBUILD_EXAMPLE:BOOL=FALSE \
       -DBUILD_TESTING:BOOL=FALSE

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libsonivox%{soversion}

%files -n libsonivox%{soversion}
%license LICENSE
%{_libdir}/libsonivox.so.*

%files devel
%{_includedir}/sonivox/
%{_libdir}/cmake/sonivox/
%{_libdir}/libsonivox.so
%{_libdir}/pkgconfig/sonivox.pc

%changelog
