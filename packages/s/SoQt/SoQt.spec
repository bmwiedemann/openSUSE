#
# spec file for package SoQt
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


%define         sover 20
%define         realver 1.6.3
Name:           SoQt
Version:        1.6.3
Release:        0
Summary:        A library which provides the glue between Coin and Qt
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://coin3d.github.io/SoQt/html/
Source:         https://github.com/coin3d/soqt/releases/download/v%{version}/soqt-%{version}-src.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(coin)

%description
The core rendering library Coin is a multiplatform high-level 3D graphics
library with a C++ API. Coin uses OpenGL for accelerated rendering, while
providing a higher abstraction level, 3D interactivity, and many complex
optimization features for fast rendering that are transparent for the
application programmer, thus facilitating the development of interactive 3D
applications and greatly increasing productivity.

%package devel
Summary:        Development files for SoQt
Group:          Development/Libraries/C and C++
Requires:       libSoQt%{sover}
Requires:       libpng-devel
Requires:       cmake(Qt5Gui)
Requires:       cmake(Qt5OpenGL)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(coin)

%description devel
By using the combination of Coin, Qt and SoQt for your 3D applications, you
have a framework for writing completely portable software across the whole range
of UNIX, Linux, Microsoft Windows and Mac OS X operating systems. Coin, Qt and
SoQt makes this possible from a 100% common codebase, which means there is a
minimum of hassle for developers when working on multiplatform software, with
the resulting large gains in productivity.

%package doc
Summary:        API documentation for SoQt
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
By using the combination of Coin, Qt and SoQt for your 3D applications, you
have a framework for writing completely portable software across the whole range
of UNIX, Linux, Microsoft Windows and Mac OS X operating systems. Coin, Qt and
SoQt makes this possible from a 100% common codebase, which means there is a
minimum of hassle for developers when working on multiplatform software, with
the resulting large gains in productivity.

%package -n libSoQt%{sover}
Summary:        A library which provides the glue between Coin and Qt
Group:          System/Libraries

%description -n libSoQt%{sover}
By using the combination of Coin, Qt and SoQt for your 3D applications, you
have a framework for writing completely portable software across the whole range
of UNIX, Linux, Microsoft Windows and Mac OS X operating systems. Coin, Qt and
SoQt makes this possible from a 100% common codebase, which means there is a
minimum of hassle for developers when working on multiplatform software, with
the resulting large gains in productivity.

%prep
%setup -q -n soqt
# Fix broken Qt4 requires in pkgconfig file
sed -i -e '/Requires:/ s/Qt\([^ ,]*\)/Qt5\1/g' SoQt.pc.cmake.in

%build
# default __builddir clashes with existing "build" dir
%global __builddir my_build
%cmake .. \
      -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
      -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/Coin4/ \
      -DSOQT_BUILD_DOCUMENTATION=TRUE \
      -DSOQT_BUILD_DOC_MAN=TRUE \
      %{nil}
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_prefix}

%post -n libSoQt%{sover} -p /sbin/ldconfig
%postun -n libSoQt%{sover} -p /sbin/ldconfig

%files -n libSoQt%{sover}
%license COPYING
%doc AUTHORS README
%{_libdir}/libSoQt.so.%{sover}*
%{_libdir}/libSoQt.so.*

%files doc
%{_docdir}/SoQt

%files devel
%{_datadir}/SoQt
%dir %{_includedir}/Coin4/Inventor/Qt
%{_includedir}/Coin4/Inventor/Qt/*
%{_libdir}/cmake/%{name}-%{realver}/
%{_libdir}/libSoQt.so
%{_libdir}/pkgconfig/SoQt.pc
%{_mandir}/man3/*

%changelog
