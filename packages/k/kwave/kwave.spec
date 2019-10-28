#
# spec file for package kwave
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kwave
Version:        19.08.2
Release:        0
Summary:        Sound Editor designed for KDE
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  audiofile-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw3-devel
BuildRequires:  flac-devel
BuildRequires:  id3lib-devel
BuildRequires:  karchive-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libogg-devel
BuildRequires:  libopus-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1500
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(mad)
Recommends:     %{name}-lang
Recommends:     lame
Recommends:     toolame
Recommends:     twolame

%description
Kwave is a sound editor designed for the KDE Desktop Environment.

With Kwave you can edit many sorts of wav-files including multi-channel files.
You are able to alter and play back each channel on its own. Kwave also
includes many plugins (most are still under development) to transform the
wave-file in several ways and presents a graphical view with a complete zoom-
and scroll capability.

%lang_package

%prep
%setup -q

# Remove "X-SuSE-translate=true" from desktop file (will be added again using "suse_update_desktop_file") - Fixes package build error
perl -pi -e "s|X-SuSE-translate=true||" kwave/org.kde.kwave.desktop.in

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.%{name} Qt KDE AudioVideo Audio Recorder AudioVideoEditing

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license GNU-LICENSE
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/kwave/
%{_kf5_applicationsdir}/org.kde.kwave.desktop
%{_kf5_appstreamdir}/org.kde.kwave.appdata.xml
%{_kf5_bindir}/kwave
%{_kf5_iconsdir}/hicolor/*/*/*.svgz
%{_kf5_libdir}/libkwave*.so.*
%{_kf5_plugindir}/kwave/
%{_kf5_servicetypesdir}/kwave-plugin.desktop
%{_kf5_sharedir}/kwave/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
