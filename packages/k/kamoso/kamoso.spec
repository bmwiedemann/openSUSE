#
# spec file for package kamoso
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


%define kf6_version 6.14.0
%define qt6_version 6.7.0
#
%bcond_without released
Name:           kamoso
Version:        25.08.3
Release:        0
Summary:        Application to take pictures and videos using a webcam
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kamoso
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.26.3
BuildRequires:  pkgconfig(gstreamer-video-1.0)
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-good-qtqml6
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-purpose >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
Kamoso is an application to take pictures and videos using a webcam.
The media can be pushed to some web services such as Facebook and
YouTube.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

%files
%license LICENSES/*
%doc AUTHORS
%doc %lang(en) %{_kf6_htmldir}/en/kamoso/
%{_kf6_applicationsdir}/org.kde.kamoso.desktop
%{_kf6_appstreamdir}/org.kde.kamoso.appdata.xml
%{_kf6_bindir}/kamoso
%{_kf6_iconsdir}/hicolor/*/actions/*.*
%{_kf6_iconsdir}/hicolor/*/apps/kamoso.*
%{_kf6_notificationsdir}/kamoso.notifyrc

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kamoso

%changelog
