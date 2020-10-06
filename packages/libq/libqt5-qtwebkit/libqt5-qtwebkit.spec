#
# spec file for package libqt5-qtwebkit
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

%bcond_without avsupport
%define __builder ninja
%define _cxx g++
%define _cc gcc

%define qt5_snapshot 0

%define libname libQt5WebKitWidgets5

%define base_name qtwebkit
%define real_version 5.212
%define so_version 5.212
%define full_version 5.212.0
%define required_qt5 5.2
%define prerel_version alpha4
%define tar_version %{base_name}-%{full_version}-%{prerel_version}
Name:           libqt5-qtwebkit
Version:        5.212~%{prerel_version}
Release:        0
Summary:        Qt 5 WebKit Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
Url:            https://qtwebkit.github.io/
Source:         https://github.com/qtwebkit/qtwebkit/releases/download/%{tar_version}/%{tar_version}.tar.xz
Source1:        baselibs.conf
Source99:       libqt5-qtwebkit-rpmlintrc
# openSUSE-specific patches
# PATCH-FIX-OPENSUSE Enable X11 target build always as we didn't ship Xcb Plugin cmake file - mlin@suse.com
Patch0:         enable_x11_target_always.patch
# PATCH-FIX-OPENSUSE
Patch1:         tell-the-truth-about-private-api.patch
# PATCH-FIX-UPSTREAM https://bugs.webkit.org/show_bug.cgi?id=141288
Patch2:         webkit-bwo141288.patch
Patch3:         qtwebkit-5.212.0_pre20200309-bison-3.7.patch
%if %{with avsupport}
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
%define _avSupport ON
%else
%define _avSupport OFF
%endif
BuildRequires:  libQt5Core-private-headers-devel >= %{required_qt5}
BuildRequires:  libQt5Gui-private-headers-devel >= %{required_qt5}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{required_qt5}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{required_qt5}
BuildRequires:  libqt5-qtlocation-private-headers-devel >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Core) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Location) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Network) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5OpenGL) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5PrintSupport) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Quick) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Sensors) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Test) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5WebChannel) >= %{required_qt5}
BuildRequires:  pkgconfig(Qt5Widgets) >= %{required_qt5}
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libxslt-devel
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  python-xml
BuildRequires:  ruby
BuildRequires:  hyphen-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
%if %qt5_snapshot
# to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  procps
BuildRequires:  xz
BuildRequires:  pkgconfig(libwebp)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The QtWebKit module provides the WebView API which allows QML
applications to render regions of dynamic web content. A WebView
component may share the screen with other QML components or encompass
the full screen as specified within the QML application.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %libname
Summary:        Qt 5 WebKit Widget library
Group:          Development/Libraries/X11
Requires:       libQt5WebKit5 = %version

%description -n %libname
The QtWebKit module provides the WebView API which allows QML
applications to render regions of dynamic web content. A WebView
component may share the screen with other QML components or encompass
the full screen as specified within the QML application.

%package -n libQt5WebKit5
Summary:        Qt5 WebKit Library
Group:          Development/Libraries/X11

%description -n libQt5WebKit5
You need this package if you want to compile programs with QtWebKit.

%package -n libQt5WebKit5-imports
Summary:        QML imports for the Qt5 WebKit library
Group:          Development/Libraries/X11
Supplements:    packageand(libQt5WebKit5:libQtQuick5)
# imports split with 5.4.1
Conflicts:      libQt5WebKit5 < 5.4.1
Requires:       libQt5WebKit5 = %version

%description -n libQt5WebKit5-imports
You need this package if you want to compile programs with QtWebKit.

%package -n libQt5WebKitWidgets-devel
Summary:        Development files for the Qt5 WebKit Widgets library
Group:          Development/Libraries/X11
Requires:       %libname = %{version}
Requires:       libQt5WebKit5-devel = %{version}
Requires:       libqt5-qtdeclarative-devel
Requires:       libqt5-qtsensors-devel

%description -n libQt5WebKitWidgets-devel
You need this package if you want to compile programs with QtWebKit.

