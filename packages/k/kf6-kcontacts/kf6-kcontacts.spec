#
# spec file for package kf6-kcontacts
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

%define qt6_version 6.6.0

%define rname kcontacts
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kcontacts
Version:        6.3.0
Release:        0
Summary:        KDE Frameworks based address book API
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
kcontacts is a Qt library which provides an API
to access address book data stored in different formats.

%package imports
Summary:        QML imports for kcontacts

%description imports
This package provides a QML module that exposes some of the kcontacts classes
as QML value types.

%package -n libKF6Contacts6
Summary:        KDE Frameworks based address book API
Requires:       kf6-kcontacts = %{version}

%description  -n libKF6Contacts6
kcontacts is a Qt library which provides an API
to access address book data stored in different formats.

%package devel
Summary:        Development files for kcontacts
Requires:       libKF6Contacts6 = %{version}
Requires:       cmake(KF6Codecs) >= %{_kf6_version}
Requires:       cmake(KF6Config) >= %{_kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(KF6I18n) >= %{_kf6_version}

%description devel
Development files for kcontacts, a Qt library to access address books.

%lang_package -n libKF6Contacts6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kcontacts6 --with-man --all-name

%ldconfig_scriptlets -n libKF6Contacts6

%files
%{_kf6_debugdir}/kcontacts.categories
%{_kf6_debugdir}/kcontacts.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/contacts/

%files -n libKF6Contacts6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Contacts.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Contacts.*
%{_kf6_cmakedir}/KF6Contacts/
%{_kf6_includedir}/KContacts/
%{_kf6_libdir}/libKF6Contacts.so

%files -n libKF6Contacts6-lang -f kcontacts6.lang

%changelog
