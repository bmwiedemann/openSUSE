#
# spec file for package raylib
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


Name:           raylib
Version:        5.5
Release:        0
Summary:        C library for learning video game programming
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://www.raylib.com
Source:         raylib-%{version}.tar.xz
BuildRequires:  Mesa-libGL-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
# raylib ships an in-tree glfw that is a copy of *a* git revision of upstream glfw
# containing features they need. They are unhappy that it takes such
# a long time for 3.4 to be released. So ship it.
#BuildRequires:  libglfw-devel >= 3.4

%description
A C library for learning video game programming.
raylib is inspired by the Borland BGI graphics library and by the XNA framework.

%package -n raylib-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libraylib550 = %{version}
Requires:       openal-soft-devel

%description -n raylib-devel
Development files and headers for %{name}.

%package -n libraylib550
Summary:        C library for learning video game programming
Group:          System/Libraries

%description -n libraylib550
A C library for learning video game programming.

%prep
%setup -q

%build
%cmake \
  -DBUILD_EXAMPLES=OFF \
  -DPLATFORM=Desktop \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_BUILD_TYPE=Release \
  -DOpenGL_GL_PREFERENCE=GLVND \
  -DUSE_EXTERNAL_GLFW=OFF

%install
%cmake_install

%post -n libraylib550 -p /sbin/ldconfig
%postun -n libraylib550 -p /sbin/ldconfig

%files -n libraylib550
%license LICENSE
%{_libdir}/libraylib.so.*

%files -n raylib-devel
%doc CHANGELOG README.md
%{_includedir}/raylib.h
%{_includedir}/raymath.h
%{_includedir}/rlgl.h
%{_libdir}/libraylib.so
%{_libdir}/pkgconfig/raylib.pc
%{_libdir}/cmake/raylib/

%changelog
