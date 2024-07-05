#
# spec file for package krdc
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           krdc
Version:        24.05.2
Release:        0
Summary:        Remote Desktop Connection
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/krdc
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  LibVNCServer-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf6-breeze-icons
BuildRequires:  libssh-devel
BuildRequires:  cmake(FreeRDP) >= 2.10
BuildRequires:  cmake(FreeRDP-Client) >= 2.10
BuildRequires:  freerdp-server
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(WinPR)
Requires:       kf6-breeze-icons
Requires:       freerdp

%description
Krdc allows to connect to VNC and RDP compatible servers.

%package devel
Summary:        Development files for krdc
Requires:       krdc = %{version}

%description devel
Development libraries and headers needed to build software using krdc

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps
cp %{_kf6_iconsdir}/breeze/apps/48/krdc.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/krdc/
%{_kf6_applicationsdir}/org.kde.krdc.desktop
%{_kf6_appstreamdir}/org.kde.krdc.appdata.xml
%{_kf6_bindir}/krdc
%{_kf6_configkcfgdir}/krdc.kcfg
%{_kf6_iconsdir}/hicolor/scalable/apps/krdc.svg
%{_kf6_libdir}/libkrdccore.so.*
%{_kf6_plugindir}/krdc/
%{_kf6_debugdir}/krdc.categories

%files devel
%{_includedir}/krdc/
%{_includedir}/krdccore_export.h
%{_kf6_libdir}/libkrdccore.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/krdc/

%changelog
