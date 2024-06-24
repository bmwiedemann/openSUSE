#
# spec file for package qt6-webview
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
%define tar_name qtwebview-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-webview%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 WebView library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-webenginecore-private-devel
BuildRequires:  qt6-webenginequick-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6OpenGL) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6WebEngineCore) = %{real_version}
BuildRequires:  cmake(Qt6WebEngineQuick) = %{real_version}
# Only available where qtwebengine is
ExclusiveArch:  aarch64 x86_64 %x86_64 riscv64
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt WebView lets you display web content inside a QML application. To avoid
including a full web browser stack, Qt WebView uses native APIs where
appropriate.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 WebView QML files and plugins

%description imports
QML files and plugins from the Qt 6 WebView module

%package -n libQt6WebView6
Summary:        Qt 6 WebView library

%description -n libQt6WebView6
Qt WebView lets you display web content inside a QML application. To avoid
including a full web browser stack, Qt WebView uses native APIs where
appropriate.

%package devel
Summary:        Qt 6 WebView library - Development files
Requires:       libQt6WebView6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}

%description devel
Development files for the Qt 6 WebView library

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 WebView library
Requires:       cmake(Qt6WebView) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description private-devel
This package provides private headers of libQt6WebView that do not have any
ABI or API guarantees.

%package -n libQt6WebViewQuick6
Summary:        Qt 6 WebViewQuick library

%description -n libQt6WebViewQuick6
The Qt6 WebViewQuick library.

%package -n qt6-webviewquick-devel
Summary:        Qt 6 WebViewQuick library - Development files
Requires:       libQt6WebViewQuick6 = %{version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6QmlModels) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
Requires:       cmake(Qt6WebView) = %{real_version}

%description -n qt6-webviewquick-devel
Development files for the Qt 6 WebViewQuick library.

%package -n qt6-webviewquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 WebViewQuick library
Requires:       cmake(Qt6WebViewQuick) = %{real_version}

%description -n qt6-webviewquick-private-devel
This package provides private headers of libQt6WebViewQuick that do not have any
ABI or API guarantees.

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
rm %{buildroot}%{_qt6_cmakedir}/Qt6WebView/*Plugin*.cmake

%ldconfig_scriptlets -n libQt6WebView6
%ldconfig_scriptlets -n libQt6WebViewQuick6

%files
%{_qt6_pluginsdir}/webview/

%files imports
%{_qt6_qmldir}/QtWebView/

%files -n libQt6WebView6
%license LICENSES/*
%{_qt6_libdir}/libQt6WebView.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtWebViewTestsConfig.cmake
%{_qt6_cmakedir}/Qt6WebView/
%{_qt6_descriptionsdir}/WebView.json
%{_qt6_includedir}/QtWebView/
%{_qt6_libdir}/libQt6WebView.prl
%{_qt6_libdir}/libQt6WebView.so
%{_qt6_metatypesdir}/qt6webview_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webview.pri
%{_qt6_pkgconfigdir}/Qt6WebView.pc
%exclude %{_qt6_includedir}/QtWebView/%{real_version}/

%files private-devel
%{_qt6_includedir}/QtWebView/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webview_private.pri

%files -n libQt6WebViewQuick6
%{_qt6_libdir}/libQt6WebViewQuick.so.*

%files -n qt6-webviewquick-devel
%{_qt6_cmakedir}/Qt6WebViewQuick/
%{_qt6_descriptionsdir}/WebViewQuick.json
%{_qt6_includedir}/QtWebViewQuick/
%{_qt6_libdir}/libQt6WebViewQuick.prl
%{_qt6_libdir}/libQt6WebViewQuick.so
%{_qt6_metatypesdir}/qt6webviewquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webviewquick.pri
%{_qt6_pkgconfigdir}/Qt6WebViewQuick.pc
%exclude %{_qt6_includedir}/QtWebViewQuick/%{real_version}/

%files -n qt6-webviewquick-private-devel
%{_qt6_includedir}/QtWebViewQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webviewquick_private.pri

%endif

%changelog
