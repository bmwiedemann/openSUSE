#
# spec file for package kruler
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
%define qt6_version 6.6.0

%bcond_without released
Name:           kruler
Version:        24.05.1
Release:        0
Summary:        Screen Ruler
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kruler
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kruler5 < %{version}
Provides:       kruler5 = %{version}

%description
A screen ruler for the Plasma desktop environment

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file -r org.kde.kruler Utility DesktopUtility

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kruler/
%{_kf6_applicationsdir}/org.kde.kruler.desktop
%{_kf6_appstreamdir}/org.kde.kruler.appdata.xml
%{_kf6_bindir}/kruler
%{_kf6_iconsdir}/hicolor/*/*/kruler*
%{_kf6_notificationsdir}/kruler.notifyrc
%{_kf6_sharedir}/kruler/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kruler/

%changelog
