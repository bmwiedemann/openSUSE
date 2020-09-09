#
# spec file for package sweeper
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
%bcond_without	lang
Name:           sweeper
Version:        20.08.1
Release:        0
Summary:        KDE Privacy Utility
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Helps clean unwanted traces the user leaves on the system.

%lang_package

%prep
%setup -q -n sweeper-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.sweeper Utility Security
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
cp %{_kf5_iconsdir}/breeze/actions/24/trash-empty.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions/
cp %{_kf5_iconsdir}/breeze/apps/48/sweeper.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

%files
%license COPYING.LIB
%doc %lang(en) %{_kf5_htmldir}/en/sweeper/
%{_kf5_applicationsdir}/org.kde.sweeper.desktop
%{_kf5_appstreamdir}/org.kde.sweeper.appdata.xml
%{_kf5_bindir}/sweeper
%{_kf5_iconsdir}/hicolor/scalable/*/*
%{_kf5_kxmlguidir}/sweeper/
%{_kf5_sharedir}/dbus-1/interfaces/*.xml

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
