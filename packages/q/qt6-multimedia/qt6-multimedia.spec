#
# spec file for package qt6-multimedia
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
%define short_name qtmultimedia
%define tar_name qtmultimedia-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-multimedia%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 Multimedia libraries
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source1:        qt6-multimedia-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-quick3d-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6Quick3D) = %{real_version}
BuildRequires:  cmake(Qt6QuickControls2) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}
BuildRequires:  cmake(Qt6Svg) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
# GStreamer may cause high latencies, enable the ffmpeg backend
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Multimedia is a module that provides a set of QML types and C++
classes to handle multimedia content. It also provides APIs to access
the camera and radio functionality.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Multimedia QML files and plugins

%description imports
QML files and plugins from the Qt 6 Multimedia module.

%package -n libQt6Multimedia6
Summary:        Qt 6 Multimedia library
Requires:       qt6-multimedia = %{version}

%description -n libQt6Multimedia6
The Qt 6 Multimedia library.

%package devel
Summary:        Qt 6 Multimedia library - Development files
Requires:       libQt6Multimedia6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}

%description devel
Development files for the Qt 6 Multimedia library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Multimedia Library
Requires:       cmake(Qt6Multimedia) = %{real_version}
%requires_eq    qt6-core-private-devel
%requires_eq    qt6-gui-private-devel

%description private-devel
This package provides private headers of libQt6Multimedia that do not have any
ABI or API guarantees.

%package -n libQt6MultimediaWidgets6
Summary:        Qt 6 MultimediaWidgets library

%description -n libQt6MultimediaWidgets6
The Qt 6 MultimediaWidgets library.

%package -n qt6-multimediawidgets-devel
Summary:        Qt 6 MultimediaWidgets library - Development files
Requires:       libQt6MultimediaWidgets6 = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Multimedia) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description -n qt6-multimediawidgets-devel
Development files for the Qt 6 MultimediaWidgets library.

%package -n qt6-multimediawidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 MultimediaWidgets Library
Requires:       qt6-multimedia-private-devel = %{version}
Requires:       cmake(Qt6MultimediaWidgets) = %{real_version}
%requires_eq    qt6-widgets-private-devel

%description -n qt6-multimediawidgets-private-devel
This package provides private headers of libQt6MultimediaWidgets that do not
have any ABI or API guarantees.

%package -n libQt6SpatialAudio6
Summary:        Qt 6 SpatialAudio library

%description -n libQt6SpatialAudio6
The Qt 6 SpatialAudio library.

%package -n qt6-spatialaudio-devel
Summary:        Qt 6 SpatialAudio library - Development files
Requires:       libQt6SpatialAudio6 = %{version}
Requires:       cmake(Qt6Multimedia) = %{real_version}

%description -n qt6-spatialaudio-devel
Development files for the Qt 6 SpatialAudio library.

%package -n qt6-spatialaudio-private-devel
Summary:        Non-ABI stable API for the Qt 6 SpatialAudio Library
Requires:       cmake(Qt6SpatialAudio) = %{real_version}

%description -n qt6-spatialaudio-private-devel
This package provides private headers of libQt6SpatialAudio that do not have any
ABI or API guarantees.

### Private only library ###

%package -n libQt6MultimediaQuick6
Summary:        Qt 6 MultimediaQuick library

%description -n libQt6MultimediaQuick6
The Qt 6 MultimediaQuick library.
This library does not have any ABI or API guarantees.

%package -n qt6-multimediaquick-private-devel
Summary:        Qt 6 MultimediaQuick library - Development files
Requires:       libQt6MultimediaQuick6 = %{version}
Requires:       qt6-multimedia-private-devel = %{version}
Requires:       cmake(Qt6Multimedia) = %{real_version}
Requires:       cmake(Qt6Quick) = %{real_version}
%requires_eq    qt6-quick-private-devel

%description -n qt6-multimediaquick-private-devel
Development files for the Qt 6 Multimedia private library.
This library does not have any ABI or API guarantees.

%package -n libQt6Quick3DSpatialAudio6
Summary:        Qt 6 Quick3DSpatialAudio library

%description -n libQt6Quick3DSpatialAudio6
The Qt 6 Quick3DSpatialAudio library.
This library does not have any ABI or API guarantees.

%package -n qt6-quick3dspatialaudio-private-devel
Summary:        Qt 6 Quick3DSpatialAudio library - Development files
Requires:       libQt6Quick3DSpatialAudio6 = %{version}
Requires:       cmake(Qt6Quick3D) = %{version}
Requires:       cmake(Qt6SpatialAudio) = %{version}
%requires_eq    qt6-quick3d-private-devel

%description -n qt6-quick3dspatialaudio-private-devel
Development files for the Qt 6 Quick3DSpatialAudio private library.
This library does not have any ABI or API guarantees.

### Static libraries ###

%package -n qt6-bundledresonanceaudio-devel-static
Summary:        Qt6 BundledResonanceAudio static library
%requires_eq    qt6-core-private-devel

%description -n qt6-bundledresonanceaudio-devel-static
The Qt6 BundledResonanceAudio static library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake_qt6 \
  -DINPUT_gstreamer:BOOL=ON \
  -DINPUT_ffmpeg:BOOL=ON

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%fdupes %{buildroot}%{_qt6_includedir}/QtMultimedia

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{Config,Targets}*.cmake

