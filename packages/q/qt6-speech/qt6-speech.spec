#
# spec file for package qt6-speech
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
%define tar_name qtspeech-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
# Not available in Leap 15
%if 0%{?suse_version} > 1500
%bcond_without flite
%endif
Name:           qt6-speech%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Qt 6 TextToSpeech Library and Plugin
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
%if %{with flite}
# Flite is built without Alsa, adding it to BuildRequires isn't needed
BuildRequires:  flite-devel > 2.0
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Multimedia) = %{real_version}
BuildRequires:  cmake(Qt6Qml) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
BuildRequires:  pkgconfig(speech-dispatcher)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The QTextToSpeech class provides a convenient access to text-to-speech engines.

%if !%{qt6_docs_flavor}

%package -n qt6-texttospeech
Summary:         Qt 6 TextToSpeech plugin

%description -n qt6-texttospeech
Qt 6 TextToSpeech plugin.

%package -n libQt6TextToSpeech6
Summary:        Qt 6 TextToSpeech library
Requires:       qt6-texttospeech = %{version}

%description -n libQt6TextToSpeech6
The QTextToSpeech class provides a convenient access to text-to-speech engines.

%package -n qt6-texttospeech-devel
Summary:        Qt 6 TextToSpeech library - Development files
Requires:       libQt6TextToSpeech6 = %{version}
Requires:       cmake(Qt6QmlIntegration) = %{real_version}

%description -n qt6-texttospeech-devel
Development files for the Qt 6 TextToSpeech library.

%package -n qt6-texttospeech-private-devel
Summary:        Non-ABI stable API for the Qt 6 TextToSpeech library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6TextToSpeech) = %{real_version}

%description -n qt6-texttospeech-private-devel
This package provides private headers of libQt6TextToSpeech that do not have
any ABI or API guarantees.

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

%ldconfig_scriptlets -n libQt6TextToSpeech6

%files -n qt6-texttospeech
%dir %{_qt6_pluginsdir}/texttospeech/
%if %{with flite}
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_flite.so
%endif
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_mock.so
%{_qt6_pluginsdir}/texttospeech/libqtexttospeech_speechd.so
%{_qt6_qmldir}/QtTextToSpeech/

%files -n libQt6TextToSpeech6
%license LICENSES/*
%{_qt6_libdir}/libQt6TextToSpeech.so.*

%files -n qt6-texttospeech-devel
%{_qt6_cmakedir}/Qt6/FindFlite.cmake
%{_qt6_cmakedir}/Qt6/FindSpeechDispatcher.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtSpeechTestsConfig.cmake
%{_qt6_cmakedir}/Qt6TextToSpeech/
%{_qt6_descriptionsdir}/TextToSpeech.json
%{_qt6_includedir}/QtTextToSpeech/
%{_qt6_libdir}/libQt6TextToSpeech.prl
%{_qt6_libdir}/libQt6TextToSpeech.so
%{_qt6_metatypesdir}/qt6texttospeech_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_texttospeech.pri
%{_qt6_pkgconfigdir}/Qt6TextToSpeech.pc
%exclude %{_qt6_includedir}/QtTextToSpeech/%{real_version}

%files -n qt6-texttospeech-private-devel
%{_qt6_cmakedir}/Qt6TextToSpeechPrivate/
%{_qt6_includedir}/QtTextToSpeech/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_texttospeech_private.pri

%endif

%changelog
