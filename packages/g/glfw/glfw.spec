#
# spec file for package glfw
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


# html docs need doxygen >= 1.9.8 which isn't available on Leap
%if 0%{?suse_version} >= 1600
%bcond_without html_docs
%else
%bcond_with html_docs
%endif
# On TW and ALP, build with geany by default
%if 0%{?suse_version} >= 1600
%bcond_without geany
%else
%bcond_with geany
%endif
%define sover  3
Name:           glfw
Version:        3.4
Release:        0
Summary:        Framework for OpenGL application development
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://www.glfw.org/
Source:         https://github.com/glfw/glfw/archive/%{version}.tar.gz#/glfw-%{version}.tar.gz
# PATCH-FIX-OPENSUSE docs-remove-footer.patch antonio.teixeira@suse.com -- Custom footer for html docs includes build date and time. Use default footer instead.
Patch1:         docs-remove-footer.patch
BuildRequires:  cmake >= 3.0
%if %{with html_docs}
BuildRequires:  doxygen >= 1.9.8
BuildRequires:  fdupes
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
%if %{with geany}
BuildRequires:  geany
%endif
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%description
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%package -n libglfw%{sover}
Summary:        Framework for OpenGL application development
Group:          System/Libraries
Provides:       libglfw%{sover}-wayland = %{version}
Obsoletes:      libglfw%{sover}-wayland < %{version}

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
Requires:       pkgconfig(gl)

%description -n libglfw-devel
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%if %{with html_docs}
%package doc
Summary:        Documentation for GLFW, an OpenGL application framework
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

This subpackage contains GLFW's documentation in html format.
%endif

%prep
%autosetup -p1 -n glfw-%{version}
find . -type f | xargs sed -i 's/\r//'

# temp geany config directory for allow geany to generate tags
mkdir -p geany_config

%build
%if %{with geany}
# generate geany tags
geany -c geany_config -g glfw.c.tags $(find src \( ! -name CMakeFiles \) -type f \( -iname "*.c" -o -iname "*.h" \) \( ! -iname "win32*" \) \( ! -iname "cocoa*" \) | sort
) include/GLFW/glfw3.h
%endif

%cmake

%make_build

%install
%cmake_install

%if %{with html_docs}
%fdupes -s %{buildroot}/%{_docdir}/%{name}
%endif
%if %{with geany}
# install geany tags
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
%{_datadir}/geany/*
%endif

%if %{with html_docs}
%files doc
%{_docdir}/%{name}/
%endif

%changelog
