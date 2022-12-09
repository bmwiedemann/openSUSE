#
# spec file for package mbox-importer
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


# Latest stable Applications (e.g. 16.08 in KA, but 16.11.90 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           mbox-importer
Version:        22.12.0
Release:        0
Summary:        Tool for importing mbox archives into akonadi
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5MailImporter)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package contains a tool that can be used to import mbox archives
into akonadi.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%files
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.mboximporter.desktop
%{_kf5_bindir}/mboximporter

%files lang -f %{name}.lang

%changelog
