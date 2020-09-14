#
# spec file for package libqt5-qtscript
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
%define libname libQt5Script5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtscript-everywhere-src-5.15.1
Name:           libqt5-qtscript
Version:        5.15.1
Release:        0
Summary:        Qt 5 Script library
# Legal:
# Most files in src/script are LGPL-2.1-only
# src/3rdparty is LGPL-2.0-or-later + BSD == LGPL-2.0-or-later
License:        (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later) AND LGPL-2.0-or-later AND LGPL-2.1-only
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM libqt5-qtscript-s390-support.patch -- adds s390, taken from webkit upstream
Patch1:         libqt5-qtscript-s390-support.patch
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus) >= %{version}
BuildRequires:  pkgconfig(Qt5Gui) >= %{version}
BuildRequires:  pkgconfig(Qt5Widgets) >= %{version}

%description
Qt Script is a module for adding scripting to applications. It allows
evaluating and debugging of scripts, and advanced use of objects and
functions. It also gives access to a low-level ECMAScript engine API.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Script library
Group:          System/Libraries
%requires_ge    libQt5Widgets5

%description -n %{libname}
Qt Script is a module for adding scripting to applications. It allows
evaluating and debugging of scripts, and advanced use of objects and
functions. It also gives access to a low-level ECMAScript engine API.

%package devel
Summary:        Development files for the Qt 5 Script library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
Provides:       libQt5Script-devel = %{version}
Obsoletes:      libQt5Script-devel < %{version}

%description devel
Qt Script is a module for adding scripting to applications.

This subpackage contains the header files for developing
applications that want to make use of libQt5Script5.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 Script library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
Requires:       libQt5Widgets-private-headers-devel >= %{version}
Provides:       libQt5Script-private-headers-devel = %{version}
Obsoletes:      libQt5Script-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtscript that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 Script examples
Group:          Documentation/Other
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtscript module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%define _lto_cflags %{nil}
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%{_libqt5_bindir}/moc," -e "s,uic_location=.*,uic_location=%{_libqt5_bindir}/uic," {} +
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%license LICENSE.*
%{_libqt5_libdir}/libQt5*.so.*

%files private-headers-devel
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5*.prl
%{_libqt5_libdir}/libQt5*.so
%{_libqt5_libdir}/pkgconfig/Qt5*.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_*.pri

%files examples
%{_libqt5_examplesdir}/

%changelog
