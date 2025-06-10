#
# spec file for package plutosvg
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


%define soversion 0
Name:           plutosvg
Version:        0.0.7
Release:        0
Summary:        Tiny SVG rendering library in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/sammycage/plutosvg
Source:         https://github.com/sammycage/plutosvg/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(plutovg)
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
# it's either one of the other
#BuildRequires:  pkgconfig(plutovg)

%description
PlutoSVG is a compact and efficient SVG rendering library written in C.
It is specifically designed for parsing and rendering SVG documents embedded in OpenType fonts,
providing an optimal balance between speed and minimal memory usage.
It is also suitable for rendering scalable icons.

%package -n     lib%{name}%{soversion}
Summary:        Tiny SVG rendering library in C

%description -n lib%{name}%{soversion}
PlutoSVG is a compact and efficient SVG rendering library written in C.
It is specifically designed for parsing and rendering SVG documents embedded in OpenType fonts,
providing an optimal balance between speed and minimal memory usage.
It is also suitable for rendering scalable icons.

%package        devel
Summary:        Development files for %{name}, an SVG rendering library in C
Requires:       lib%{name}%{soversion} = %{version}
Requires:       cmake(plutovg)

%description    devel
The %{name}-devel package contains header files for
developing application that use %{name}.
PlutoSVG is an SVG rendering library written in C.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fPIC -O3 -ftree-parallelize-loops=4 -ftree-vectorize -fpredictive-commoning"
export CXXFLAGS="%{optflags}"
export LDFLAGS="${LDFLAGS} -Wl,-lm"
%cmake \
	-DCMAKE_C_FLAGS="${CFLAGS}" \
	-DCMAKE_CXX_FLAGS="${CXXFLAGS}" \
	-DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS}" \
	-DCMAKE_MODULE_LINKER_FLAGS="${LDFLAGS}" \
	-DCMAKE_SHARED_LINKER_FLAGS="${LDFLAGS}"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}%{soversion}

%files -n lib%{name}%{soversion}
%license LICENSE
%{_libdir}/lib%{name}.so.%{soversion}*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake
%{_libdir}/pkgconfig/*

%changelog
