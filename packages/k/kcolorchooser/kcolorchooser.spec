#
# spec file for package kcolorchooser
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
Name:           kcolorchooser
Version:        22.12.0
Release:        0
Summary:        Color Chooser
License:        MIT
URL:            https://apps.kde.org/kcolorchooser
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  oxygen-icon-theme-large
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)

%description
This is an color chooser application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%suse_update_desktop_file -r org.kde.kcolorchooser Utility DesktopUtility

%files
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kcolorchooser.desktop
%{_kf5_appstreamdir}/org.kde.kcolorchooser.appdata.xml
%{_kf5_bindir}/kcolorchooser
%{_kf5_iconsdir}/hicolor/*/apps/kcolorchooser.png

%files lang -f %{name}.lang

%changelog
