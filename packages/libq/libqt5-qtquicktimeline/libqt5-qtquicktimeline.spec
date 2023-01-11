#
# spec file for package libqt5-qtquicktimeline
#
# Copyright (c) 2023 SUSE LLC
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


%define qt5_snapshot 1
Name:           libqt5-qtquicktimeline
Version:        5.15.8+kde0
Release:        0
Summary:        Qt 5 Quick Timeline Addon
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtquicktimeline-everywhere-src-%{version}
Source:         %{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{real_version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{real_version}

%description
The Qt Quick Timeline module provides QML types to use timelines and keyframes
to animate Qt Quick user interfaces.

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

%files
%license LICENSE.*
%dir %{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/QtQuick/Timeline

%changelog
