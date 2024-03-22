#
# spec file for package kcharselect
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


%define kf6_version 5.246.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kcharselect
Version:        24.02.1
Release:        0
Summary:        KDE Character Selector
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kcharselect
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kcharselect5 < %{version}
Provides:       kcharselect5 = %{version}

%description
KCharSelect is the KDE character selector tool.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.kcharselect Utility Accessibility

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/*.desktop
%{_kf6_appstreamdir}/org.kde.kcharselect.appdata.xml
%{_kf6_bindir}/kcharselect

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
