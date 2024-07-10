#
# spec file for package grantlee-editor
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           grantlee-editor
Version:        24.05.2
Release:        0
Summary:        Messageviewer header theme editor based on Grantlee
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
#Only required for the icon
BuildRequires:  kaddressbook
BuildRequires:  kmail-application-icons
BuildRequires:  libkleo
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kaddressbook
Requires:       kmail-application-icons
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
A theme editor for messageviewer based on Grantlee. Once created or modified,
the themes can be used in KMail.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/contactthemeeditor/
%doc %lang(en) %{_kf6_htmldir}/en/headerthemeeditor/
%{_kf6_applicationsdir}/org.kde.contactprintthemeeditor.desktop
%{_kf6_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kf6_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_kf6_bindir}/contactprintthemeeditor
%{_kf6_bindir}/contactthemeeditor
%{_kf6_bindir}/headerthemeeditor
%{_kf6_configkcfgdir}/grantleethemeeditor.kcfg
%{_kf6_debugdir}/grantleeditor.categories
%{_kf6_debugdir}/grantleeditor.renamecategories
%{_kf6_libdir}/libgrantleethemeeditor.so.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/contactthemeeditor/
%exclude %{_kf6_htmldir}/en/headerthemeeditor/

%changelog
