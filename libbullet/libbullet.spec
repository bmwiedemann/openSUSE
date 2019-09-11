#
# spec file for package libbullet
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


%define sover   2_88
%define lname   libbullet%{sover}
%define pdesc   Bullet is a Collision Detection and Rigid Body Dynamics Library.
Name:           libbullet
Version:        2.88
Release:        0
Summary:        Bullet Continuous Collision Detection and Physics Library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://pybullet.org/wordpress/
Source:         https://github.com/bulletphysics/bullet3/archive/%{version}/bullet3-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-pkgconfig-cflags.patch gh#bulletphysics/bullet3#626
Patch1:         fix-pkgconfig-cflags.patch
Patch2:         use-system-libs.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tinyxml2)

%description
%{pdesc}

%package -n %{lname}
Summary:        Bullet Continuous Collision Detection and Physics Library
Group:          System/Libraries
Obsoletes:      libbullet < %{version}-%{release}
Provides:       libbullet = %{version}-%{release}

%description -n %{lname}
%{pdesc}

%package -n libBulletFileLoader%{sover}
Summary:        Bullet File Loader Library
Group:          System/Libraries

%description -n libBulletFileLoader%{sover}
%{pdesc}

%package -n libBulletInverseDynamicsUtils%{sover}
Summary:        Bullet Inverse Dynamics Utils Library
Group:          System/Libraries

%description -n libBulletInverseDynamicsUtils%{sover}
%{pdesc}

%package -n libBulletWorldImporter%{sover}
Summary:        Bullet World Importer Library
Group:          System/Libraries

%description -n libBulletWorldImporter%{sover}
%{pdesc}

%package -n libBulletXmlWorldImporter%{sover}
Summary:        Bullet Xml World Importer Library
Group:          System/Libraries

%description -n libBulletXmlWorldImporter%{sover}
%{pdesc}

%package -n libConvexDecomposition%{sover}
Summary:        Bullet Convex Decomposition Library
Group:          System/Libraries

%description -n libConvexDecomposition%{sover}
%{pdesc}

%package -n libGIMPACTUtils%{sover}
Summary:        Bullet GIMPACT Utils Library
Group:          System/Libraries

%description -n libGIMPACTUtils%{sover}
%{pdesc}

%package -n libHACD%{sover}
Summary:        Bullet HACD Library
Group:          System/Libraries

%description -n libHACD%{sover}
%{pdesc}

%package devel
Summary:        Development package for bullet library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libBulletFileLoader%{sover} = %{version}
Requires:       libBulletInverseDynamicsUtils%{sover} = %{version}
Requires:       libBulletWorldImporter%{sover} = %{version}
Requires:       libBulletXmlWorldImporter%{sover} = %{version}
Requires:       libConvexDecomposition%{sover} = %{version}
Requires:       libGIMPACTUtils%{sover} = %{version}
Requires:       libHACD%{sover} = %{version}

%description devel
This package contain all that is needed to developer or compile
appliancation with the Bullet library.

%prep
%setup -q -n bullet3-%{version}
%patch1 -p1
%patch2 -p1

# Take from Fedora specfile
rm -rf build3/*.{bat,exe}
rm -rf build3/xcode*
rm -rf build3/*osx*
rm -rf build3/premake*
rm -rf data
rm -rf examples

# Taken from Fedora specfile
# BulletRobotics and obj2sdf require several bundled libs not yet packaged in 
# the distribution
sed -i 's|BulletRobotics||' Extras/CMakeLists.txt
sed -i 's|obj2sdf||' Extras/CMakeLists.txt

# Fix any file permissions and formats
dos2unix -c ascii README.md

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
       -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
       -DINCLUDE_INSTALL_DIR="%{_includedir}/bullet" \
       -DBUILD_BULLET2_DEMOS=OFF \
       -DBUILD_CPU_DEMOS=OFF \
       -DBUILD_EXTRAS=ON \
       -DBUILD_OPENGL3_DEMOS=OFF \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_UNIT_TESTS=off \
       -DINSTALL_EXTRA_LIBS=ON \
       -DINSTALL_LIBS=ON

make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}/%{_includedir}

%post -n %{lname} -p /sbin/ldconfig
%post -n libBulletFileLoader%{sover} -p /sbin/ldconfig
%post -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig
%post -n libBulletWorldImporter%{sover} -p /sbin/ldconfig
%post -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig
%post -n libConvexDecomposition%{sover} -p /sbin/ldconfig
%post -n libGIMPACTUtils%{sover} -p /sbin/ldconfig
%post -n libHACD%{sover} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%postun -n libBulletFileLoader%{sover} -p /sbin/ldconfig
%postun -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig
%postun -n libBulletWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libConvexDecomposition%{sover} -p /sbin/ldconfig
%postun -n libGIMPACTUtils%{sover} -p /sbin/ldconfig
%postun -n libHACD%{sover} -p /sbin/ldconfig

%files -n %{lname}
%doc README.md AUTHORS.txt
%license LICENSE.txt
%{_libdir}/libB*.so.*
%{_libdir}/libLinearMath*.so.*
%exclude %{_libdir}/libBulletFileLoader.so.*
%exclude %{_libdir}/libBulletInverseDynamicsUtils.so.*
%exclude %{_libdir}/libBulletWorldImporter.so.*
%exclude %{_libdir}/libBulletXmlWorldImporter.so.*

%files -n libBulletFileLoader%{sover}
%{_libdir}/libBulletFileLoader.so.*

%files -n libBulletInverseDynamicsUtils%{sover}
%{_libdir}/libBulletInverseDynamicsUtils.so.*

%files -n libBulletWorldImporter%{sover}
%{_libdir}/libBulletWorldImporter.so.*

%files -n libBulletXmlWorldImporter%{sover}
%{_libdir}/libBulletXmlWorldImporter.so.*

%files -n libConvexDecomposition%{sover}
%{_libdir}/libConvexDecomposition.so.*

%files -n libGIMPACTUtils%{sover}
%{_libdir}/libGIMPACTUtils.so.*

%files -n libHACD%{sover}
%{_libdir}/libHACD.so.*

%files devel
%{_includedir}/bullet/
%{_libdir}/cmake/bullet
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/bullet.pc

%changelog