# The GstreamerMediaPlugin library has a limited usage outside of Qt development
# (needed to create unit tests for the gstreamer plugin)
rm %{buildroot}%{_qt6_cmakedir}/Qt6Multimedia/Qt6QGstreamerMediaPluginAdditionalTargetInfo.cmake
rm %{buildroot}%{_qt6_descriptionsdir}/QGstreamerMediaPluginPrivate.json
rm %{buildroot}%{_qt6_libdir}/libQt6QGstreamerMediaPlugin.a
rm %{buildroot}%{_qt6_libdir}/libQt6QGstreamerMediaPlugin.prl
rm %{buildroot}%{_qt6_metatypesdir}/qt6qgstreamermediapluginprivate_*_metatypes.json
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_qgstreamermediaplugin_private.pri
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6QGstreamerMediaPluginPrivate/
rm -r %{buildroot}%{_qt6_includedir}/QtQGstreamerMediaPlugin/

%ldconfig_scriptlets -n libQt6Multimedia6
%ldconfig_scriptlets -n libQt6MultimediaQuick6
%ldconfig_scriptlets -n libQt6MultimediaWidgets6
%ldconfig_scriptlets -n libQt6Quick3DSpatialAudio6
%ldconfig_scriptlets -n libQt6SpatialAudio6

%files
%{_qt6_pluginsdir}/multimedia/

%files imports
%{_qt6_qmldir}/QtMultimedia/
%{_qt6_qmldir}/QtQuick3D/

%files -n libQt6Multimedia6
%license LICENSES/*
%{_qt6_libdir}/libQt6Multimedia.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindAVFoundation.cmake
%{_qt6_cmakedir}/Qt6/FindFFmpeg.cmake
%{_qt6_cmakedir}/Qt6/FindGObject.cmake
%{_qt6_cmakedir}/Qt6/FindGStreamer.cmake
%{_qt6_cmakedir}/Qt6/FindMMRenderer.cmake
%{_qt6_cmakedir}/Qt6/FindMMRendererCore.cmake
%{_qt6_cmakedir}/Qt6/FindVAAPI.cmake
%{_qt6_cmakedir}/Qt6/FindWMF.cmake
%{_qt6_cmakedir}/Qt6/FindWrapPulseAudio.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtMultimediaTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Multimedia/
%{_qt6_descriptionsdir}/Multimedia.json
%{_qt6_includedir}/QtMultimedia/
%{_qt6_libdir}/libQt6Multimedia.prl
%{_qt6_libdir}/libQt6Multimedia.so
%{_qt6_metatypesdir}/qt6multimedia_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_multimedia.pri
%{_qt6_pkgconfigdir}/Qt6Multimedia.pc
%exclude %{_qt6_includedir}/QtMultimedia/%{real_version}

%files private-devel
%{_qt6_includedir}/QtMultimedia/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_multimedia_private.pri

%files -n libQt6MultimediaWidgets6
%{_qt6_libdir}/libQt6MultimediaWidgets.so.*

%files -n qt6-multimediawidgets-devel
%{_qt6_cmakedir}/Qt6MultimediaWidgets/
%{_qt6_descriptionsdir}/MultimediaWidgets.json
%{_qt6_includedir}/QtMultimediaWidgets/
%{_qt6_libdir}/libQt6MultimediaWidgets.prl
%{_qt6_libdir}/libQt6MultimediaWidgets.so
%{_qt6_metatypesdir}/qt6multimediawidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_multimediawidgets.pri
%{_qt6_pkgconfigdir}/Qt6MultimediaWidgets.pc
%exclude %{_qt6_includedir}/QtMultimediaWidgets/%{real_version}

%files -n qt6-multimediawidgets-private-devel
%{_qt6_includedir}/QtMultimediaWidgets/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_multimediawidgets_private.pri

%files -n libQt6SpatialAudio6
%{_qt6_libdir}/libQt6SpatialAudio.so.*

%files -n qt6-spatialaudio-devel
%{_qt6_cmakedir}/Qt6SpatialAudio/
%{_qt6_descriptionsdir}/SpatialAudio.json
%{_qt6_includedir}/QtSpatialAudio/
%{_qt6_libdir}/libQt6SpatialAudio.prl
%{_qt6_libdir}/libQt6SpatialAudio.so
%{_qt6_metatypesdir}/qt6spatialaudio_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_spatialaudio.pri
%{_qt6_pkgconfigdir}/Qt6SpatialAudio.pc
%exclude %{_qt6_includedir}/QtSpatialAudio/%{real_version}

%files -n qt6-spatialaudio-private-devel
%{_qt6_includedir}/QtSpatialAudio/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_spatialaudio_private.pri

### Private only library ###

%files -n libQt6MultimediaQuick6
%{_qt6_libdir}/libQt6MultimediaQuick.so.*

%files -n qt6-multimediaquick-private-devel
%{_qt6_cmakedir}/Qt6MultimediaQuickPrivate/
%{_qt6_descriptionsdir}/MultimediaQuickPrivate.json
%{_qt6_includedir}/QtMultimediaQuick/
%{_qt6_libdir}/libQt6MultimediaQuick.prl
%{_qt6_libdir}/libQt6MultimediaQuick.so
%{_qt6_metatypesdir}/qt6multimediaquickprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_multimediaquick_private.pri

%files -n libQt6Quick3DSpatialAudio6
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so.*

%files -n qt6-quick3dspatialaudio-private-devel
%{_qt6_cmakedir}/Qt6Quick3DSpatialAudioPrivate/
%{_qt6_descriptionsdir}/Quick3DSpatialAudioPrivate.json
%{_qt6_includedir}/QtQuick3DSpatialAudio/
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.prl
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so
%{_qt6_metatypesdir}/qt6quick3dspatialaudioprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_quick3dspatialaudio_private.pri

### Static libraries ###

%files -n qt6-bundledresonanceaudio-devel-static
%{_qt6_cmakedir}/Qt6/FindWrapBundledResonanceAudioConfigExtra.cmake
%{_qt6_cmakedir}/Qt6BundledResonanceAudio/
%{_qt6_libdir}/libQt6BundledResonanceAudio.a

%endif

%changelog
