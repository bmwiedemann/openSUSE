#
# spec file for package umbrello
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.27.0
%define qt6_version 6.9.0
#
%bcond_without released
Name:           umbrello
Version:        26.08.0
Release:        0
Summary:        UML Modeller
License:        GFDL-1.2-only AND GPL-2.0-only AND GPL-3.0-or-later
URL:            https://apps.kde.org/umbrello
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
Obsoletes:      umbrello5 < %{version}
Provides:       umbrello5 = %{version}

%description
Umbrello is a UML modelling application.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DBUILD_PHP_IMPORT:BOOL=FALSE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/umbrello
%{_kf6_applicationsdir}/org.kde.umbrello.desktop
%{_kf6_appstreamdir}/org.kde.umbrello.appdata.xml
%{_kf6_bindir}/po2xmi6
%{_kf6_bindir}/umbrello6
%{_kf6_bindir}/xmi2pot6
%{_kf6_iconsdir}/hicolor/*/*/umbrello*
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-uml.png
%{_kf6_sharedir}/umbrello6/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/umbrello

%changelog
