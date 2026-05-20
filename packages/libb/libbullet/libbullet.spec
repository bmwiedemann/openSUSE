#
# spec file for package libbullet
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover   3_25
%define lname   libbullet%{sover}
%define pdesc   Bullet is a Collision Detection and Rigid Body Dynamics Library.
%global python3_inc %(python3 -c "import sysconfig; print(sysconfig.get_path('include'))")
%global python3_lib %(python3 -c "import sysconfig, os; d=sysconfig.get_config_vars(); print(os.path.join(d['LIBDIR'], d['LDLIBRARY']))")
Name:           libbullet
Version:        3.25
Release:        0
Summary:        Bullet Continuous Collision Detection and Physics Library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://pybullet.org/wordpress/
Source:         https://github.com/bulletphysics/bullet3/archive/%{version}/bullet3-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-pkgconfig-includedir.patch
Patch1:         fix-pkgconfig-includedir.patch
Patch2:         use-system-libs.patch
# PATCH-FIX-OPENSUSE fix-gwen-linux-link.patch - link gwen against OpenGLWindow on Linux to resolve glad symbols
Patch3:         fix-gwen-linux-link.patch
# PATCH-FIX-OPENSUSE fix-pybullet-numpy2-compat.patch - cast PyObject* to PyArrayObject* for PyArray_DATA() (GCC14/NumPy2 compat)
Patch4:         fix-pybullet-numpy2-compat.patch
# PATCH-FIX-OPENSUSE fix-pybullet-link-python-linux.patch - link pybullet.so against libpython on Linux for -Wl,--no-undefined
Patch5:         fix-pybullet-link-python-linux.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-numpy-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
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

%package -n python3-pybullet
Summary:        Python bindings for the Bullet Physics library
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
Requires:       libBulletFileLoader%{sover} = %{version}
Requires:       libBulletWorldImporter%{sover} = %{version}

%description -n python3-pybullet
%{pdesc}

This package provides Python 3 bindings (pybullet) for the Bullet
physics simulation library, including support for robotics simulation,
rigid body dynamics, and soft body simulation.

%prep
%autosetup -p1 -n bullet3-%{version}

# Take from Fedora specfile
rm -rf build3/*.{bat,exe}
rm -rf build3/xcode*
rm -rf build3/*osx*
rm -rf build3/premake*

# Fix any file permissions and formats
dos2unix -c ascii README.md

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
       -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
       -DINCLUDE_INSTALL_DIR="%{_includedir}/bullet" \
       -DBUILD_BULLET2_DEMOS=ON \
       -DBUILD_CPU_DEMOS=OFF \
       -DBUILD_EXTRAS=ON \
       -DBUILD_OPENGL3_DEMOS=ON \
       -DBUILD_PYBULLET=ON \
       -DBUILD_PYBULLET_NUMPY=ON \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_UNIT_TESTS=ON \
       -DINSTALL_EXTRA_LIBS=ON \
       -DINSTALL_LIBS=ON \
       -DUSE_DOUBLE_PRECISION=ON \
       -DBUILD_OBJ2SDF_EXTRA=OFF \
       -DPYTHON_INCLUDE_DIR=%{python3_inc} \
       -DPYTHON_LIBRARY=%{python3_lib} \
       -DPYTHON_SITE_PACKAGES=%{python3_sitearch}

make VERBOSE=1 %{?_smp_mflags}

%check
%ctest

%install
%cmake_install
# Fix double-slash in pkgconfig Cflags generated when INCLUDE_INSTALL_DIR is absolute
sed -i 's|/usr//usr|/usr|g' %{buildroot}%{_libdir}/pkgconfig/bullet_robotics*.pc
%fdupes -s %{buildroot}/%{_includedir}

%post -n %{lname} -p /sbin/ldconfig
%post -n libBulletFileLoader%{sover} -p /sbin/ldconfig
%post -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig
%post -n libBulletWorldImporter%{sover} -p /sbin/ldconfig
%post -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig
%post -n libConvexDecomposition%{sover} -p /sbin/ldconfig
%post -n libGIMPACTUtils%{sover} -p /sbin/ldconfig
%post -n libHACD%{sover} -p /sbin/ldconfig
%post -n python3-pybullet -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%postun -n libBulletFileLoader%{sover} -p /sbin/ldconfig
%postun -n libBulletInverseDynamicsUtils%{sover} -p /sbin/ldconfig
%postun -n libBulletWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libBulletXmlWorldImporter%{sover} -p /sbin/ldconfig
%postun -n libConvexDecomposition%{sover} -p /sbin/ldconfig
%postun -n libGIMPACTUtils%{sover} -p /sbin/ldconfig
%postun -n libHACD%{sover} -p /sbin/ldconfig
%postun -n python3-pybullet -p /sbin/ldconfig

%files -n %{lname}
%doc README.md AUTHORS.txt
%license LICENSE.txt
%{_libdir}/libB*.so.*
%{_libdir}/libLinearMath*.so.*
%exclude %{_libdir}/libBulletExampleBrowserLib.so*
%exclude %{_libdir}/libBulletFileLoader.so.*
%exclude %{_libdir}/libBulletInverseDynamicsUtils.so.*
%exclude %{_libdir}/libBulletWorldImporter.so.*
%exclude %{_libdir}/libBulletXmlWorldImporter.so.*
%exclude %{_libdir}/libBussIK.so*

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
%{_libdir}/libBulletExampleBrowserLib.so
%exclude %{_libdir}/libBulletExampleBrowserLib.so.*
%exclude %{_libdir}/libBussIK.so*
%exclude %{_libdir}/libgwen.so*
%exclude %{_libdir}/libOpenGLWindow.so*
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/pkgconfig/bullet_robotics.pc
%{_libdir}/pkgconfig/bullet_robotics_gui.pc
# clsocket headers and static lib installed by bullet3 into global include/lib
%exclude %{_includedir}/ActiveSocket.h
%exclude %{_includedir}/Host.h
%exclude %{_includedir}/PassiveSocket.h
%exclude %{_includedir}/SimpleSocket.h
%exclude %{_includedir}/StatTimer.h
%exclude /usr/lib/libclsocket.a

%files -n python3-pybullet
%doc README.md
%license LICENSE.txt
%{python3_sitearch}/pybullet.so*
%{_libdir}/libBulletExampleBrowserLib.so.*
%{_libdir}/libOpenGLWindow.so*
%{_libdir}/libBussIK.so*
%{_libdir}/libgwen.so*

%changelog
