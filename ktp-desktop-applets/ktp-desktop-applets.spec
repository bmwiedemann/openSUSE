#
# spec file for package ktp-desktop-applets
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
Name:           ktp-desktop-applets
Version:        19.08.0
Release:        0
Summary:        Telepathy presence applet
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  kwindowsystem-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma-framework-devel
BuildRequires:  cmake(KF5I18n)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
Requires:       ktp-common-internals
Provides:       ktp-presence-applet = 0.5.3
Obsoletes:      ktp-presence-applet < 0.5.3
Provides:       ktp-contact-applet = 0.5.3
Obsoletes:      %{name}5 < %{version}
Obsoletes:      ktp-contact-applet < 0.5.3
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
This package provides a Plasma applet to launch your Telepathy contacts list.

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
%{_kf5_plasmadir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
