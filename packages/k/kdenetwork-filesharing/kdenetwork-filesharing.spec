#
# spec file for package kdenetwork-filesharing
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
Name:           kdenetwork-filesharing
Version:        24.05.2
Release:        0
Summary:        KDE Network Libraries
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
Recommends:     samba-client
Enhances:       dolphin
# The package used to named kdenetwork4-filesharing
Provides:       kdenetwork4-filesharing = %{version}
Obsoletes:      kdenetwork4-filesharing < %{version}
Obsoletes:      kdenetwork4-filesharing-lang < %{version}

%description
Network File Sharing configuration module and plugin.
Used for configuring Samba shares.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.kdenetwork-filesharing.metainfo.xml
%{_kf6_dbuspolicydir}/org.kde.filesharing.samba.conf
%{_kf6_libexecdir}/kauth/authhelper
%dir %{_kf6_plugindir}/kf6/propertiesdialog
%{_kf6_plugindir}/kf6/propertiesdialog/SambaAcl.so
%{_kf6_plugindir}/kf6/propertiesdialog/sambausershareplugin.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.filesharing.samba.policy

%files lang -f %{name}.lang

%changelog
