#
# spec file for package akonadi-notes
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.104.0
%define libname libKPim5AkonadiNotes5
%bcond_without released
Name:           akonadi-notes
Version:        23.04.1
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
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)

%description
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package -n %{libname}
Summary:        Library to implement management of notes in Akonadi
Provides:       %{name} = %{version}
# Renamed
Obsoletes:      akonadi-notes-lang <= 23.04.0

%description  -n %{libname}
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package devel
Summary:        Build environment for akonadi-notes
Requires:       %{libname} = %{version}
Requires:       cmake(KPim5Mime)

%description devel
This package contains the development files needed to use the akonadi-notes
library in other applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n akonadi-notes-%{version}

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSES/*
%{_kf5_libdir}/libKPim5AkonadiNotes.so.*

%files devel
%dir %{_includedir}/KPim5
%{_kf5_cmakedir}/KF5AkonadiNotes/
%{_kf5_cmakedir}/KPim5AkonadiNotes/
%{_includedir}/KPim5/AkonadiNotes/
%{_kf5_libdir}/libKPim5AkonadiNotes.so
%{_kf5_mkspecsdir}/qt_AkonadiNotes.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
