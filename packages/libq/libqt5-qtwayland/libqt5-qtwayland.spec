#
# spec file for package libqt5-qtwayland
#
# Copyright (c) 2021 SUSE LLC
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


# Internal QML imports of examples
%global __requires_exclude qmlimport\\(com.theqtcompany.*

%define qt5_snapshot 0
%define libname libQt5WaylandCompositor5
%define base_name libqt5
%define real_version 5.15.2
%define so_version 5.15.2
%define tar_version qtwayland-everywhere-src-5.15.2
Name:           libqt5-qtwayland
Version:        5.15.2
Release:        0
Summary:        Qt 5 Wayland Addon
# The wayland compositor files are GPL-3.0-or-later
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM
Patch1:         0001-Scanner-Avoid-accessing-dangling-pointers-in-destroy.patch
Patch2:         0002-Make-setting-QT_SCALE_FACTOR-work-on-Wayland.patch
Patch3:         0003-Do-not-try-to-eglMakeCurrent-for-unintended-case.patch
Patch4:         0004-Make-setting-QT_SCALE_FACTOR-work-on-Wayland.patch
Patch5:         0005-Ensure-that-grabbing-is-performed-in-correct-context.patch
Patch6:         0006-Fix-leaked-subsurface-wayland-items.patch
Patch7:         0007-Use-qWarning-and-_exit-instead-of-qFatal-for-wayland.patch
Patch8:         0008-Fix-memory-leak-in-QWaylandGLContext.patch
Patch9:         0009-Client-Send-set_window_geometry-only-once-configured.patch
Patch10:        0010-Translate-opaque-area-with-frame-margins.patch
Patch11:        0011-Client-Send-exposeEvent-to-parent-on-subsurface-posi.patch
Patch12:        0012-Get-correct-decoration-margins-region.patch
Patch13:        0013-xdgshell-Tell-the-compositor-the-screen-we-re-expect.patch
Patch14:        0014-Fix-compilation.patch
Patch15:        0015-client-Allow-QWaylandInputContext-to-accept-composed.patch
Patch16:        0016-Client-Announce-an-output-after-receiving-more-compl.patch
Patch17:        0017-Fix-issue-with-repeated-window-size-changes.patch
Patch18:        0018-Include-locale.h-for-setlocale-LC_CTYPE.patch
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  xz
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
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libQt5WaylandClient5 = %{version}
Requires:       libQt5WaylandCompositor5 = %{version}
Conflicts:      qtwayland-devel

%description devel
Development package to build Qt-based compositors.

%package private-headers-devel
Summary:        Qt 5 Wayland Addon Non-ABI stable experimental API files
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libqt5-qtbase-private-headers-devel
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtwayland that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5WaylandCompositor5
Summary:        Qt 5 Wayland Addon
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Conflicts:      qtwayland

%description -n libQt5WaylandCompositor5
Qt is a set of libraries for developing applications.

%package -n libQt5WaylandClient5
Summary:        Qt 5 Wayland Addon
License:        GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Conflicts:      qtwayland

%description -n libQt5WaylandClient5
Qt is a set of libraries for developing applications.

%package examples
Summary:        Qt5 wayland examples
License:        BSD-3-Clause
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
	CONFIG+=wayland-compositor

%make_jobs

%install
%qmake5_install

find %{buildroot}%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*pc' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} \;
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

fdupes -s %{buildroot}

%files
%license LICENSE.*
%{_libqt5_bindir}/qtwaylandscanner
%{_libqt5_plugindir}/
%{_libqt5_archdatadir}/qml/QtWayland/

%files -n libQt5WaylandCompositor5
%license LICENSE.*
%{_libqt5_libdir}/libQt5WaylandCompositor.so.*

%files -n libQt5WaylandClient5
%license LICENSE.*
%{_libqt5_libdir}/libQt5WaylandClient.so.*

%files devel
%license LICENSE.*
%{_libqt5_libdir}/*.prl
%{_libqt5_libdir}/*.so
%{_libqt5_libdir}/pkgconfig/*
%{_libqt5_libdir}/cmake/Qt5*/
%{_libqt5_archdatadir}/mkspecs/modules/*.pr?
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
