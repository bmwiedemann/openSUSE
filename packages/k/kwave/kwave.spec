#
# spec file for package kwave
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


%bcond_without released
Name:           kwave
Version:        24.05.2
Release:        0
Summary:        Sound editor by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kwave
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  audiofile-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw3-devel
BuildRequires:  flac-devel
BuildRequires:  id3lib-devel
BuildRequires:  libogg-devel
BuildRequires:  libopus-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(mad)
Recommends:     lame
Recommends:     toolame
Recommends:     twolame
BuildRequires:  rsvg-convert

%description
Kwave is a sound editor by KDE.

With Kwave you can edit many sorts of wav-files including multi-channel files.
You are able to alter and play back each channel on its own. Kwave also
includes many plugins (most are still under development) to transform the
wave-file in several ways and presents a graphical view with a complete zoom-
and scroll capability.

%lang_package

%prep
%autosetup -p1

# Remove "X-SuSE-translate=true" from desktop file (will be added again using "suse_update_desktop_file") - Fixes package build error
perl -pi -e "s|X-SuSE-translate=true||" kwave/org.kde.kwave.desktop.in

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.%{name} Qt KDE AudioVideo Audio Recorder AudioVideoEditing

%ldconfig_scriptlets

%files
%license GNU-LICENSE
%doc %lang(en) %{_kf5_htmldir}/en/kwave/
%{_kf5_applicationsdir}/org.kde.kwave.desktop
%{_kf5_appstreamdir}/org.kde.kwave.appdata.xml
%{_kf5_bindir}/kwave
%{_kf5_iconsdir}/hicolor/*/*/*.svgz
%{_kf5_libdir}/libkwave*.so.*
%{_kf5_plugindir}/kwave/
%{_kf5_sharedir}/kwave/

%files lang -f %{name}.lang

%changelog
