#
# spec file for package libkeduvocdocument
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
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkeduvocdocument
Version:        22.12.0
Release:        0
Summary:        Library for KDE Education Applications
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

%description
This package contains the library which is required by the KDE education
applications.

%package -n libKEduVocDocument5
Summary:        Library for KDE Education Applications
Recommends:     %{name}-lang
Recommends:     kdeedu-data
Provides:       %{name} = %{version}

%description -n libKEduVocDocument5
This package contains the library which is required by the KDE education
applications.

%package devel
Summary:        Library for KDE Education Applications: Build Environment
Requires:       libKEduVocDocument5 = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop KDE education applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DKDE4_USE_COMMON_CMAKE_PACKAGE_CONFIG_DIR=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes -s %{buildroot}

%post -n libKEduVocDocument5 -p /sbin/ldconfig
%postun -n libKEduVocDocument5 -p /sbin/ldconfig

%files -n libKEduVocDocument5
%license COPYING*
%doc README
%{_kf5_libdir}/libKEduVocDocument.so.*

%files devel
%doc README
%{_kf5_cmakedir}/libkeduvocdocument/
%{_kf5_libdir}/libKEduVocDocument.so
%{_kf5_prefix}/include/libkeduvocdocument/

%files lang -f %{name}.lang

%changelog
