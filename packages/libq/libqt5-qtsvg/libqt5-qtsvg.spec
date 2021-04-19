#
# spec file for package libqt5-qtsvg
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


%define qt5_snapshot 0
%define libname libQt5Svg5
%define base_name libqt5
%define real_version 5.15.2
%define so_version 5.15.2
%define tar_version qtsvg-everywhere-src-5.15.2
Name:           libqt5-qtsvg
Version:        5.15.2
Release:        0
Summary:        Qt 5 SVG Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM
Patch1:         0001-Improve-handling-of-malformed-numeric-values-in-svg-.patch
Patch2:         0002-Clamp-parsed-doubles-to-float-representable-values.patch
Patch3:         0003-Avoid-buffer-overflow-in-isSupportedSvgFeature.patch
Patch4:         0004-Make-image-handler-accept-UTF-16-UTF-32-encoded-SVGs.patch
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)
# Use git to apply the patches, Patch4 contains binary diffs
BuildRequires:  git-core

%description
The Qt SVG module provides functionality for displaying SVG images
as a widget, and to create SVG files using drawing commands.

%prep
%autosetup -p1 -S git -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 SVG Library
Group:          Development/Libraries/X11
%requires_ge    libQt5Widgets5

%description -n %{libname}
The Qt SVG module provides functionality for displaying SVG images
as a widget, and to create SVG files using drawing commands.

%package devel
Summary:        Development files for the Qt5 SVG library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Provides:       libQt5Svg-devel = %{version}
Obsoletes:      libQt5Svg-devel < %{version}

%description devel
You need this package if you want to compile programs with QtSvg.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 SVG library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Provides:       libQt5Svg-private-headers-devel = %{version}
Obsoletes:      libQt5Svg-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtsvg that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 SVG examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtsvg modules.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libqt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} +
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Svg.so.*
%dir %{_libqt5_plugindir}
%{_libqt5_plugindir}/imageformats/libqsvg.so
%{_libqt5_plugindir}/iconengines

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtSvg
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/QtSvg
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5Svg.prl
%{_libqt5_libdir}/libQt5Svg.so
%{_libqt5_libdir}/pkgconfig/Qt5Svg.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
