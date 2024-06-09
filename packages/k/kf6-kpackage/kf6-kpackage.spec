#
# spec file for package kf6-kpackage
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

%define rname kpackage
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kpackage
Version:        6.3.0
Release:        0
Summary:        Non-binary asset user-installable package managing framework
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This framework lets applications to manage user installable packages of
non-binary assets.

%package -n libKF6Package6
Summary:        Non-binary asset user-installable package managing framework
Requires:       kf6-kpackage >= %{version}

%description -n libKF6Package6
This framework lets applications to manage user installable packages of
non-binary assets.

%package devel
Summary:        Non-binary asset user-installable package managing framework
Requires:       libKF6Package6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}

%description devel
This framework lets applications to manage user installable packages of
non-binary assets.

Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libkpackage6 --with-man --all-name

%ldconfig_scriptlets -n libKF6Package6

%files
%doc %lang(en) %{_kf6_mandir}/man1/kpackagetool6.1%{?ext_man}
%{_kf6_bindir}/kpackagetool6
%{_kf6_debugdir}/kpackage.categories
%{_kf6_debugdir}/kpackage.renamecategories

%files -n libKF6Package6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Package.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Package.*
%{_kf6_includedir}/KPackage/
%{_kf6_cmakedir}/KF6Package/
%{_kf6_libdir}/libKF6Package.so

%files lang -f libkpackage6.lang

%changelog
