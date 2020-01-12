#
# spec file for package ktp-contact-list
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktp-contact-list
Version:        19.12.1
Release:        0
Summary:        Telepathy contact list
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  fdupes
BuildRequires:  kcmutils-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kpeople5-devel
BuildRequires:  ktp-common-internals-devel
BuildRequires:  ktp-icons
BuildRequires:  kwallet-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
Telepathy contact list application

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

  %fdupes %{buildroot}

%files
%license COPYING*
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/ktp-contactlist
%{_kf5_sharedir}/dbus-1/services/org.kde.ktpcontactlist.service

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
