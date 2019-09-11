#
# spec file for package libqt5-qtwayland
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define qt5_snapshot 0
%define libname libQt5WaylandCompositor5
%define base_name libqt5
%define real_version 5.13.0
%define so_version 5.13.0
%define tar_version qtwayland-everywhere-src-5.13.0
Name:           libqt5-qtwayland
Version:        5.13.0
Release:        0
Summary:        Qt 5 Wayland Addon
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM
Patch1:         0001-Don-t-crash-if-we-start-a-drag-without-dragFocus.patch
# In 5.12 branch only, not merged to 5.13 yet
Patch2:         0002-Client-Fix-stuttering-when-the-GUI-thread-is-busy.patch
# Those aren't merged upstream yet
# https://codereview.qt-project.org/c/qt/qtwayland/+/265999
Patch3:         0003-Client-Don-t-send-fake-SurfaceCreated-Destroyed-even.patch
# https://codereview.qt-project.org/c/qt/qtwayland/+/265998
Patch4:         0004-Client-Make-handleUpdate-aware-of-exposure-changes.patch
# https://codereview.qt-project.org/c/qt/qtwayland/+/265997
Patch5:         0005-Client-Reset-frame-callback-timer-when-hiding-a-wind.patch
# PATCH-FIX-UPSTREAM
Patch6:         0001-Fix-use-of-private-dependency.patch
# PATCH-FIX-OPENSUSE
Patch100:       workaround-null-object.patch
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  xz
%if 0%{?suse_version} < 1330
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.1.0
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server) >= 1.1.0
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon) >= 0.2.0
Conflicts:      qtwayland
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt is a set of libraries for developing applications.

%package devel
Summary:        Qt 5 Wayland Addon
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libQt5WaylandClient5 = %{version}
Requires:       libQt5WaylandCompositor5 = %{version}
Conflicts:      qtwayland-devel

%description devel
Development package to build Qt-based compositors.

%package private-headers-devel
Summary:        Qt 5 Wayland Addon Non-ABI stable experimental API files
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libqt5-qtbase-private-headers-devel

%description private-headers-devel
This package provides private headers of libqt5-qtwayland that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5WaylandCompositor5
Summary:        Qt 5 Wayland Addon
Group:          Development/Libraries/C and C++
Conflicts:      qtwayland

%description -n libQt5WaylandCompositor5
Qt is a set of libraries for developing applications.

%package -n libQt5WaylandClient5
Summary:        Qt 5 Wayland Addon
Group:          Development/Libraries/C and C++
Conflicts:      qtwayland

%description -n libQt5WaylandClient5
Qt is a set of libraries for developing applications.

%package examples
Summary:        Qt5 wayland examples
Group:          Development/Libraries/X11
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtwayland module.

%prep
%autosetup -p1 -n %{tar_version}

%post  -n libQt5WaylandCompositor5 -p /sbin/ldconfig

%postun -n libQt5WaylandCompositor5 -p /sbin/ldconfig

%post  -n libQt5WaylandClient5 -p /sbin/ldconfig

%postun -n libQt5WaylandClient5 -p /sbin/ldconfig

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%{_libqt5_qmake} \
%if 0%{?suse_version} < 1330
    QMAKE_CC=gcc-7 QMAKE_CXX=g++-7 CONFIG+=c++14 \
%endif
	CONFIG+=wayland-compositor

%if 0%{?suse_version} < 1330
    export CC=gcc-7
    export CXX=g++-7
%endif

%{make_jobs}

%install
%{qmake5_install}

find %{buildroot}%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.*
%{_libqt5_bindir}/qtwaylandscanner
%{_libqt5_plugindir}/
%{_libqt5_archdatadir}/qml/QtWayland/

%files -n libQt5WaylandCompositor5
%defattr(-,root,root,-)
%doc  LICENSE.*
%{_libqt5_libdir}/libQt5WaylandCompositor.so.*

%files -n libQt5WaylandClient5
%defattr(-,root,root,-)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5WaylandClient.so.*

%files devel
%defattr(-,root,root,-)
%doc LICENSE.*
%{_libqt5_libdir}/*.prl
%{_libqt5_libdir}/*.so
%{_libqt5_libdir}/pkgconfig/*
%{_libqt5_libdir}/cmake/Qt5*/
%{_libqt5_archdatadir}/mkspecs/modules/*.pr?
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*

%files private-headers-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
