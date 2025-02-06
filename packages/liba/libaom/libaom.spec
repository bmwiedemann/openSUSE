#
# spec file for package libaom
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%else
%define psuffix -devel-doc
%endif

%define sover 3
%define __builder ninja
%define __builddir _build
Name:           libaom%{psuffix}
Version:        3.11.0
Release:        0
%if "%{flavor}" == ""
Summary:        AV1 codec library
Group:          Productivity/Multimedia/Other
%endif
%if "%{flavor}" == "doc"
Summary:        Documentation for the libaom API
Group:          Documentation/HTML
BuildArch:      noarch
%endif
License:        BSD-2-Clause
URL:            https://aomedia.googlesource.com/aom/
Source0:        libaom-%{version}.tar.zst
Source99:       baselibs.conf
Patch0:         libaom-0001-Do-not-disable-_FORTIFY_SOURCE.patch
Patch1:         system-gtest.patch
Patch2:         system-yuv.patch

BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.9
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libyuv)
%ifarch x86_64 %ix86
BuildRequires:  yasm
%endif

%if "%{flavor}" == "doc"
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
%endif

%description
%if "%{flavor}" == ""
This is a library for AOMedia Video 1 (AV1), an open, royalty-free
video coding format designed for video transmissions over the Internet.
%endif
%if "%{flavor}" == "doc"
This package contains the API documentation for libaom, a library
for the AOMedia Video 1 (AV1) video coding format.
%endif

%if "%{flavor}" == ""
%package -n %{name}%{sover}
Summary:        AV1 codec library
Group:          System/Libraries

%description -n %{name}%{sover}
This is a library for AOMedia Video 1 (AV1), an open, royalty-free
video coding format designed for video transmissions over the Internet.

%package devel
Summary:        Development files for libaom, an AV1 codec library
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover}%{_isa} = %{version}

%description devel
This package contains the development headers and library files for
libaom, a library for the AOMedia Video 1 (AV1) video coding format.

%package -n aom-tools
Summary:        AV1 Codec Library Tools
Group:          Productivity/Multimedia/Other

%description -n aom-tools
This package contains tools included with libaom, a library for
the AOMedia Video 1 (AV1) video coding format.
%endif

%prep
%autosetup -n libaom-%{version} -p1
sed -E -i 's|#include "third_party/googletest/src/googletest/include/([^"]*)"|#include <\1>|' test/*.{cc,h}

%build
%cmake \
    -DAOM_AS_FLAGS=-gdwarf2 \
%if "%{flavor}" == ""
    -DENABLE_DOCS=OFF \
%endif
`# Do not build unit tests, they require non-free external files.` \
    -DENABLE_TESTS=OFF \
    -DENABLE_TESTDATA=OFF \
\
	-DCONFIG_LOWBITDEPTH=1 \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
%ifnarch aarch64 %arm %ix86 x86_64 %x86_64 ppc %power64
	-DAOM_TARGET_CPU=generic \
%endif
%ifarch %arm
`# see regex in build/cmake/rtcd.pl (this actually work for armv6hl too)` \
	-DAOM_TARGET_CPU=armv7 \
`# Fix missing flag for neon code` \
`# See aom_ports/arm_cpudetect.c` \
	-DENABLE_NEON=ON \
	-DAOM_NEON_INTRIN_FLAG=-mfpu=neon \
%endif
%ifarch aarch64
	-DAOM_TARGET_CPU=arm64 \
%endif
%ifarch ppc %power64
	-DAOM_TARGET_CPU=ppc \
%endif
%ifarch %ix86
	-DAOM_TARGET_CPU=x86 \
%endif
%ifarch x86_64 %x86_64
	-DAOM_TARGET_CPU=x86_64 \
%endif
	%{nil}

%if "%{flavor}" == ""
%cmake_build
%endif

%if "%{flavor}" == "doc"
%cmake_build docs
%endif

%install
%if "%{flavor}" == ""
%cmake_install
rm %{buildroot}%{_libdir}/%{name}.a

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE PATENTS
%doc AUTHORS CHANGELOG
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/aom
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/aom.pc

%files -n aom-tools
%{_bindir}/aomdec
%{_bindir}/aomenc

%endif

%if "%{flavor}" == "doc"
%files
%doc %{__builddir}/docs/html/*
%endif

%changelog
