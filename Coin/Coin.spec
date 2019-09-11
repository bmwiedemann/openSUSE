#
# spec file for package Coin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 60

Name:           Coin
Version:        3.1.3
Release:        0
Summary:        Scene-graph based retain-mode 3D graphics library
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.coin3d.org/lib/coin/
Source0:        https://bitbucket.org/Coin3D/coin/downloads/%{name}-%{version}.tar.gz
Patch0:         0012-memhandler-initialization.patch
# X-OPENSUSE-PATCH: Coin60.patch -- hack around library policy names
Patch1:         Coin60.patch
Patch2:         Coin.patch
BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

%package devel
Summary:        Development files for Coin, a 3D graphics library
Group:          Development/Libraries/C and C++
Requires:       fontconfig-devel
Requires:       freetype2-devel
Requires:       libCoin%{soname} = %{version}
Requires:       openal-soft-devel
Requires:       zlib-devel
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(ice)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xt)

%description devel
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

This subpackage contains libraries and header files for developing
applications that want to make use of Coin.

%package -n libCoin%{soname}
Summary:        Scene-graph based retain-mode 3D graphics library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libCoin%{soname}
Coin is a scene-graph based, retain-mode, rendering and model
manipulation C++ class library that uses OpenGL for its 3D graphics.
Coin is compatible to Open Inventor 2.1 and also has support for 3D
sound, GLSL shaders, and additional file formats like VRML97.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
sed -i '/^#include "fonts\/freetype.h"$/i #include <cstdlib>\n#include <cmath>' src/fonts/freetype.cpp
sed -i '/^#include <Inventor\/C\/basic.h>$/i #include <Inventor/C/errors/debugerror.h>' include/Inventor/SbBasic.h

# Remove build time references so build-compare can do its work
sed -i "s/Generated on \$datetime/Generated/" docs/doxygen/footer.html

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%configure \
    --htmldir=%{_docdir}/%{name}-devel/html \
    --enable-3ds-import \
    --enable-javascript-api \
    --enable-threadsafe \
    --enable-html \
    --enable-man \
    --disable-dl-openal \
    --disable-dl-fontconfig \
    --disable-dl-freetype \
    --disable-dl-zlib \
    --disable-dl-libbzip2 \
    --disable-dl-glu \
    --with-freetype=%{_prefix}

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# avoid conflicting man page
rm %{buildroot}/usr/share/man/man3/deprecated.*

# Fix rpmlint warning "pkgconfig-invalid-libs-dir". -L${libdir} is already included in the Coin.pc file
sed -i "s/\-L\/usr\/lib64 \-L\/usr\/lib/ /" %{buildroot}%{_libdir}/pkgconfig/Coin.pc

# Fix the libdir
sed -i -e "s,\-L/usr/lib64 \-L/usr/lib,\-L%{_libdir}," %{buildroot}%{_datadir}/Coin%{soname}/conf/coin-default.cfg

# Remove unneeded files
rm -f %{buildroot}%{_libdir}/*.la

%fdupes %{buildroot}/%{_prefix}

%post -n libCoin%{soname} -p /sbin/ldconfig

%postun -n libCoin%{soname} -p /sbin/ldconfig

%files -n libCoin%{soname}
%defattr(-,root,root,-)
%doc LICENSE.GPL
%{_datadir}/Coin%{soname}/
%{_libdir}/libCoin.so.%{soname}*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog FAQ FAQ.legal LICENSE.GPL NEWS README RELNOTES THANKS
%{_bindir}/coin-config
%{_includedir}/Inventor/
%{_includedir}/SoDebug.h
%{_includedir}/SoWinEnterScope.h
%{_includedir}/SoWinLeaveScope.h
%{_libdir}/pkgconfig/Coin.pc
%{_libdir}/libCoin.so
%{_datadir}/aclocal/coin.m4
%doc %{_mandir}/man1/coin-config.1%{ext_man}
%doc %{_mandir}/man3/*.3%{ext_man}
%{_docdir}/%{name}-devel/html

%changelog
