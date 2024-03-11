#
# spec file for package kdiagram6
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


%define kf6_version 5.246.0
%define qt6_version 6.6.0

%define rname kdiagram
%bcond_without released
Name:           kdiagram6
Version:        3.0.1
Release:        0
Summary:        Libraries (KChart, KGantt) for creating diagrams
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:         kdiagram.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Libraries (KChart, KGantt) for creating diagrams

%package -n libKChart6-3
Summary:        KChart library for kdiagram

%description -n libKChart6-3
This package contains the KChart libraries from the kdiagram package.

%package -n libKGantt6-3
Summary:        Gantt chart implementation for kdiagram

%description -n libKGantt6-3
This package contains the KGantt libraries from the kdiagram package.

%package devel
Summary:        Development package for the KDiagram libraries
Requires:       libKChart6-3 = %{version}
Requires:       libKGantt6-3 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6PrintSupport) >= %{qt6_version}
Requires:       cmake(Qt6Svg) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
Development package for the KDiagram libraries

%lang_package -n libKGantt6-3
%lang_package -n libKChart6-3

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kgantt6 --with-qt --without-mo
%find_lang kchart6 --with-qt --without-mo

%ldconfig_scriptlets -n libKChart6-3
%ldconfig_scriptlets -n libKGantt6-3

%files -n libKChart6-3
%license LICENSES/*
%{_libdir}/libKChart6.so.*

%files -n libKGantt6-3
%license LICENSES/*
%{_libdir}/libKGantt6.so.*

%files devel
%doc %{_kf6_qchdir}/KChart6.*
%doc %{_kf6_qchdir}/KGantt6.*
%{_includedir}/KChart6/
%{_includedir}/KGantt6/
%{_kf6_cmakedir}/KChart6/
%{_kf6_cmakedir}/KGantt6/
%{_kf6_libdir}/libKChart6.so
%{_kf6_libdir}/libKGantt6.so
%{_kf6_mkspecsdir}/qt_KChart6.pri
%{_kf6_mkspecsdir}/qt_KGantt6.pri

%files -n libKChart6-3-lang -f kchart6.lang

%files -n libKGantt6-3-lang -f kgantt6.lang

%changelog
