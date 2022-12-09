#
# spec file for package kruler
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kruler
Version:        22.12.0
Release:        0
Summary:        Screen Ruler
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kruler
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
A screen ruler for the Plasma desktop environment

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kruler Utility DesktopUtility

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kruler/
%{_kf5_applicationsdir}/org.kde.kruler.desktop
%{_kf5_appstreamdir}/org.kde.kruler.appdata.xml
%{_kf5_bindir}/kruler
%{_kf5_iconsdir}/hicolor/*/*/kruler*
%{_kf5_notifydir}/kruler.notifyrc
%{_kf5_sharedir}/kruler/

%files lang -f %{name}.lang

%changelog
