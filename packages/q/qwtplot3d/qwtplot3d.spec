#
# spec file for package qwtplot3d
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


%define soname 0
Name:           qwtplot3d
Version:        0.2.7+git20190410.a6d0890d
Release:        0
Summary:        A feature-rich Qt/OpenGL-based C++ programming library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/copasi/copasi-dependencies/tree/master/src/qwtplot3d-qt4
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         build_a_shared_lib.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(zlib)

%description
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library. It provides essentially a bunch of 3D widgets
for programmers.

%package -n libqwtplot3d-qt5-%{soname}
Summary:        Shared library containing the QwtPlot3D Widget set
Group:          System/Libraries

%description -n libqwtplot3d-qt5-%{soname}
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library. It provides essentially a bunch of 3D widgets
for programmers.

%package devel
Summary:        Development tools for programs which uses QwtPlot3D Widget set
Group:          Development/Libraries/C and C++
Requires:       libqwtplot3d-qt5-%{soname} = %{version}

%description devel
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D widgets for programmers.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DSELECT_QT=Qt5 \
  -DWITH_ZLIB=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_libqt5_includedir}/%{name}

%make_jobs

%install
%cmake_install

%post -n libqwtplot3d-qt5-%{soname} -p /sbin/ldconfig
%postun -n libqwtplot3d-qt5-%{soname} -p /sbin/ldconfig

%files -n libqwtplot3d-qt5-%{soname}
%license COPYING
%{_libdir}/libqwtplot3d-qt5.so.*

%files devel
%license COPYING
%doc examples
%{_libdir}/libqwtplot3d-qt5.so
%{_libqt5_includedir}/qwtplot3d/

%changelog
