#
# spec file for package kaccounts-providers
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
Name:           kaccounts-providers
Version:        20.08.2
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5WebEngineWidgets)
Requires:       signon-plugin-oauth2
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
KDE Accounts Providers.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %make_install -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%files
%license COPYING*
#{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_appstreamdir}/
%{_kf5_plugindir}/kaccounts/
%{_kf5_sharedir}/accounts/
%{_kf5_sharedir}/kpackage/
%{_kf5_sysconfdir}/signon-ui/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
