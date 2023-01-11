#
# spec file for package libqt5-qtquickcontrols
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
%global __requires_exclude qmlimport\\(.*example.*

%define qt5_snapshot 1
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtquickcontrols-everywhere-src-%{version}
Name:           libqt5-qtquickcontrols
Version:        5.15.8+kde0
Release:        0
Summary:        Qt 5 Quick Controls Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch1:         fix-handle-deps.patch
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
The Qt Quick Controls module provides a set of controls that
can be used to build complete interfaces in Qt Quick.

%package examples
Summary:        Qt5 quickcontrols examples
License:        BSD-3-Clause
Group:          Development/Libraries/X11

%description examples
Examples for libqt5-qtquickcontrols module.

%prep
%autosetup -p1 -n %{tar_version}

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

%files
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
