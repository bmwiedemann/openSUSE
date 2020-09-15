#
# spec file for package libqt5-qtquicktimeline
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


Name:           libqt5-qtquicktimeline
Version:        5.15.1
Release:        0
Summary:        Qt 5 Quick Timeline Addon
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtquicktimeline-everywhere-src-5.15.1
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}

%description
The Qt Quick Timeline module provides QML types to use timelines and keyframes
to animate Qt Quick user interfaces.

%prep
%autosetup -n %{tar_version}

%build
%qmake5
%make_jobs

%install
%qmake5_install

%files
%license LICENSE.*
%dir %{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/QtQuick/Timeline

%changelog