%package -n libQt5WebKit5-devel
Summary:        Development files for the Qt5 WebKit library
Group:          Development/Libraries/X11
Requires:       libQt5WebKit5 = %version
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Gui)
Requires:       pkgconfig(Qt5Network)
Requires:       pkgconfig(Qt5Qml)
Requires:       pkgconfig(Qt5Quick)
Requires:       pkgconfig(Qt5Sensors)

%description -n libQt5WebKit5-devel
You need this package if you want to compile programs with QtWebKit.

%package -n libQt5WebKitWidgets-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebKit Widgets library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       libQt5WebKit-private-headers-devel = %{version}
Requires:       libQt5WebKitWidgets-devel = %{version}

%description -n libQt5WebKitWidgets-private-headers-devel
This package provides private headers of libqt5-qtwebkit that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5WebKit-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebKit library
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       libQt5WebKit5-devel = %{version}

%description -n libQt5WebKit-private-headers-devel
This package provides private headers of libqt5-qtwebkit that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package devel
Summary:        Development files for the Qt5 WebKit library
Group:          Development/Libraries/X11
Requires:       libQt5WebKit5-devel = %{version}
Requires:       libQt5WebKitWidgets-devel = %{version}

%description devel
You need this package if you want to compile programs with qtwebkit.
This package pulls in development files for both libQt5WebKit and
libQt5WebKitWidgets libraries.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebKit library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5WebKit-private-headers-devel = %{version}
Requires:       libQt5WebKitWidgets-private-headers-devel = %{version}

%description private-headers-devel
You need this package if you want to compile programs with QtWebKit.
This package pulls in private headers for both libQt5WebKit and
libQt5WebKitWidgets libraries.


%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%post -n libQt5WebKit5 -p /sbin/ldconfig

%postun -n libQt5WebKit5 -p /sbin/ldconfig

%build
%define _lto_cflags %{nil}

# Limit to 2GB mem per thread to avoid failure
%limit_build -m 2000

%if %qt5_snapshot
# force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%global optflags %(echo %{optflags} -fpermissive -Wl,--no-keep-memory -Wl,--reduce-memory-overheads | sed 's/-g /-g1 /')

%cmake -DPORT=Qt \
       -DCMAKE_C_COMPILER=%{_cc} \
       -DCMAKE_CXX_COMPILER=%{_cxx} \
       -DCMAKE_BUILD_TYPE=Release \
       -DENABLE_VIDEO=%{_avSupport} \
       -DENABLE_WEB_AUDIO=%{_avSupport} \
%ifarch ppc ppc64 ppc64le s390 s390x
       -DENABLE_JIT=OFF \
       -DUSE_SYSTEM_MALLOC=ON \
%endif
       -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
       -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread"

%cmake_build

%install
%cmake_install

find %{buildroot}/%{_libqt5_libdir} -type f -name '*la' -print -exec perl -pi -e 's,-L%{_builddir}/\S+,,g' {} +

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %libname
%defattr(-,root,root,755)
%doc LICENSE.*
%dir %{_libqt5_libexecdir}
%{_libqt5_libexecdir}/QtWebProcess
%{_libqt5_libdir}/libQt5WebKitWidgets.so.*

%files -n libQt5WebKit5
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5WebKit.so.*
%{_libqt5_libexecdir}/QtWebNetworkProcess
%{_libqt5_libexecdir}/QtWebPluginProcess
%{_libqt5_libexecdir}/QtWebStorageProcess

%files -n libQt5WebKit5-imports
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtWebKit

%files -n libQt5WebKitWidgets-private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/QtWebKitWidgets/%{full_version}

%files -n libQt5WebKit-private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/QtWebKit/%{full_version}

%files -n libQt5WebKit5-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtWebKit/%{full_version}
%{_libqt5_includedir}/QtWebKit
%{_libqt5_libdir}/cmake/Qt5WebKit
%{_libqt5_libdir}/libQt5WebKit.so
%{_libqt5_libdir}/pkgconfig/Qt5WebKit.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_webkit.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_webkit_private.pri

%files -n libQt5WebKitWidgets-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtWebKitWidgets/%{full_version}
%{_libqt5_includedir}/QtWebKitWidgets
%{_libqt5_libdir}/cmake/Qt5WebKitWidgets
%{_libqt5_libdir}/libQt5WebKitWidgets.so
%{_libqt5_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_webkitwidgets.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_webkitwidgets_private.pri

%changelog
