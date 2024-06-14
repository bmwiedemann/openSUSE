#
# spec file for package kdeedu-data
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdeedu-data
Version:        24.05.1
Release:        0
Summary:        Data files for KDE Education Applications
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
# For ecm_query_qt
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
Obsoletes:      libkdeedu4-data < %{version}
Obsoletes:      libkeduvocdocument-data < %{version}
Provides:       libkdeedu4-data = %{version}
Provides:       libkeduvocdocument-data = %{version}
BuildArch:      noarch

%description
This package contains common data files used by various KDE education
applications.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license COPYING
%dir %{_kf6_sharedir}/apps
%{_kf6_iconsdir}/hicolor/*/*/*.*
%{_kf6_sharedir}/apps/kvtml/

%changelog
