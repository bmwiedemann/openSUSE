#
# spec file for package akonadi-notes
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


%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           akonadi-notes
Version:        22.12.1
Release:        0
Summary:        Library to implement management of notes in Akonadi
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

%description
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package -n libKF5AkonadiNotes5
Summary:        Library to implement management of notes in Akonadi
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5AkonadiNotes5
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package devel
Summary:        Build environment for akonadi-notes
Requires:       libKF5AkonadiNotes5 = %{version}
Requires:       cmake(KF5Mime)

%description devel
This package contains the development files needed to use the akonadi-notes
library in other applications.

%lang_package

%prep
%autosetup -p1 -n akonadi-notes-%{version}

%build
%cmake_kf5 -d build -- -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5AkonadiNotes5 -p /sbin/ldconfig
%postun -n libKF5AkonadiNotes5 -p /sbin/ldconfig

%files -n libKF5AkonadiNotes5
%license LICENSES/*
%{_kf5_libdir}/libKF5AkonadiNotes.so.*

%files devel
%{_kf5_cmakedir}/KF5AkonadiNotes/
%{_kf5_includedir}/AkonadiNotes/
%{_kf5_libdir}/libKF5AkonadiNotes.so
%{_kf5_mkspecsdir}/qt_AkonadiNotes.pri

%files lang -f %{name}.lang

%changelog
