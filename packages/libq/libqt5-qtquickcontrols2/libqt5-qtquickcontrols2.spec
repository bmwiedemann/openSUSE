#
# spec file for package libqt5-qtquickcontrols2
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
%global __requires_exclude qmlimport\\((Backend|Theme|.*example).*

%define qt5_snapshot 1
%define base_name libqt5
%define real_version 5.15.7
%define so_version 5.15.7
%define tar_version qtquickcontrols2-everywhere-src-%{version}
Name:           libqt5-qtquickcontrols2
Version:        5.15.7+kde7
Release:        0
Summary:        Qt 5 Quick Controls Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{real_version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{real_version}
BuildRequires:  libqt5-qtbase-devel >= %{real_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{real_version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{real_version}
%requires_ge    libQt5Widgets5
%requires_ge    libQtQuick5

%description
The Qt Quick Controls2 module provides a set of controls that
can be used to build complete interfaces in Qt Quick.

%package -n libQt5QuickControls2-5
Summary:        Qt 5 QuickControl2 Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          System/Libraries

%description -n libQt5QuickControls2-5
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package -n libQt5QuickTemplates2-5
Summary:        Qt5 QuickTemplates2 Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          System/Libraries

%description -n libQt5QuickTemplates2-5
You need this package if you want to compile programs with qtquickcontrols2.

%package -n libQt5QuickControls2-devel
Summary:        Qt Development Kit
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Requires:       libQt5QuickControls2-5 = %{version}

%description -n libQt5QuickControls2-devel
You need this package if you want to compile programs with qtquickcontrols2.

%package -n libQt5QuickTemplates2-devel
Summary:        Qt Development Kit
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Requires:       libQt5QuickTemplates2-5 = %{version}

%description -n libQt5QuickTemplates2-devel
You need this package if you want to compile programs with qtquickcontrols2.

%package private-headers-devel
Summary:        Headers for the unstable API of the Qt5 QuickControls2 module
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Requires:       libQt5QuickControls2-devel = %{version}
Requires:       libQt5QuickTemplates2-devel = %{version}

%description private-headers-devel
You need this package if you want to compile programs against the unstable API
of the Qt5 QuickControls 2 module.

%package examples
Summary:        Qt5 quickcontrols2 examples
License:        BSD-3-Clause
Group:          Development/Libraries/X11

%description examples
Examples for libqt5-qtquickcontrols2 module.

%prep
%autosetup -n %{tar_version}

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libqt5_libdir} -type f -name '*la' -print -exec perl -pi -e 's,-L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libqt5_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%{_lib}qt5_bindir/moc," -e "s,uic_location=.*,uic_location=%{_lib}qt5_bindir/uic," {} +
find %{buildroot}/%{_libqt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} +

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%post -n libQt5QuickControls2-5 -p /sbin/ldconfig
%postun -n libQt5QuickControls2-5 -p /sbin/ldconfig
%post -n libQt5QuickTemplates2-5 -p /sbin/ldconfig
%postun -n libQt5QuickTemplates2-5 -p /sbin/ldconfig

%files -n libQt5QuickControls2-5
%license LICENSE.*
%{_libqt5_libdir}/libQt5QuickControls2.so.*

%files -n libQt5QuickTemplates2-5
%license LICENSE.*
%{_libqt5_libdir}/libQt5QuickTemplates2.so.*

%files
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/Qt

%files -n libQt5QuickControls2-devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtQuickControls2/%{so_version}
%{_libqt5_includedir}/QtQuickControls2
%{_libqt5_libdir}/cmake/Qt5QuickControls2
%{_libqt5_libdir}/libQt5QuickControls2.prl
%{_libqt5_libdir}/libQt5QuickControls2.so
%{_libqt5_libdir}/pkgconfig/Qt5QuickControls2.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quickcontrols2.pri

%files -n libQt5QuickTemplates2-devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtQuickTemplates2/%{so_version}
%{_libqt5_includedir}/QtQuickTemplates2
%{_libqt5_libdir}/cmake/Qt5QuickTemplates2
%{_libqt5_libdir}/libQt5QuickTemplates2.prl
%{_libqt5_libdir}/libQt5QuickTemplates2.so
%{_libqt5_libdir}/pkgconfig/Qt5QuickTemplates2.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quicktemplates2.pri

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtQuickControls2/%{so_version}
%{_libqt5_includedir}/QtQuickTemplates2/%{so_version}
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quickcontrols2_private.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quicktemplates2_private.pri

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
