#
# spec file for package kdnssd
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


%define rname kio-zeroconf
%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdnssd
Version:        24.05.1
Release:        0
Summary:        Zeroconf Support for KIO applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}

%description
This package adds Zeroconf support to KIO, allowing the use of this protocol
in all applications that are using KIO.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_appstreamdir}/org.kde.kio_zeroconf.metainfo.xml
%{_kf6_dbusinterfacesdir}/org.kde.kdnssd.xml
%{_kf6_plugindir}/kf6/kded/dnssdwatcher.so
%{_kf6_plugindir}/kf6/kio/zeroconf.so
%dir %{_kf6_sharedir}/remoteview/
%{_kf6_sharedir}/remoteview/zeroconf.desktop

%files lang -f %{name}.lang

%changelog
