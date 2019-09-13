#
# spec file for package glfw
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover  3
%if 0%{?is_opensuse}
%bcond_without geany
%else
%bcond_with geany
%endif
Name:           glfw
Version:        3.3
Release:        0
Summary:        Framework for OpenGL application development
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.glfw.org/
Source:         https://github.com/glfw/glfw/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.12
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
%if 0%{?suse_version} > 1320
BuildRequires:  vulkan-devel
%endif
%if %{with geany}
BuildRequires:  geany
%endif

%description
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%package -n libglfw%{sover}
Summary:        Framework for OpenGL application development
Group:          System/Libraries

%description -n libglfw%{sover}
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%package -n libglfw-devel
Summary:        Development files for GLFW, an OpenGL application framework
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libglfw%{sover} = %{version}

%description -n libglfw-devel
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%prep
%setup -q
find . -type f | xargs sed -i 's/\r//'

# temp geany config directory for allow geany to generate tags
mkdir -p geany_config

%build
# generate geany tags
%if %{with geany}
geany -c geany_config -g glfw.c.tags $(find src \( ! -name CMakeFiles \) -type f \( -iname "*.c" -o -iname "*.h" \) \( ! -iname "win32*" \) \( ! -iname "cocoa*" \) | sort
) include/GLFW/glfw3.h
%endif

%cmake
make %{?_smp_mflags} all

%install
%cmake_install

# install geany tags
%if %{with geany}
install -d %{buildroot}/%{_datadir}/geany/tags/
install -m0644 glfw.c.tags %{buildroot}/%{_datadir}/geany/tags/
%endif

%post   -n libglfw%{sover} -p /sbin/ldconfig
%postun -n libglfw%{sover} -p /sbin/ldconfig

%files -n libglfw%{sover}
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.%{sover}*

%files -n libglfw-devel
%doc examples/*.c
%{_includedir}/GLFW/
%{_libdir}/cmake/glfw3
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%if %{with geany}
%{_datadir}/geany/
%endif

%changelog
