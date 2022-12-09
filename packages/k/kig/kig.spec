#
# spec file for package kig
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
Name:           kig
Version:        22.12.0
Release:        0
Summary:        Interactive Geometry
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kig
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_python3-devel
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5XmlPatterns)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Kig is an application for Interactive Geometry. It's intended to serve
two purposes: Allow students to interactively explore mathematical
figures and concepts using the computer. Serve as a WYSIWYG tool for
drawing mathematical figures and including them in other documents.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBoost_NO_BOOST_CMAKE=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_applicationsdir}/org.kde.kig.desktop
%{_kf5_appstreamdir}/org.kde.kig.appdata.xml
%{_kf5_bindir}/kig
%{_kf5_bindir}/pykig.py
%{_kf5_iconsdir}/hicolor/*/*/*kig.*
%{_kf5_mandir}/man?/*
%{_kf5_plugindir}/kf5/parts/kigpart.so
%{_kf5_servicesdir}/kig_part.desktop
%{_kf5_sharedir}/katepart5/
%{_kf5_sharedir}/kig/
%{_kf5_sharedir}/kxmlgui5/

%files lang -f %{name}.lang

%changelog
