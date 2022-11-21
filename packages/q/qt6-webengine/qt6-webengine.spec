#
# spec file for package qt6-webengine
#
# Copyright (c) 2022 SUSE LLC
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


%define real_version 6.4.1
%define short_version 6.4
%define tar_name qtwebengine-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%define no_flavor ("%qt6_flavor" == "")
#
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
%if %{?suse_version} > 1500 || 0%{?sle_version} > 150300
%bcond_without system_vpx
# icu >= 68 is required
%bcond_without system_icu
%define _use_system_icu ON
%else
%bcond_with system_vpx
%bcond_with system_icu
%define _use_system_icu OFF
%endif
%bcond_without system_ffmpeg
%bcond_without system_minizip
#
Name:           qt6-webengine%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Web browser engine for Qt applications
License:        GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-webengine-rpmlintrc
# Patches 0-100 are upstream patches #
# Patches 100-200 are openSUSE and/or non-upstream(able) patches #
Patch100:       rtc-dont-use-h264.patch
#
# Chromium/blink don't support PowerPC and zSystems and build fails on
# 32 bits archs (https://bugreports.qt.io/browse/QTBUG-102143)
ExclusiveArch:  aarch64 x86_64 riscv64
BuildRequires:  Mesa-KHR-devel
BuildRequires:  bison
# Not pulled automatically on Leap
BuildRequires:  cups-config
BuildRequires:  cups-devel
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  krb5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 1.6.0
BuildRequires:  memory-constraints
BuildRequires:  nodejs-default
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-html5lib
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-quickwidgets-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  snappy-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlModels)
BuildRequires:  cmake(Qt6QmlTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsTools)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(harfbuzz) >= 2.4.0
%if %{with system_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 68
BuildRequires:  pkgconfig(icu-uc) >= 68
%endif
BuildRequires:  pkgconfig(lcms2)
%if %{with system_ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse) >= 0.9.10
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(opus) >= 1.3.1
BuildRequires:  pkgconfig(re2)
%if %{with system_vpx}
BuildRequires:  pkgconfig(vpx) >= 1.10.0
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
%if %{with system_minizip}
BuildRequires:  pkgconfig(minizip)
%endif
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt WebEngine module provides a web browser engine to embed web content into
Qt applications.
The functionality in Qt WebEngine is divided into the following
modules:
* Qt WebEngine Core module for interacting with Chromium
* Qt WebEngine Widgets module for creating widget-based web applications
* Qt WebEngine module for creating Qt Quick based web applications

%if %{no_flavor}

%package imports
Summary:        Qt 6 WebEngine QML files and plugins

%description imports
QML files and plugins from the Qt 6 WebEngine module

%package -n libQt6Pdf6
Summary:        Qt6 Pdf library

%description -n libQt6Pdf6
The Qt6 Pdf library.

%package -n qt6-pdf-imports
Summary:        Qt 6 Pdf QML files and plugins

%description -n qt6-pdf-imports
QML files and plugins from the Qt 6 Pdf module

%package -n qt6-pdf-devel
Summary:        Development files for the Qt 6 Pdf library
Requires:       libQt6Pdf6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)

%description -n qt6-pdf-devel
Development files for the Qt 6 Pdf library.

%package -n qt6-pdf-private-devel
Summary:        Non-ABI stable API for the Qt 6 Pdf library
Requires:       cmake(Qt6Pdf) = %{real_version}

%description -n qt6-pdf-private-devel
This package provides private headers of libQt6Pdf that do not have any
ABI or API guarantees.

%package -n libQt6PdfQuick6
Summary:        Qt6 PdfQuick library

%description -n libQt6PdfQuick6
The Qt6 PdfQuick library.

%package -n qt6-pdfquick-devel
Summary:        Development files for the Qt 6 PdfQuick library
Requires:       libQt6PdfQuick6 = %{version}
Requires:       qt6-pdf-private-devel = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Qml)
%requires_eq    qt6-quick-private-devel

%description -n qt6-pdfquick-devel
Development files for the Qt 6 PdfQuick library.

%package -n qt6-pdfquick-private-devel
Summary:        Non-ABI stable API for the Qt 6 PdfQuick library
Requires:       cmake(Qt6PdfQuick) = %{real_version}

%description -n qt6-pdfquick-private-devel
This package provides private headers of libQt6PdfQuick that do not have any
ABI or API guarantees.

%package -n libQt6PdfWidgets6
Summary:        Qt6 PdfWidgets library

