#
# spec file for package qt6-multimedia
#
# Copyright (c) 2021 SUSE LLC
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


%define real_version 6.2.3
%define short_version 6.2
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
Version:        6.2.3
Release:        0
Summary:        Qt 6 Multimedia libraries
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source1:        qt6-multimedia-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
# gstreamer, alsa and pulseaudio are conflicting. gstreamer is the default
# BuildRequires:  pkgconfig(alsa)
# BuildRequires:  pkgconfig(libpulse)
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

%description -n libQt6Multimedia6
The Qt 6 Multimedia library.

%package devel
Summary:        Qt 6 Multimedia library - Development files
Requires:       libQt6Multimedia6 = %{version}
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)

%description devel
Development files for the Qt 6 Multimedia library.

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 Multimedia Library
Requires:       cmake(Qt6Multimedia) = %{real_version}

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
Requires:       cmake(Qt6Multimedia) = %{real_version}
Requires:       cmake(Qt6Widgets)

%description -n qt6-multimediawidgets-devel
Development files for the Qt 6 MultimediaWidgets library.

%package -n qt6-multimediawidgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 MultimediaWidgets Library
Requires:       cmake(Qt6MultimediaWidgets) = %{real_version}
%requires_eq    qt6-widgets-private-devel

%description -n qt6-multimediawidgets-private-devel
This package provides private headers of libQt6MultimediaWidgets that do not
have any ABI or API guarantees.

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
Requires:       cmake(Qt6Quick)

%description -n qt6-multimediaquick-private-devel
Development files for the Qt 6 Multimedia private library.
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

%fdupes %{buildroot}%{_qt6_includedir}/QtMultimedia

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins

%post -n libQt6Multimedia6 -p /sbin/ldconfig
%post -n libQt6MultimediaQuick6 -p /sbin/ldconfig
%post -n libQt6MultimediaWidgets6 -p /sbin/ldconfig
%postun -n libQt6Multimedia6 -p /sbin/ldconfig
%postun -n libQt6MultimediaQuick6 -p /sbin/ldconfig
%postun -n libQt6MultimediaWidgets6 -p /sbin/ldconfig

%files imports
%{_qt6_qmldir}/QtMultimedia/

%files -n libQt6Multimedia6
%license LICENSE.*
%{_qt6_libdir}/libQt6Multimedia.so.*

%files devel
%{_qt6_cmakedir}/Qt6/FindAVFoundation.cmake
%{_qt6_cmakedir}/Qt6/FindGObject.cmake
%{_qt6_cmakedir}/Qt6/FindGStreamer.cmake
%{_qt6_cmakedir}/Qt6/FindMMRenderer.cmake
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
%exclude %{_qt6_includedir}/QtMultimediaWidgets/%{real_version}

%files -n qt6-multimediawidgets-private-devel
%{_qt6_includedir}/QtMultimediaWidgets/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_multimediawidgets_private.pri

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

%endif

%changelog
