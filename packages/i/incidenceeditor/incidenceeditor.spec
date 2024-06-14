#
# spec file for package incidenceeditor
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
Name:           incidenceeditor
Version:        24.05.1
Release:        0
Summary:        Incidenceeditor library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KGantt6) >= 3.0.0
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarSupport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6EventViews) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6LdapWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TextEdit) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package contains the incidenceeditor library.

%package -n libKPim6IncidenceEditor6
Summary:        Incidenceeditor Library
License:        LGPL-2.1-or-later
Requires:       incidenceeditor >= %{version}
Obsoletes:      libKPim5IncidenceEditor5 < %{version}
Obsoletes:      incidenceeditor-lang <= 23.04.0
Obsoletes:      libKPim5IncidenceEditor5-lang < %{version}

%description -n libKPim6IncidenceEditor6
The IncidenceEditor library for KDE PIM applications.

%package devel
Summary:        Development package for incidenceeditor
License:        LGPL-2.1-or-later
Requires:       libKPim6IncidenceEditor6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}
Requires:       cmake(KPim6AkonadiMime) >= %{kpim6_version}
Requires:       cmake(KPim6CalendarSupport) >= %{kpim6_version}
Requires:       cmake(KPim6CalendarUtils) >= %{kpim6_version}
Requires:       cmake(KPim6EventViews) >= %{kpim6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
The development package for the incidenceeditor libraries.

%lang_package -n libKPim6IncidenceEditor6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6IncidenceEditor6 --all-name

%ldconfig_scriptlets -n libKPim6IncidenceEditor6

%files
%{_kf6_debugdir}/incidenceeditor.categories
%{_kf6_debugdir}/incidenceeditor.renamecategories

%files -n libKPim6IncidenceEditor6
%license LICENSES/*
%{_libdir}/libKPim6IncidenceEditor.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6IncidenceEditor.*
%{_includedir}/KPim6/IncidenceEditor/
%{_kf6_cmakedir}/KPim6IncidenceEditor/
%{_kf6_libdir}/libKPim6IncidenceEditor.so

%files -n libKPim6IncidenceEditor6-lang -f libKPim6IncidenceEditor6.lang

%changelog
