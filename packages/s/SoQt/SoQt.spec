#
# spec file for package SoQt
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


%define         sover 20
%define         realver 1.6.0
Name:           SoQt
Version:        1.6~pre.2047
Release:        0
Summary:        A library which provides the glue between Coin and Qt
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://bitbucket.org/Coin3D/coin/wiki/Home
Source:         soqt-%{version}.tar.xz
Patch0:         SoQt-man3.patch
#PATCH-FIX-OPENSUSE 0001-Use-a-Find-module-to-find-older-Coin-versions.patch -- use a SoQt snapshot with a stable Coin package
Patch1:         0001-Use-a-Find-module-to-find-older-Coin-versions.patch
BuildRequires:  Coin-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)

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
Requires:       Coin-devel
Requires:       Mesa-devel
Requires:       libSoQt%{sover}
Requires:       libpng-devel
Requires:       cmake(Qt5Gui)
Requires:       cmake(Qt5OpenGL)
Requires:       cmake(Qt5Widgets)

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
%setup -q -n soqt-%{version}
%patch0
%patch1 -p1

%build
# using the cmake macro leads to compile errors
mkdir my_build
cd my_build
cmake .. \
      -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_PREFIX_PATH=%{_datadir}/cmake/Modules \
      -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \
      -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{name} \
      -DCMAKE_SKIP_RPATH:BOOL=ON \
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
      -DBUILD_SHARED_LIBS:BOOL=ON \
      -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
      -DCoin_DOC_DIR=%{_docdir}/Coin
make %{?_smp_mflags}

%install
cd my_build
%make_install

%fdupes %{buildroot}%{_prefix}

%post -n libSoQt%{sover} -p /sbin/ldconfig
%postun -n libSoQt%{sover} -p /sbin/ldconfig

%files -n libSoQt%{sover}
%license COPYING
%doc AUTHORS README
%{_libdir}/libSoQt.so.*

%files doc
%{_docdir}/SoQt

%files devel
%dir %{_includedir}/Inventor/Qt
%{_includedir}/Inventor/Qt/*
%{_datadir}/SoQt
%{_libdir}/libSoQt.so
%{_libdir}/cmake/%{name}-%{realver}/
%{_libdir}/pkgconfig

%changelog
