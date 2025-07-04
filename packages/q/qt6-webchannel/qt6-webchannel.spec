#
# spec file for package qt6-webchannel
#
# Copyright (c) 2025 SUSE LLC
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


%define real_version 6.9.1
%define short_version 6.9
%define tar_name qtwebchannel-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-webchannel%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Qt 6 WebChannel library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-webchannel-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6Test) = %{real_version}
BuildRequires:  cmake(Qt6WebSockets) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt WebChannel enables peer-to-peer communication between a server
(QML/C++ application) and a client (HTML/JavaScript or QML
application).

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 WebChannel QML files and plugins

%description imports
QML files and plugins from the Qt 6 WebChannel module

%package -n libQt6WebChannel6
Summary:        Qt 6 WebChannel library

%description -n libQt6WebChannel6
The Qt 6 WebChannel library.

%package devel
Summary:        Qt 6 WebChannel library - Development files
Requires:       libQt6WebChannel6 = %{version}
Requires:       cmake(Qt6Qml) = %{real_version}

%description devel
Development files for the Qt 6 WebChannel library

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 WebChannel library
Requires:       cmake(Qt6WebChannel) = %{real_version}

%description private-devel
This package provides private headers of libQt6WebChannel that do not have any
ABI or API guarantees.

%package -n libQt6WebChannelQuick6
Summary:        Qt 6 WebChannelQuick library

%description -n libQt6WebChannelQuick6
The Qt 6 WebChannelQuick library.

%package -n qt6-webchannelquick-devel
Summary:        Qt 6 WebChannelQuick library - Development files
Requires:       libQt6WebChannelQuick6 = %{version}
Requires:       cmake(Qt6WebChannel) = %{real_version}

%description -n qt6-webchannelquick-devel
Development files for the Qt 6 WebChannelQuick library

%package -n qt6-webchannelquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 WebChannelQuick library
Requires:       cmake(Qt6WebChannelQuick) = %{real_version}

%description -n qt6-webchannelquick-private-devel
This package provides private headers of libQt6WebChannelQuick that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%fdupes %{buildroot}

%ldconfig_scriptlets -n libQt6WebChannel6
%ldconfig_scriptlets -n libQt6WebChannelQuick6

%files imports
%{_qt6_qmldir}/QtWebChannel/

%files -n libQt6WebChannel6
%license LICENSES/*
%{_qt6_libdir}/libQt6WebChannel.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtWebChannelTestsConfig.cmake
%{_qt6_cmakedir}/Qt6WebChannel/
%{_qt6_descriptionsdir}/WebChannel.json
%{_qt6_includedir}/QtWebChannel/
%{_qt6_libdir}/libQt6WebChannel.prl
%{_qt6_libdir}/libQt6WebChannel.so
%{_qt6_metatypesdir}/qt6webchannel_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webchannel.pri
%{_qt6_pkgconfigdir}/Qt6WebChannel.pc
%exclude %{_qt6_includedir}/QtWebChannel/%{real_version}/

%files private-devel
%{_qt6_cmakedir}/Qt6WebChannelPrivate/
%{_qt6_includedir}/QtWebChannel/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webchannel_private.pri

%files -n libQt6WebChannelQuick6
%license LICENSES/*
%{_qt6_libdir}/libQt6WebChannelQuick.so.*

%files -n qt6-webchannelquick-devel
%{_qt6_cmakedir}/Qt6WebChannelQuick/
%{_qt6_descriptionsdir}/WebChannelQuick.json
%{_qt6_includedir}/QtWebChannelQuick/
%{_qt6_libdir}/libQt6WebChannelQuick.prl
%{_qt6_libdir}/libQt6WebChannelQuick.so
%{_qt6_metatypesdir}/qt6webchannelquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webchannelquick.pri
%{_qt6_pkgconfigdir}/Qt6WebChannelQuick.pc
%exclude %{_qt6_includedir}/QtWebChannelQuick/%{real_version}/

%files -n qt6-webchannelquick-private-devel
%{_qt6_cmakedir}/Qt6WebChannelQuickPrivate/
%{_qt6_includedir}/QtWebChannelQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webchannelquick_private.pri

%endif

%changelog
