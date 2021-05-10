#
# spec file for package qt6-quicktimeline
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


%define real_version 6.1.0
%define short_version 6.1
%define tar_name qtquicktimeline-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quicktimeline%{?pkg_suffix}
Version:        6.1.0
Release:        0
Summary:        Qt 6 module for creating keyframe-based animations
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt Quick Timeline module enables keyframe-based animations and
parameterization. This module is directly supported by Qt Design Studio and
Qt Quick Designer, with a timeline editor to create keyframe-based animations.

%package imports
Summary:        Qt 6 QuickTimeline QML files and plugins

%description imports
QML files and plugins from the Qt 6 QuickTimeline module

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%files imports
%license LICENSE.*
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_qmldir}/QtQuick/Timeline/

%endif

%changelog
