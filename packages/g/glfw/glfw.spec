#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "-wayland"
%bcond_without wayland
%else
%bcond_with wayland
%endif
%define sover  3
Name:           glfw%{flavor}
Version:        3.3.8
Release:        0
Summary:        Framework for OpenGL application development
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://www.glfw.org/
Source:         https://github.com/glfw/glfw/archive/%{version}.tar.gz#/glfw-%{version}.tar.gz
Source99:       glfw-rpmlintrc
BuildRequires:  cmake >= 3.0
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
%if %{with wayland}
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
%else
BuildRequires:  geany
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
%endif

%description
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%package -n libglfw%{sover}%{flavor}
Summary:        Framework for OpenGL application development
Group:          System/Libraries
%if %{with wayland}
Provides:       libglfw%{sover} = %{version}
Conflicts:      libglfw%{sover}
%else
Conflicts:      libglfw%{sover}-wayland = %{version}
%endif

%description -n libglfw%{sover}%{flavor}
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%if %{without wayland}
%package -n libglfw%{flavor}-devel
Summary:        Development files for GLFW, an OpenGL application framework
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libglfw%{sover} = %{version}
Requires:       pkgconfig(gl)

%description -n libglfw%{flavor}-devel
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.
%endif

%prep
%setup -q -n glfw-%{version}
find . -type f | xargs sed -i 's/\r//'

# temp geany config directory for allow geany to generate tags
mkdir -p geany_config

%build
%if %{without wayland}
# generate geany tags
geany -c geany_config -g glfw.c.tags $(find src \( ! -name CMakeFiles \) -type f \( -iname "*.c" -o -iname "*.h" \) \( ! -iname "win32*" \) \( ! -iname "cocoa*" \) | sort
) include/GLFW/glfw3.h
%endif

%cmake \
%if %{with wayland}
  -DGLFW_USE_WAYLAND=ON
%endif

%make_build

%install
%cmake_install

%if %{with wayland}
# Only in main package
rm -rfv %{buildroot}%{_includedir} %{buildroot}%{_libdir}/{cmake,libglfw.so,pkgconfig}
%else
# install geany tags
install -d %{buildroot}/%{_datadir}/geany/tags/
install -m0644 glfw.c.tags %{buildroot}/%{_datadir}/geany/tags/
%endif

%post   -n libglfw%{sover}%{flavor} -p /sbin/ldconfig
%postun -n libglfw%{sover}%{flavor} -p /sbin/ldconfig

%files -n libglfw%{sover}%{flavor}
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.%{sover}*

%if %{without wayland}
%files -n libglfw-devel
%doc examples/*.c
%{_includedir}/GLFW/
%{_libdir}/cmake/glfw3
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_datadir}/geany/*
%endif

%changelog
