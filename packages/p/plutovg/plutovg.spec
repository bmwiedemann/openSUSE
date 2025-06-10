#
# spec file for package plutovg
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


%define soversion 1
Name:           plutovg
Version:        1.1.0
Release:        0
Summary:        Tiny 2D vector graphics library in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/sammycage/%{name}
Source:         https://github.com/sammycage/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
PlutoVG is a standalone 2D vector graphics library in C.

Features:
* Path Filling, Stroking and Dashing
* Soild, Gradient and Texture Paints
* Fonts and Texts
* Clipping and Compositing
* Transformations
* Images

%package -n     lib%{name}%{soversion}
Summary:        Tiny 2D vector graphics library in C

%description -n lib%{name}%{soversion}
PlutoVG is a standalone 2D vector graphics library in C.

Features:
* Path Filling, Stroking and Dashing
* Soild, Gradient and Texture Paints
* Fonts and Texts
* Clipping and Compositing
* Transformations
* Images

%package        devel
Summary:        Development files for %{name}, a vector graphics library
Requires:       lib%{name}%{soversion} = %{version}

%description    devel
The %{name}-devel package contains header files for
developing application that use %{name}.
PlutoVG is a standalone 2D vector graphics library in C.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fPIC -O3 -ftree-parallelize-loops=4 -ftree-vectorize -fpredictive-commoning"
%ifarch x86_64
export CFLAGS="${CFLAGS} -march=x86-64-v2 -mtune=generic -mssse3 -msse4 -msse4.1 -msse4.2 -mavx -maes -mpclmul"
%endif
export CXXFLAGS="%{optflags}"
%cmake
%cmake_build

%ldconfig_scriptlets -n lib%{name}%{soversion}

%install
%cmake_install

%files -n lib%{name}%{soversion}
%license LICENSE
%{_libdir}/lib%{name}.so.%{soversion}*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake
%{_libdir}/pkgconfig/*

%changelog