%description -n libQt6PdfWidgets6
The Qt6 PdfWidgets library.

%package -n qt6-pdfwidgets-devel
Summary:        Development files for the Qt 6 PdfWidgets library
Requires:       libQt6PdfWidgets6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Pdf) = %{real_version}
Requires:       cmake(Qt6Widgets)

%description -n qt6-pdfwidgets-devel
Development files for the Qt 6 PdfWidgets library.

%package -n qt6-pdfwidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 PdfWidgets library
Requires:       cmake(Qt6PdfWidgets) = %{real_version}

%description -n qt6-pdfwidgets-private-devel
This package provides private headers of libQt6PdfWidgets that do not have any
ABI or API guarantees.

%package -n libQt6WebEngineCore6
Summary:        Qt6 WebEngineCore library
Requires:       qt6-webengine = %{version}

%description -n libQt6WebEngineCore6
The Qt6 WebEngineCore library.

%package -n qt6-webenginecore-devel
Summary:        Development files for the Qt 6 WebEngineCore library
Requires:       libQt6WebEngineCore6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Positioning)
Requires:       cmake(Qt6Quick)
Requires:       cmake(Qt6WebChannel)

%description -n qt6-webenginecore-devel
Development files for the Qt 6 WebEngineCore library.

%package -n qt6-webenginecore-private-devel
Summary:        Non-ABI stable API for the Qt 6 WebEngineCore library
Requires:       cmake(Qt6WebEngineCore) = %{real_version}

%description -n qt6-webenginecore-private-devel
This package provides private headers of libQt6WebEngineCore that do not have any
ABI or API guarantees.

%package -n libQt6WebEngineQuick6
Summary:        Qt6 WebEngineQuick library
Requires:       qt6-webengine-imports = %{version}

%description -n libQt6WebEngineQuick6
The Qt6 WebEngineQuick library.

%package -n qt6-webenginequick-devel
Summary:        Development files for the Qt 6 WebEngineQuick library
Requires:       libQt6WebEngineQuick6 = %{version}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6WebEngineCore) = %{real_version}

%description -n qt6-webenginequick-devel
Development files for the Qt 6 WebEngineQuick library.

%package -n qt6-webenginequick-private-devel
Summary:        Non-ABI stable API for the Qt 6 WebEngineQuick library
Requires:       cmake(Qt6WebEngineQuick) = %{real_version}

%description -n qt6-webenginequick-private-devel
This package provides private headers of libQt6WebEngineQuick that do not have any
ABI or API guarantees.

%package -n libQt6WebEngineWidgets6
Summary:        Qt6 WebEngineWidgets library

%description -n libQt6WebEngineWidgets6
The Qt6 WebEngineWidgets library.

%package -n qt6-webenginewidgets-devel
Summary:        Development files for the Qt 6 WebEngineWidgets library
Requires:       libQt6WebEngineWidgets6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6PrintSupport)
Requires:       cmake(Qt6QuickWidgets)
Requires:       cmake(Qt6WebEngineCore)
%requires_eq    qt6-quick-private-devel

%description -n qt6-webenginewidgets-devel
Development files for the Qt 6 WebEngineWidgets library.

%package -n qt6-webenginewidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 WebEngineWidgets library
Requires:       cmake(Qt6WebEngineWidgets) = %{real_version}

%description -n qt6-webenginewidgets-private-devel
This package provides private headers of libQt6WebEngineWidgets that do not have any
ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%if %{no_flavor}
# Determine the right number of parallel processes based on the available memory
# Copied from the Qt 5 webengine package
%limit_build -m 2750
%endif

# Ensure that also the internal chromium build follows the right number of
# parallel processes instead of its defaults.
export NINJAFLAGS="%{?_smp_mflags}"

%cmake_qt6 \
  -DCMAKE_TOOLCHAIN_FILE:STRING="%{_qt6_cmakedir}/Qt6/qt.toolchain.cmake" \
  -DFEATURE_qtpdf_build:BOOL=ON \
  -DFEATURE_webengine_developer_build:BOOL=OFF \
  -DFEATURE_webengine_embedded_build:BOOL=OFF \
  -DFEATURE_webengine_extensions:BOOL=ON \
  -DFEATURE_webengine_printing_and_pdf:BOOL=ON \
  -DFEATURE_webengine_kerberos:BOOL=ON \
  -DFEATURE_webengine_native_spellchecker:BOOL=OFF \
  -DFEATURE_webengine_system_libevent:BOOL=ON \
  -DFEATURE_webengine_webrtc:BOOL=ON \
  -DFEATURE_webengine_webrtc_pipewire:BOOL=ON \
  -DFEATURE_webengine_system_icu:BOOL=%{_use_system_icu} \
