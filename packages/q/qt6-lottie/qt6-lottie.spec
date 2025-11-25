#
# spec file for package qt6-lottie
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define real_version 6.10.1
%define short_version 6.10
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
Version:        6.10.1
Release:        0
Summary:        QML API for rendering graphics and animation
# LICENSE.GPL3-EXCEPT only applies to the conan recipe which is not used
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-lottie-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6GuiPrivate) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6QuickPrivate) = %{real_version}
BuildRequires:  cmake(Qt6QuickControls2) = %{real_version}
BuildRequires:  cmake(Qt6QuickTest) = %{real_version}
BuildRequires:  cmake(Qt6QuickVectorImageGeneratorPrivate) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Lottie plugin.

%if !%{qt6_docs_flavor}

%package imports
Summary:        Qt 6 Lottie QML files and plugins

%description imports
QML files and plugins from the Qt 6 Lottie module.

%package -n libQt6Lottie6
Summary:        Qt 6 Lottie library

%description -n libQt6Lottie6
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Lottie plugin.
This package provides the Qt 6 lottie library.

%package -n qt6-lottie-devel
Summary:        Qt 6 Lottie library - Development files
Requires:       libQt6Lottie6 = %{version}
Requires:       qt6-lottie = %{version}

%description -n qt6-lottie-devel
Development files for the Qt 6 Lottie library.

%package -n qt6-lottie-private-devel
Summary:        Non-ABI stable API for the Qt6 6 Lottie library
Requires:       cmake(Qt6Lottie) = %{real_version}

%description -n qt6-lottie-private-devel
This package provides private headers of libQt6Lottie that do not have any
ABI or API guarantees.

### Private only library ###


%package -n libQt6LottieVectorImageGenerator6
Summary:        Qt 6 LottieVectorImageGeneratorPrivate library

%description -n libQt6LottieVectorImageGenerator6
The Qt 6 LottieVectorImageGeneratorPrivate library.
This library does not have any ABI or API guarantees.

%package -n qt6-lottievectorimagegenerator-private-devel
Summary:        Qt 6 LottieVectorImageGeneratorPrivate library - Development files
Requires:       libQt6LottieVectorImageGenerator6 = %{version}
Requires:       cmake(Qt6Lottie) = %{real_version}
Requires:       cmake(Qt6QuickVectorImageGeneratorPrivate) = %{real_version}

%description -n qt6-lottievectorimagegenerator-private-devel
Development files for the Qt 6 LottieVectorImageGeneratorPrivate private library.
This library does not have any ABI or API guarantees.

%package -n libQt6LottieVectorImageHelpers6
Summary:        Qt 6 LottieVectorImageHelpers library

%description -n libQt6LottieVectorImageHelpers6
The Qt 6 LottieVectorImageHelpers library.
This library does not have any ABI or API guarantees.

%package -n qt6-lottievectorimagehelpers-private-devel
Summary:        Qt 6 LottieVectorImageHelpers library - Development files
Requires:       libQt6LottieVectorImageHelpers6 = %{version}
Requires:       cmake(Qt6Lottie) = %{real_version}

%description -n qt6-lottievectorimagehelpers-private-devel
Development files for the Qt 6 LottieVectorImageHelpers private library.
This library does not have any ABI or API guarantees.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 \
  -DQT_QML_NO_CACHEGEN:BOOL=TRUE \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# CMake files are not needed for plugins
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6Qml/QmlPlugins
rm %{buildroot}%{_qt6_cmakedir}/Qt6Quick/Qt6QLottieVectorImagePlugin*

%{qt6_link_executables}

%ldconfig_scriptlets -n libQt6Lottie6
%ldconfig_scriptlets -n libQt6LottieVectorImageGenerator6
%ldconfig_scriptlets -n libQt6LottieVectorImageHelpers6

%files
%{_bindir}/lottietoqml6
%{_qt6_bindir}/lottietoqml
%dir %{_qt6_pluginsdir}/vectorimageformats
%{_qt6_pluginsdir}/vectorimageformats/libqlottievectorimage.so

%files imports
%dir %{_qt6_qmldir}/Qt
%dir %{_qt6_qmldir}/Qt/labs
%{_qt6_qmldir}/Qt/labs/lottieqt/

%files -n libQt6Lottie6
%license LICENSES/*
%{_qt6_libdir}/libQt6Lottie.so.*

%files -n qt6-lottie-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_cmakedir}/Qt6Lottie/
%{_qt6_cmakedir}/Qt6LottieTools/
%{_qt6_descriptionsdir}/Lottie.json
%{_qt6_includedir}/QtLottie/
%{_qt6_libdir}/libQt6Lottie.prl
%{_qt6_libdir}/libQt6Lottie.so
%{_qt6_metatypesdir}/qt6lottie_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_lottie.pri
%{_qt6_pkgconfigdir}/Qt6Lottie.pc
%exclude %{_qt6_includedir}/QtLottie/%{real_version}

%files -n qt6-lottie-private-devel
%{_qt6_cmakedir}/Qt6LottiePrivate/
%{_qt6_includedir}/QtLottie/%{real_version}
%{_qt6_mkspecsdir}/modules/qt_lib_lottie_private.pri

### Private only library ###
%files -n libQt6LottieVectorImageGenerator6
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so.*

%files -n qt6-lottievectorimagegenerator-private-devel
%{_qt6_cmakedir}/Qt6LottieVectorImageGeneratorPrivate/
%{_qt6_descriptionsdir}/LottieVectorImageGeneratorPrivate.json
%{_qt6_includedir}/QtLottieVectorImageGenerator/
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.prl
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so
%{_qt6_metatypesdir}/qt6lottievectorimagegeneratorprivate_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_lottievectorimagegenerator_private.pri

%files -n libQt6LottieVectorImageHelpers6
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so.*

%files -n qt6-lottievectorimagehelpers-private-devel
%{_qt6_cmakedir}/Qt6LottieVectorImageHelpers/
%{_qt6_cmakedir}/Qt6LottieVectorImageHelpersPrivate/
%{_qt6_descriptionsdir}/LottieVectorImageHelpers.json
%{_qt6_includedir}/QtLottieVectorImageHelpers/
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.prl
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so
%{_qt6_metatypesdir}/qt6lottievectorimagehelpers_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_lottievectorimagehelpers*.pri
%{_qt6_pkgconfigdir}/Qt6LottieVectorImageHelpers.pc

%endif

%changelog
