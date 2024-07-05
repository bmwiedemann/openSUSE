#
# spec file for package pim-sieve-editor
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
Name:           pim-sieve-editor
Version:        24.05.2
Release:        0
Summary:        Sieve scripts editor for KDE PIM applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://apps.kde.org/sieveeditor
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Is only required for the desktop file icon
BuildRequires:  kmail-application-icons
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KSieveUi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.14.2
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kmail
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package provides an editor, complete with syntax highlighting and
command completion, to edit Sieve scripts ("server side filtering")
in KDE PIM applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.sieveeditor Network Email

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/sieveeditor/
%{_kf6_applicationsdir}/org.kde.sieveeditor.desktop
%{_kf6_appstreamdir}/org.kde.sieveeditor.appdata.xml
%{_kf6_bindir}/sieveeditor
%{_kf6_configkcfgdir}/sieveeditorglobalconfig.kcfg
%{_kf6_debugdir}/sieveeditor.categories
%{_kf6_debugdir}/sieveeditor.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/sieveeditor.*
%{_kf6_libdir}/libsieveeditor.so.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/sieveeditor/

%changelog