%if %{with system_ffmpeg}
  -DFEATURE_webengine_system_ffmpeg:BOOL=ON \
  -DFEATURE_webengine_proprietary_codecs:BOOL=ON \
%endif
  -DQT_BUILD_EXAMPLES:BOOL=ON

%{qt6_build}

%install
%{qt6_install}

%if %{no_flavor}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Designer/
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Gui/
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

# This shouldn't be needed
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6BuildInternals

%post -n libQt6Pdf6 -p /sbin/ldconfig
%post -n libQt6PdfQuick6 -p /sbin/ldconfig
%post -n libQt6PdfWidgets6 -p /sbin/ldconfig
%post -n libQt6WebEngineCore6 -p /sbin/ldconfig
%post -n libQt6WebEngineQuick6 -p /sbin/ldconfig
%post -n libQt6WebEngineWidgets6 -p /sbin/ldconfig
%postun -n libQt6Pdf6 -p /sbin/ldconfig
%postun -n libQt6PdfQuick6 -p /sbin/ldconfig
%postun -n libQt6PdfWidgets6 -p /sbin/ldconfig
%postun -n libQt6WebEngineCore6 -p /sbin/ldconfig
%postun -n libQt6WebEngineQuick6 -p /sbin/ldconfig
%postun -n libQt6WebEngineWidgets6 -p /sbin/ldconfig

%files
%dir %{_qt6_pluginsdir}/designer
%{_qt6_datadir}/resources/
%{_qt6_translationsdir}/qtwebengine_locales/
%{_qt6_libexecdir}/QtWebEngineProcess
%{_qt6_pluginsdir}/designer/libqwebengineview.so

%files imports
%{_qt6_qmldir}/QtWebEngine/

%files -n libQt6Pdf6
%dir %{_qt6_pluginsdir}/imageformats
%{_qt6_libdir}/libQt6Pdf.so.*
%{_qt6_pluginsdir}/imageformats/libqpdf.so

%files -n qt6-pdf-imports
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_qmldir}/QtQuick/Pdf

%files -n qt6-pdf-devel
%{_qt6_cmakedir}/Qt6Pdf/
%{_qt6_descriptionsdir}/Pdf.json
%{_qt6_includedir}/QtPdf/
%{_qt6_libdir}/libQt6Pdf.prl
%{_qt6_libdir}/libQt6Pdf.so
%{_qt6_metatypesdir}/qt6pdf_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_pdf.pri
%{_qt6_pkgconfigdir}/Qt6Pdf.pc
%exclude %{_qt6_includedir}/QtPdf/%{real_version}

%files -n qt6-pdf-private-devel
%{_qt6_includedir}/QtPdf/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_pdf_private.pri

%files -n libQt6PdfQuick6
%{_qt6_libdir}/libQt6PdfQuick.so.*

%files -n qt6-pdfquick-devel
%{_qt6_cmakedir}/Qt6PdfQuick/
%{_qt6_descriptionsdir}/PdfQuick.json
%{_qt6_includedir}/QtPdfQuick/
%{_qt6_libdir}/libQt6PdfQuick.prl
%{_qt6_libdir}/libQt6PdfQuick.so
%{_qt6_metatypesdir}/qt6pdfquick_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_pdfquick.pri
%{_qt6_pkgconfigdir}/Qt6PdfQuick.pc
%exclude %{_qt6_includedir}/QtPdfQuick/%{real_version}

%files -n qt6-pdfquick-private-devel
%{_qt6_includedir}/QtPdfQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_pdfquick_private.pri

%files -n libQt6PdfWidgets6
%{_qt6_libdir}/libQt6PdfWidgets.so.*

%files -n qt6-pdfwidgets-devel
%{_qt6_cmakedir}/Qt6PdfWidgets/
%{_qt6_descriptionsdir}/PdfWidgets.json
%{_qt6_includedir}/QtPdfWidgets/
%{_qt6_libdir}/libQt6PdfWidgets.prl
%{_qt6_libdir}/libQt6PdfWidgets.so
%{_qt6_metatypesdir}/qt6pdfwidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_pdfwidgets.pri
%{_qt6_pkgconfigdir}/Qt6PdfWidgets.pc
%exclude %{_qt6_includedir}/QtPdfWidgets/%{real_version}

