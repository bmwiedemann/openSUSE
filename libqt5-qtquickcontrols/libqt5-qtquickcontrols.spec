#
# spec file for package libqt5-qtquickcontrols
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

Name:           libqt5-qtquickcontrols
Version:        5.13.1
Release:        0
Summary:        Qt 5 Quick Controls Addon
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.1
%define so_version 5.13.1
%define tar_version qtquickcontrols-everywhere-src-5.13.1
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
%requires_ge libQt5Widgets5
%requires_ge libQtQuick5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Qt Quick Controls module provides a set of controls that
can be used to build complete interfaces in Qt Quick.

%package examples
Summary:        Qt5 quickcontrols examples
Group:          Development/Libraries/X11

%description examples
Examples for libqt5-qtquickcontrols module.

%prep
%setup -q -n %{tar_version}
%autopatch -p1

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

%files
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
