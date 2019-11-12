#
# spec file for package ktp-auth-handler
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           ktp-auth-handler
Version:        19.08.3
Release:        0
Summary:        Telepathy auth handler
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kaccounts-integration-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  ktp-common-internals-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.3.0
BuildRequires:  pkgconfig(accounts-qt5)
BuildRequires:  pkgconfig(libsignon-qt5)
Requires:       libqca-qt5-plugins
Requires:       signon-plugin-oauth2
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
Telepathy-auth-handler provides UI/KWallet integration for passwords and SSL errors on account connect

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
%{_kf5_libdir}/libexec/
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.*.service
%{_kf5_sharedir}/telepathy/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
