#
# spec file for package kig
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0

%bcond_without released
Name:           kig
Version:        25.12.0
Release:        0
Summary:        Interactive Geometry
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kig
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_python3-devel
BuildRequires:  python3-devel
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.kig.desktop
%{_kf6_appstreamdir}/org.kde.kig.metainfo.xml
%{_kf6_bindir}/kig
%{_kf6_bindir}/pykig.py
%{_kf6_plugindir}/kf6/parts/kigpart.so
%{_kf6_iconsdir}/hicolor/*/*/*kig.*
%{_kf6_mandir}/man1/kig.1%{?ext_man}
%dir %{_kf6_sharedir}/katepart5
%dir %{_kf6_sharedir}/katepart5/syntax
%{_kf6_sharedir}/katepart5/syntax/python-kig.xml
%{_kf6_sharedir}/kig/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
