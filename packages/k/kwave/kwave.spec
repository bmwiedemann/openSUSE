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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kwave
Version:        24.12.2
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
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fftw3-devel
BuildRequires:  flac-devel
BuildRequires:  id3lib-devel
BuildRequires:  libogg-devel
BuildRequires:  libopus-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
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

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license GNU-LICENSE
%doc %lang(en) %{_kf6_htmldir}/en/kwave/
%{_kf6_applicationsdir}/org.kde.kwave.desktop
%{_kf6_appstreamdir}/org.kde.kwave.appdata.xml
%{_kf6_bindir}/kwave
%{_kf6_iconsdir}/hicolor/*/*/*.svgz
%{_kf6_libdir}/libkwave*.so.*
%{_kf6_plugindir}/kwave/
%{_kf6_sharedir}/kwave/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kwave/

%changelog
