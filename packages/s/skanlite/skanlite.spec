#
# spec file for package skanlite
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
Name:           skanlite
Version:        24.05.1
Release:        0
Summary:        Image Scanner Application
License:        LGPL-2.1-or-later
URL:            https://www.kde.org/applications/graphics/skanlite/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:    kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      %{name}-doc < %{version}

%description
Skanlite is an image scanner application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/skanlite/
%{_kf6_applicationsdir}/org.kde.skanlite.desktop
%{_kf6_appstreamdir}/org.kde.skanlite.appdata.xml
%{_kf6_bindir}/skanlite
%{_kf6_iconsdir}/hicolor/48x48/apps/org.kde.skanlite.svg

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/skanlite/

%changelog
