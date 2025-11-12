#
# spec file for package easyeffects
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


Name:           easyeffects
Version:        8.0.0
Release:        0
Summary:        Audio Effects for PipeWire Applications
License:        GPL-3.0-or-later
URL:            https://github.com/wwmm/easyeffects
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gsl-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ladspa-devel
BuildRequires:  libbs2b-devel
BuildRequires:  libebur128-devel
BuildRequires:  liblilv-0-devel
BuildRequires:  libportal-qt6-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libwebrtc-audio-processing-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  pipewire-devel
BuildRequires:  rnnoise-devel
BuildRequires:  soundtouch-devel
BuildRequires:  tbb-devel
BuildRequires:  zita-convolver-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickShapesPrivate)
BuildRequires:  cmake(Qt6WebEngineQuick)
Requires:       kf6-kirigami
Requires:       kirigami-addons6
Requires:       qt6-graphs-imports
Requires:       qt6-webengine-imports
Recommends:     lv2-calf
Recommends:     lv2-lsp-plugins
Recommends:     lv2-zam-plugins
Recommends:     mda-lv2

%description
Easy Effects is a collection of audio effects, providing limiter, compressor,
convolver, equalizer and auto volume and many other plugins for PipeWire
applications.

%lang_package

%prep
%autosetup

%build
%cmake \
  -DCMAKE_CXX_FLAGS='-isystem /usr/include/glib-2.0' \
  -DCMAKE_CXX_FLAGS='-isystem /usr/lib64/glib-2.0/include'
%cmake_build

%install
%cmake_install

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.%{name}-symbolic.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_bindir}/%{name}

%files lang -f %{name}.lang

%changelog
