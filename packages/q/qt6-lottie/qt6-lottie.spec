#
# spec file for package qt6-lottie
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


%define real_version 6.7.2
%define short_version 6.7
%define short_name qtlottie
%define tar_name qtlottie-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-lottie%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        QML API for rendering graphics and animation
# LICENSE.GPL3-EXCEPT only applies to the conan recipe which is not used
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-lottie-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Bodymovin plugin.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Lottie QML files and plugins

%description imports
QML files and plugins from the Qt 6 Lottie module.

### Private only library ###

%package -n libQt6Bodymovin6
Summary:        Qt 6 Bodymovin library

%description -n libQt6Bodymovin6
The Qt 6 Bodymovin library.
This library does not have any ABI or API guarantees.

%package -n qt6-bodymovin-private-devel
Summary:        Development files for the Qt 6 Bodymovin library
Requires:       cmake(Qt6Gui) = %{real_version}
%requires_eq    qt6-gui-private-devel
# Renamed in 6.2.0
Provides:       qt6-bodymovin-devel = 6.2.0
Obsoletes:      qt6-bodymovin-devel < 6.2.0

%description -n qt6-bodymovin-private-devel
This package provides private headers of libQt6Bodymovin that do not have any
ABI or API guarantees.

%endif

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

%ldconfig_scriptlets -n libQt6Bodymovin6

%files imports
%dir %{_qt6_qmldir}/Qt
%dir %{_qt6_qmldir}/Qt/labs
%{_qt6_qmldir}/Qt/labs/lottieqt/

%files -n libQt6Bodymovin6
%license LICENSES/*
%{_qt6_libdir}/libQt6Bodymovin.so.*

### Private only library ###

%files -n qt6-bodymovin-private-devel
%{_qt6_cmakedir}/Qt6BodymovinPrivate/
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_descriptionsdir}/BodymovinPrivate.json
%{_qt6_includedir}/QtBodymovin/
%{_qt6_libdir}/libQt6Bodymovin.prl
%{_qt6_libdir}/libQt6Bodymovin.so
%{_qt6_metatypesdir}/qt6bodymovinprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_bodymovin_private.pri

%endif

%changelog
