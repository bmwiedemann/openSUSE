#
# spec file for package akonadi-notes
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           akonadi-notes
Version:        24.05.1
Release:        0
Summary:        Library to implement management of notes in Akonadi
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package -n libKPim6AkonadiNotes6
Summary:        Library to implement management of notes in Akonadi
Provides:       akonadi-notes >= %{version}
Obsoletes:      akonadi-notes-lang <= 23.04.0
Obsoletes:      libKF5AkonadiNotes5 < %{version}
Obsoletes:      libKPim5AkonadiNotes5 < %{version}
Obsoletes:      libKPim5AkonadiNotes5-lang < %{version}

%description  -n libKPim6AkonadiNotes6
Akonadi Notes is a library that bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package devel
Summary:        Build environment for akonadi-notes
Requires:       libKPim6AkonadiNotes6 = %{version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
This package contains the development files needed to use the akonadi-notes
library in other applications.

%lang_package -n libKPim6AkonadiNotes6

%prep
%autosetup -p1 -n akonadi-notes-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6AkonadiNotes6

%files -n libKPim6AkonadiNotes6
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiNotes.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6AkonadiNotes.*
%{_kf6_cmakedir}/KPim6AkonadiNotes/
%{_includedir}/KPim6/AkonadiNotes/
%{_kf6_libdir}/libKPim6AkonadiNotes.so

%files -n libKPim6AkonadiNotes6-lang -f %{name}.lang

%changelog