%files -n qt6-pdfwidgets-private-devel
%{_qt6_includedir}/QtPdfWidgets/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_pdfwidgets_private.pri

%files -n libQt6WebEngineCore6
%license LICENSES/*
%{_qt6_libdir}/libQt6WebEngineCore.so.*

%files -n qt6-webenginecore-devel
%{_qt6_cmakedir}/Qt6/FindGPerf.cmake
%{_qt6_cmakedir}/Qt6/FindGn.cmake
%{_qt6_cmakedir}/Qt6/FindNinja.cmake
%{_qt6_cmakedir}/Qt6/FindNodejs.cmake
%{_qt6_cmakedir}/Qt6/FindPkgConfigHost.cmake
%{_qt6_cmakedir}/Qt6/FindSnappy.cmake
%{_qt6_cmakedir}/Qt6WebEngineCore/
%{_qt6_cmakedir}/Qt6WebEngineCoreTools/
%{_qt6_descriptionsdir}/WebEngineCore.json
%{_qt6_includedir}/QtWebEngineCore/
%{_qt6_libdir}/libQt6WebEngineCore.prl
%{_qt6_libdir}/libQt6WebEngineCore.so
%{_qt6_libexecdir}/gn
%{_qt6_libexecdir}/qwebengine_convert_dict
%{_qt6_metatypesdir}/qt6webenginecore_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webenginecore.pri
%{_qt6_pkgconfigdir}/Qt6WebEngineCore.pc
%exclude %{_qt6_includedir}/QtWebEngineCore/%{real_version}

%files -n qt6-webenginecore-private-devel
%{_qt6_includedir}/QtWebEngineCore/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webenginecore_private.pri

%files -n libQt6WebEngineQuick6
%{_qt6_libdir}/libQt6WebEngineQuick.so.*
%{_qt6_libdir}/libQt6WebEngineQuickDelegatesQml.so.*

%files -n qt6-webenginequick-devel
%{_qt6_cmakedir}/Qt6WebEngineQuick/
%{_qt6_cmakedir}/Qt6WebEngineQuickDelegatesQml/
%{_qt6_descriptionsdir}/WebEngineQuick.json
%{_qt6_descriptionsdir}/WebEngineQuickDelegatesQml.json
%{_qt6_includedir}/QtWebEngineQuick/
%{_qt6_libdir}/libQt6WebEngineQuick.prl
%{_qt6_libdir}/libQt6WebEngineQuick.so
%{_qt6_libdir}/libQt6WebEngineQuickDelegatesQml.prl
%{_qt6_libdir}/libQt6WebEngineQuickDelegatesQml.so
%{_qt6_metatypesdir}/qt6webenginequick_*_metatypes.json
%{_qt6_metatypesdir}/qt6webenginequickdelegatesqml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webenginequick.pri
%{_qt6_mkspecsdir}/modules/qt_lib_webenginequickdelegatesqml.pri
%{_qt6_pkgconfigdir}/Qt6WebEngineQuick.pc
%{_qt6_pkgconfigdir}/Qt6WebEngineQuickDelegatesQml.pc
%exclude %{_qt6_includedir}/QtWebEngineQuick/%{real_version}

%files -n qt6-webenginequick-private-devel
%{_qt6_includedir}/QtWebEngineQuick/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webenginequick_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_webenginequickdelegatesqml_private.pri

%files -n libQt6WebEngineWidgets6
%{_qt6_libdir}/libQt6WebEngineWidgets.so.*

%files -n qt6-webenginewidgets-devel
%{_qt6_cmakedir}/Qt6WebEngineWidgets/
%{_qt6_descriptionsdir}/WebEngineWidgets.json
%{_qt6_includedir}/QtWebEngineWidgets/
%{_qt6_libdir}/libQt6WebEngineWidgets.prl
%{_qt6_libdir}/libQt6WebEngineWidgets.so
%{_qt6_metatypesdir}/qt6webenginewidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_webenginewidgets.pri
%{_qt6_pkgconfigdir}/Qt6WebEngineWidgets.pc
%exclude %{_qt6_includedir}/QtWebEngineWidgets/%{real_version}

%files -n qt6-webenginewidgets-private-devel
%{_qt6_includedir}/QtWebEngineWidgets/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_webenginewidgets_private.pri

%endif

%changelog
