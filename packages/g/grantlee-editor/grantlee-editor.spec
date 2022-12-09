#
# spec file for package grantlee-editor
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


%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           grantlee-editor
Version:        22.12.0
Release:        0
Summary:        Messageviewer header theme editor based on Grantlee
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
#Only required for the icon
BuildRequires:  kaddressbook
BuildRequires:  kmail-application-icons
BuildRequires:  libkleo
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5WebEngine) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
Requires:       kaddressbook
Requires:       kmail-application-icons
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
A theme editor for messageviewer based on Grantlee. Once created or modified,
the themes can be used in KMail.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/contactthemeeditor/
%doc %lang(en) %{_kf5_htmldir}/en/headerthemeeditor/
%{_kf5_applicationsdir}/org.kde.contactprintthemeeditor.desktop
%{_kf5_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kf5_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_kf5_bindir}/contactprintthemeeditor
%{_kf5_bindir}/contactthemeeditor
%{_kf5_bindir}/headerthemeeditor
%{_kf5_configkcfgdir}/grantleethemeeditor.kcfg
%{_kf5_debugdir}/grantleeditor.categories
%{_kf5_debugdir}/grantleeditor.renamecategories
%{_kf5_libdir}/libgrantleethemeeditor.so.*

%files lang -f %{name}.lang

%changelog
