#
# spec file for package libqt5-qtquick3d
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with system_assimp

%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtquick3d-everywhere-src-5.15.1
Name:           libqt5-qtquick3d
Version:        5.15.1
Release:        0
Summary:        Qt 5 Quick 3D Module
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
%if %{with system_assimp}
BuildRequires:  pkgconfig(assimp) >= 5.0.0
%else
BuildRequires:  zlib-devel
%endif
BuildRequires:  libQt5Core-private-headers-devel >= 5.12
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5OpenGLExtensions-devel-static
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= 5.12
BuildRequires:  pkgconfig(Qt5Quick)
%requires_ge    libQt5Widgets5
%requires_ge    libQtQuick5

%description
Qt Quick 3D is a high level 3D API for Qt Quick.
Qt Quick 3D enables anyone to introduce 3D content into their Qt Quick
applications. Rather than requiring the end user to know advanced details of
the graphicsrendering pipeline (building framegraphs and materials),
it is now possible to simply build up a 3D scene using high level primitives.

%package -n libQt5Quick3D5
Summary:        Qt5 Quick3D Library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libQt5Quick3D5
Qt Quick 3D is a high level 3D API for Qt Quick.
Qt Quick 3D enables anyone to introduce 3D content into their Qt Quick
applications. Rather than requiring the end user to know advanced details of
the graphicsrendering pipeline (building framegraphs and materials),
it is now possible to simply build up a 3D scene using high level primitives.

%package -n libQt5Quick3DAssetImport5
Summary:        Qt5 Quick3D Asset Importing Library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libQt5Quick3DAssetImport5
Qt Quick 3D Library for importing of 3D assets.

%package tools
Summary:        Qt Development Kit
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11

%description tools
Tools for working with the Qt Quick 3D module.

%package imports
Summary:        Qt Development Kit
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
Requires:       %{name}-tools
Requires:       libQt5Quick3D5 = %{version}
Requires:       libQt5Quick3DAssetImport5 = %{version}

%description imports
QML API for Qt Quick 3D.

%package devel
Summary:        Qt Development Kit
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
Requires:       %{name}-tools
Requires:       libQt5Quick3D5 = %{version}
Requires:       libQt5Quick3DAssetImport5 = %{version}

%description devel
You need this package if you want to compile programs with Qt Quick 3D.

%package private-headers-devel
Summary:        Headers for the unstable API of the Qt5 Quick 3D module
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
Requires:       %{name}-devel = %{version}

%description private-headers-devel
You need this package if you want to compile programs against the unstable API
of the Qt5 Quick 3D module.

%package examples
Summary:        Qt5 Quick 3D examples
License:        BSD-3-Clause
Group:          Development/Libraries/X11

%description examples
Examples for the Qt Quick 3D module.

%prep
%autosetup -n %{tar_version}

%build
%qmake5 -- \
	%if %{with system_assimp}
	-system-assimp \
	%endif

%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%fdupes %{buildroot}

%post -n libQt5Quick3D5 -p /sbin/ldconfig
%postun -n libQt5Quick3D5 -p /sbin/ldconfig
%post -n libQt5Quick3DAssetImport5 -p /sbin/ldconfig
%postun -n libQt5Quick3DAssetImport5 -p /sbin/ldconfig

%files -n libQt5Quick3D5
%license LICENSE.*
# Those go mostly together
%{_libqt5_libdir}/libQt5Quick3D.so.*
%{_libqt5_libdir}/libQt5Quick3DUtils.so.*
%{_libqt5_libdir}/libQt5Quick3DRender.so.*
%{_libqt5_libdir}/libQt5Quick3DRuntimeRender.so.*

%files -n libQt5Quick3DAssetImport5
%license LICENSE.*
# This needs plugins to be useful
%{_libqt5_libdir}/libQt5Quick3DAssetImport.so.*
%dir %{_libqt5_plugindir}/assetimporters/
%{_libqt5_plugindir}/assetimporters/libassimp.so
%{_libqt5_plugindir}/assetimporters/libuip.so

%files imports
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick3D/

%files tools
%license LICENSE.*
%{_libqt5_bindir}/balsam
%{_libqt5_bindir}/meshdebug

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtQuick3D*/%{so_version}
%{_libqt5_includedir}/QtQuick3D*/
%{_libqt5_libdir}/cmake/Qt5Quick3D*/
%{_libqt5_libdir}/libQt5Quick3D*.prl
%{_libqt5_libdir}/libQt5Quick3D*.so
%{_libqt5_libdir}/pkgconfig/Qt5Quick3D*.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quick3d*.pri

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtQuick3D*/%{so_version}

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
