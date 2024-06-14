#
# spec file for package sweeper
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


%define kf6_version 6.0.0
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           sweeper
Version:        24.05.1
Release:        0
Summary:        KDE Privacy Utility
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/sweeper
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Helps clean unwanted traces the user leaves on the system.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.sweeper Utility Security

mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/
cp %{_kf6_iconsdir}/breeze/apps/48/sweeper.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/sweeper/
%{_kf6_applicationsdir}/org.kde.sweeper.desktop
%{_kf6_appstreamdir}/org.kde.sweeper.appdata.xml
%{_kf6_bindir}/sweeper
%{_kf6_debugdir}/sweeper.categories
%{_kf6_iconsdir}/hicolor/scalable/*/*
%{_kf6_dbusinterfacesdir}/org.kde.sweeper.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/sweeper/

%changelog
