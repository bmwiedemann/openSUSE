#
# spec file for package kamoso
#
# Copyright (c) 2020 SUSE LLC
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


%define gstnum  1.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kamoso
Version:        20.08.1
Release:        0
Summary:        Application to take pictures and videos using a webcam
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://projects.kde.org/kamoso
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 0.0.9
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libudev)
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       kirigami2
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Kamoso is an application to take pictures and videos using a webcam.
The media can be pushed to some web services such as Facebook and
YouTube.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -r org.kde.kamoso Qt KDE AudioVideo Recorder

%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%files
%license COPYING
%doc AUTHORS README TODO
%{_kf5_applicationsdir}/org.kde.kamoso.desktop
%{_kf5_bindir}/kamoso
%{_kf5_iconsdir}/hicolor/*/actions/*.*
%{_kf5_iconsdir}/hicolor/*/apps/kamoso.*
%doc %lang(en) %{_kf5_htmldir}/en/kamoso/
%{_kf5_appstreamdir}/org.kde.kamoso.appdata.xml
%{_libdir}/gstreamer-%{gstnum}/gstkamosoqt5videosink.so
%{_kf5_notifydir}/kamoso.notifyrc
%{_kf5_sharedir}/sounds/kamoso-shutter.wav

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
