#
# spec file for package opentimelineio
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


Name:           opentimelineio
Version:        0.18.0
Release:        0
Summary:        API and interchange format for editorial timeline information
License:        Apache-2.0
URL:            https://github.com/AcademySoftwareFoundation/OpenTimelineIO
Source:         https://github.com/AcademySoftwareFoundation/OpenTimelineIO/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0002-CMake-fixes.patch
BuildRequires:  cmake
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cmake(RapidJSON)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Imath)

%description
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package -n libopentimelineio18
Summary:        API and interchange format for editorial timeline information

%description -n libopentimelineio18
OpenTimelineIO is an interchange format and API for editorial cut information.
OTIO contains information about the order and length of cuts and references to
external media. It is not however, a container format for media.

%package devel
Summary:        Development files for opentimelineio
Requires:       libopentimelineio18 = %{version}
# opentimelineio doesn't link to imath and will break if the soname changes
%requires_eq    Imath-devel

%description devel
Development files for opentimelineio.

%prep
%autosetup -p1 -n OpenTimelineIO-%{version}
rm -r src/deps

%build
%if 0%{?suse_version} == 1500
export CXX=g++-13
%endif

%cmake \
  -DOTIO_FIND_IMATH:BOOL=TRUE \
  -DOTIO_FIND_RAPIDJSON:BOOL=TRUE \
  -DOTIO_DEPENDENCIES_INSTALL:BOOL=FALSE

%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libopentimelineio18

%files -n libopentimelineio18
%license LICENSE.txt
%doc README.md
%{_libdir}/libopentime.so.*
%{_libdir}/libopentimelineio.so.*

%files devel
%{_includedir}/opentimelineio/
%{_includedir}/opentime/
%{_libdir}/cmake/opentime/
%{_libdir}/cmake/opentimelineio/
%{_libdir}/libopentime.so
%{_libdir}/libopentimelineio.so

%changelog

