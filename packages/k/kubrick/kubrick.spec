#
# spec file for package kubrick
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kubrick
Version:        20.08.2
Release:        0
Summary:        Game based on Rubik's Cube
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(glu)
Obsoletes:      kubrick5 < %{version}
Provides:       kubrick5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
This package contains the KDE game Kubrick which is based on Rubik's
Cube.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license COPYING COPYING.DOC
%doc %lang(en) %{_kf5_htmldir}/en/kubrick/
%{_kf5_applicationsdir}/org.kde.kubrick.desktop
%{_kf5_appstreamdir}/org.kde.kubrick.appdata.xml
%{_kf5_bindir}/kubrick
%{_kf5_debugdir}/kubrick.categories
%{_kf5_iconsdir}/hicolor/*/*/kubrick*
%{_kf5_kxmlguidir}/kubrick/
%{_kf5_sharedir}/kubrick/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
