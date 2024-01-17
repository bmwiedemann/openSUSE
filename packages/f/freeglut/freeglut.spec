#
# spec file for package freeglut
#
# Copyright (c) 2022 SUSE LLC
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


%define _libname libglut3
Name:           freeglut
Version:        3.2.2
Release:        0
Summary:        Freely licensed alternative to the GLUT library
License:        MIT
URL:            http://freeglut.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/freeglut/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/openglut/openglut-0.6.3-doc.tar.gz
Source2:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
Recommends:     Mesa-demo-x
Provides:       mesaglut = 7.11
Obsoletes:      mesaglut < 7.11

%description
Freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library. GLUT was originally written by Mark Kilgard to
support the sample programs in the second edition OpenGL Redbook. Since
then, GLUT has been used in a wide variety of practical applications
because it is simple, universally available, and highly portable.

GLUT (and freeglut) allow the user to create and manage windows
containing OpenGL contexts and also read the mouse, keyboard, and
joystick functions on a wide range of platforms.

%package -n %{_libname}
Summary:        Freely licensed alternative to the GLUT library

%description -n %{_libname}
Freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library. GLUT was originally written by Mark Kilgard to
support the sample programs in the second edition OpenGL Redbook. Since
then, GLUT has been used in a wide variety of practical applications
because it is simple, universally available, and highly portable.

GLUT (and freeglut) allow the user to create and manage windows
containing OpenGL contexts and also read the mouse, keyboard, and
joystick functions on a wide range of platforms.

%package devel
Summary:        Development libraries, includes and man pages for freeglut (GLUT Library)
Requires:       %{_libname} = %{version}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Provides:       mesaglut-devel = 7.11
Obsoletes:      mesaglut-devel < 7.11

%description devel
This package contains all necessary include files and libraries needed
to compile and link applications for the freeglut library.

In addition, it also includes manual pages which describe all functions
provided by the freeglut library.

Freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library. GLUT was originally written by Mark Kilgard to
support the sample programs in the second edition OpenGL Redbook. Since
then, GLUT has been used in a wide variety of practical applications
because it is simple, universally available, and highly portable.

GLUT (and freeglut) allow the user to create and manage windows
containing OpenGL contexts and also read the mouse, keyboard, and
joystick functions on a wide range of platforms.

%package demo
Summary:        Demonstration applications for the freeglut library

%description demo
This package contains demonstration applications for the freeglut library.

Freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library. GLUT was originally written by Mark Kilgard to
support the sample programs in the second edition OpenGL Redbook. Since
then, GLUT has been used in a wide variety of practical applications
because it is simple, universally available, and highly portable.

GLUT (and freeglut) allow the user to create and manage windows
containing OpenGL contexts and also read the mouse, keyboard, and
joystick functions on a wide range of platforms.

%prep
%setup -q -a1

%build
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DFREEGLUT_BUILD_STATIC_LIBS=OFF
%cmake_build

%install
%cmake_install

# install demo files
install -d %{buildroot}%{_libexecdir}/freeglut
pushd build/bin/ > /dev/null
for i in *; do
    install $i %{buildroot}%{_libexecdir}/freeglut/$i
done
popd > /dev/null

# glut manpages
mkdir -p %{buildroot}/%{_mandir}/man3
install -p -m 644 doc/man/*.3 $RPM_BUILD_ROOT/%{_mandir}/man3

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%files -n %{_libname}
%license COPYING
%doc AUTHORS README
%{_libdir}/libglut.so.*

%files devel
%{_includedir}/GL
%{_libdir}/libglut.so
%{_libdir}/pkgconfig/glut.pc
%dir %{_libdir}/cmake/FreeGLUT
%{_libdir}/cmake/FreeGLUT/*
%{_mandir}/man3/*

%files demo
%{_libexecdir}/freeglut

%changelog
