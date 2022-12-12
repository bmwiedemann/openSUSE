#
# spec file for package kcontacts
#
# Copyright (c) 2021 SUSE LLC
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kcontacts
Version:        5.101.0
Release:        0
Summary:        KDE Frameworks based address book API
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{_kf5_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)

%description
kcontacts is a Qt5 based library which provides an API
to access address book data stored in different formats.

%package -n libKF5Contacts5
Summary:        KDE Frameworks based address book API
Provides:       %{name} = %{version}
# package existed in KDE:Unstable:Applications for a short while
Provides:       %{name}-data = %{version}
Obsoletes:      %{name}-data < %{version}
Recommends:     %{name}-lang

%description  -n libKF5Contacts5
kcontacts is a Qt5 based library which provides an API
to access address book data stored in different formats.

%package devel
Summary:        Development files for kcontacts
Requires:       libKF5Contacts5 = %{version}
Requires:       cmake(KF5Codecs) >= %{_kf5_version}
Requires:       cmake(KF5Config) >= %{_kf5_version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_version}
Requires:       cmake(KF5I18n) >= %{_kf5_version}
Provides:       kcontacts5-devel = %{version}
Obsoletes:      kcontacts5-devel < %{version}

%description devel
Development files for kcontacts, a Qt5 library to access
address books.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5Contacts5 -p /sbin/ldconfig
%postun -n libKF5Contacts5 -p /sbin/ldconfig

%files -n libKF5Contacts5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Contacts.so.*

%files devel
%{_kf5_cmakedir}/KF5Contacts/
%{_kf5_includedir}/KContacts/
%{_kf5_libdir}/libKF5Contacts.so
%{_kf5_mkspecsdir}/qt_KContacts.pri

%files lang -f %{name}.lang

%changelog
