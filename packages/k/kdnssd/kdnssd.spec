#
# spec file for package kdnssd
#
# Copyright (c) 2021 SUSE LLC
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


%define rname zeroconf-ioslave
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           kdnssd
Version:        21.04.0
Release:        0
Summary:        Zeroconf Support for KIO applications
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
Recommends:     %{name}-lang

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
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.DOC
%{_kf5_appstreamdir}/org.kde.zeroconf-ioslave.metainfo.xml
%{_kf5_dbusinterfacesdir}/org.kde.kdnssd.xml
%{_kf5_plugindir}/kded_dnssdwatcher.so
%{_kf5_plugindir}/kf5/kio/zeroconf.so
%dir %{_kf5_servicesdir}/kded/
%{_kf5_servicesdir}/kded/dnssdwatcher.desktop
%dir %{_kf5_sharedir}/remoteview/
%{_kf5_sharedir}/remoteview/zeroconf.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
