#
# spec file for package kdeedu-data
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
Name:           kdeedu-data
Version:        20.08.2
Release:        0
Summary:        Data files for KDE Education Applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  xz
Obsoletes:      libkdeedu4-data < %{version}
Obsoletes:      libkeduvocdocument-data < %{version}
Provides:       libkdeedu4-data = %{version}
Provides:       libkeduvocdocument-data = %{version}
BuildArch:      noarch
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains common data files used by various
KDE education applications.

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes -s %{buildroot}

%files
%license COPYING
%dir %{_kf5_sharedir}/apps
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_sharedir}/apps/kvtml/

%changelog
