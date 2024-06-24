#
# spec file for package qt6-virtualkeyboard
#
# Copyright (c) 2024 SUSE LLC
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
%define tar_name qtvirtualkeyboard-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-virtualkeyboard%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Framework for writing or integrating input methods and engines for Qt 6
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-virtualkeyboard-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6QmlTools) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickControls2) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(xcb)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt VirtualKeyboard provides an input framework and reference keyboard frontend
for Qt 6.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 VirtualKeyboard QML files and plugins

%description imports
QML files and plugins from the Qt 6 VirtualKeyboard module.

%package -n libQt6VirtualKeyboard6
Summary:        Qt 6 VirtualKeyboard library
Requires:       qt6-virtualkeyboard >= %{version}

%description -n libQt6VirtualKeyboard6
Qt VirtualKeyboard provides an input framework and reference keyboard frontend
for Qt 6.

%package -n qt6-virtualkeyboard-devel
Summary:        Qt 6 VirtualKeyboard library - Development files
Requires:       libQt6VirtualKeyboard6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Qml) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}

%description -n qt6-virtualkeyboard-devel
Development files for the Qt 6 VirtualKeyboard library.

%package -n qt6-virtualkeyboard-private-devel
Summary:        Non-ABI stable API for the Qt 6 VirtualKeyboard library
Requires:       cmake(Qt6VirtualKeyboard) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description -n qt6-virtualkeyboard-private-devel
This package provides private headers of libQt6VirtualKeyboard that do not have
any ABI or API guarantees.


### Private only library ###
%package -n libQt6HunspellInputMethod6
Summary:        Qt 6 HunspellInputMethod private library

%description -n libQt6HunspellInputMethod6
Internal library used by Qt for providing Hunspell support.
This library does not have any ABI or API guarantees.

%package -n qt6-hunspellinputmethod-private-devel
Summary:        Development files for the Qt 6 HunspellInputMethod library
Requires:       libQt6HunspellInputMethod6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6VirtualKeyboard) = %{real_version}
# Renamed in 6.2.0
Provides:       qt6-hunspellinputmethod-devel = 6.2.0
Obsoletes:      qt6-hunspellinputmethod-devel < 6.2.0

%description -n qt6-hunspellinputmethod-private-devel
Development files for the Qt 6 HunspellInputMethod library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

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
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Gui

# Only Qt6*Dependencies.cmake files are installed in these folders
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6BundledOpenwnn
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6BundledPinyin
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6BundledTcime

%ldconfig_scriptlets -n libQt6HunspellInputMethod6
%ldconfig_scriptlets -n libQt6VirtualKeyboard6

%files
%dir %{_qt6_pluginsdir}/platforminputcontexts
%{_qt6_pluginsdir}/platforminputcontexts/libqtvirtualkeyboardplugin.so

%files imports
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/

%files -n libQt6VirtualKeyboard6
%license LICENSES/*
%{_qt6_libdir}/libQt6VirtualKeyboard.so.*
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so.*

%files -n qt6-virtualkeyboard-devel
%{_qt6_cmakedir}/Qt6/FindCerence*.cmake
%{_qt6_cmakedir}/Qt6/FindMyScript.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtVirtualKeyboardTestsConfig.cmake
%{_qt6_cmakedir}/Qt6VirtualKeyboard/
%{_qt6_descriptionsdir}/VirtualKeyboard.json
%{_qt6_includedir}/QtVirtualKeyboard/
%{_qt6_libdir}/libQt6VirtualKeyboard.prl
%{_qt6_libdir}/libQt6VirtualKeyboard.so
%{_qt6_metatypesdir}/qt6virtualkeyboard_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_virtualkeyboard.pri
%{_qt6_pkgconfigdir}/Qt6HunspellInputMethod.pc
%{_qt6_pkgconfigdir}/Qt6VirtualKeyboard.pc
%exclude %{_qt6_includedir}/QtVirtualKeyboard/%{real_version}/

%files -n qt6-virtualkeyboard-private-devel
%{_qt6_cmakedir}/Qt6VirtualKeyboardSettings/
%{_qt6_descriptionsdir}/VirtualKeyboardSettings.json
%{_qt6_includedir}/QtVirtualKeyboard/%{real_version}/
%{_qt6_includedir}/QtVirtualKeyboardSettings/
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.prl
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so
%{_qt6_metatypesdir}/qt6virtualkeyboardsettings_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_virtualkeyboardsettings.pri
%{_qt6_mkspecsdir}/modules/qt_lib_virtualkeyboardsettings_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_virtualkeyboard_private.pri
%{_qt6_pkgconfigdir}/Qt6VirtualKeyboardSettings.pc

### Private only library ###

%files -n libQt6HunspellInputMethod6
%{_qt6_libdir}/libQt6HunspellInputMethod.so.*

%files -n qt6-hunspellinputmethod-private-devel
%{_qt6_cmakedir}/Qt6/FindHunspell.cmake
%{_qt6_cmakedir}/Qt6HunspellInputMethod/
%{_qt6_descriptionsdir}/HunspellInputMethod.json
%{_qt6_includedir}/QtHunspellInputMethod/
%{_qt6_libdir}/libQt6HunspellInputMethod.prl
%{_qt6_libdir}/libQt6HunspellInputMethod.so
%{_qt6_metatypesdir}/qt6hunspellinputmethod_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_hunspellinputmethod.pri
%{_qt6_mkspecsdir}/modules/qt_lib_hunspellinputmethod_private.pri

%endif

%changelog
