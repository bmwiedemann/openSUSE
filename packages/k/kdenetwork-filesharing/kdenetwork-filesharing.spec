#
# spec file for package kdenetwork-filesharing
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdenetwork-filesharing
Version:        20.08.2
Release:        0
Summary:        KDE Network Libraries
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  PackageKit-Qt5-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
Enhances:       dolphin
# The package was named kdenetwork4-filesharing, although being a KF5 plugin
Provides:       kdenetwork4-filesharing = %{version}
Obsoletes:      kdenetwork4-filesharing < %{version}
Obsoletes:      kdenetwork4-filesharing-lang < %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Network File Sharing configuration module and plugin.
Used for configuring Samba shares.

%lang_package

%prep
%setup -q

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
%{_kf5_appstreamdir}/org.kde.kdenetwork-filesharing.metainfo.xml
%{_kf5_plugindir}/sambausershareplugin.so
%{_kf5_servicesdir}/sambausershareplugin.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
