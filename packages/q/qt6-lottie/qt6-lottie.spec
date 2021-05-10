#
# spec file for package qt6-lottie
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
Version:        6.1.0
Release:        0
Summary:        QML API for rendering graphics and animation
# LICENSE.GPL3-EXCEPT only applies to the conan recipe which is not used
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-lottie-rpmlintrc
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  qt6-gui-private-devel
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

%package -n libQt6Bodymovin6
Summary:        Qt 6 Bodymovin library

%description -n libQt6Bodymovin6
The Qt 6 Bodymovin library.

%package -n qt6-bodymovin-devel
Summary:        Qt 6 Bodymovin library - Development files
Requires:       libQt6Bodymovin6 = %{version}
%requires_eq  qt6-gui-private-devel

%description -n qt6-bodymovin-devel
Development files for the Qt 6 Bodymovin library.

%package -n qt6-bodymovin-private-devel
Summary:        Non-ABI stable API for the Qt 6 Bodymovin Library
Requires:       cmake(Qt6Bodymovin) = %{real_version}

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

%post -n libQt6Bodymovin6 -p /sbin/ldconfig
%postun -n libQt6Bodymovin6 -p /sbin/ldconfig

%files imports
%dir %{_qt6_qmldir}/Qt
%dir %{_qt6_qmldir}/Qt/labs
%{_qt6_qmldir}/Qt/labs/lottieqt/

%files -n libQt6Bodymovin6
%license LICENSE.GPL3
%{_qt6_libdir}/libQt6Bodymovin.so.*

%files -n qt6-bodymovin-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Bodymovin/
%{_qt6_descriptionsdir}/Bodymovin.json
%{_qt6_includedir}/QtBodymovin/
%{_qt6_libdir}/libQt6Bodymovin.prl
%{_qt6_libdir}/libQt6Bodymovin.so
%exclude %{_qt6_includedir}/QtBodymovin/%{real_version}

%files -n qt6-bodymovin-private-devel
%{_qt6_includedir}/QtBodymovin/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_bodymovin_private.pri

%endif

%changelog
