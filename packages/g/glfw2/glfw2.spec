#
# spec file for package glfw2
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


Name:           glfw2
Version:        2.7.6
Release:        0
Summary:        Portable framework for OpenGL application development
License:        Zlib
Group:          Development/Libraries/C and C++
%define sover  2
URL:            http://glfw.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/glfw/glfw-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE glfw-2.7.6-soname.diff lnussel@suse.de -- add sover to shared library
Patch0:         glfw-2.7.6-soname.diff
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xrandr)

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

%package devel
Summary:        Development files for GLFW, an OpenGL application framework
Group:          Development/Libraries/C and C++
Requires:       libglfw%{sover} = %{version}

%description -n glfw2-devel
GLFW is a framework for OpenGL application development. It is a
single library providing a powerful, portable API for otherwise
operating system specific tasks such as opening an OpenGL window, and
reading keyboard, time, mouse and joystick input.

%prep
%autosetup -p1 -n glfw-%version

%build
CFLAGS="%{optflags}" \
sh ./compile.sh

pushd lib/x11
%make_build -f Makefile.x11 \
    PREFIX="%{_prefix}" \
    libglfw.so \
    libglfw.pc
popd
sed -i -e 's,libdir=.*,libdir=%_libdir/glfw2,' lib/x11/libglfw.pc

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/GL
install -Dm 644 lib/x11/libglfw.pc %{buildroot}%{_libdir}/pkgconfig/libglfw.pc
install -m 644 include/GL/* %{buildroot}/%{_includedir}/GL

install -D -m0755 lib/x11/libglfw.so "%{buildroot}%{_libdir}/libglfw.so.%{version}"
ln -s libglfw.so.%{version} "%{buildroot}%{_libdir}/libglfw.so.%{sover}"

install -d -m0755 "%{buildroot}%{_libdir}/glfw2"
ln -s ../libglfw.so.%{version} "%{buildroot}%{_libdir}/glfw2/libglfw.so"

%ldconfig_scriptlets -n libglfw%{sover}

%files -n libglfw%{sover}
%license COPYING.txt
%{_libdir}/libglfw.so.*

%files devel
%doc readme.html
%{_includedir}/GL/glfw.h
%dir %{_libdir}/glfw2
%{_libdir}/glfw2/libglfw.so
%{_libdir}/pkgconfig/libglfw.pc

%changelog
