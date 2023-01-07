#
# spec file for package ktp-desktop-applets
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
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ktp-desktop-applets
Version:        22.12.1
Release:        0
Summary:        Telepathy presence applet
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
Requires:       ktp-common-internals
Provides:       ktp-presence-applet = 0.5.3
Obsoletes:      ktp-presence-applet < 0.5.3
Provides:       ktp-contact-applet = 0.5.3
Obsoletes:      %{name}5 < %{version}
Obsoletes:      ktp-contact-applet < 0.5.3
Provides:       %{name}5 = %{version}

%description
This package provides a Plasma applet to launch your Telepathy contacts list.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes %{buildroot}

%files
%license COPYING*
%{_kf5_plasmadir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/

%files lang -f %{name}.lang

%changelog
