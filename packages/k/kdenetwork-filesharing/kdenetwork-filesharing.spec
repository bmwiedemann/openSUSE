#
# spec file for package kdenetwork-filesharing
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
Name:           kdenetwork-filesharing
Version:        22.12.0
Release:        0
Summary:        KDE Network Libraries
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  PackageKit-Qt5-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Widgets)
Enhances:       dolphin
# The package was named kdenetwork4-filesharing, although being a KF5 plugin
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

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_appstreamdir}/org.kde.kdenetwork-filesharing.metainfo.xml
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/propertiesdialog
%{_kf5_plugindir}/kf5/propertiesdialog/sambausershareplugin.so
%{_kf5_plugindir}/kf5/propertiesdialog/SambaAcl.so
%{_kf5_dbuspolicydir}/org.kde.filesharing.samba.conf
%{_kf5_sharedir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.filesharing.samba.policy
%{_libexecdir}/kauth/authhelper

%files lang -f %{name}.lang

%changelog
