#
# spec file for package kf6-kdesu
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

%define rname kdesu
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kdesu
Version:        6.3.0
Release:        0
Summary:        User interface for running shell commands with root privileges
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Pty) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package -n libKF6Su6
Summary:        User interface for running shell commands with root privileges
Requires:       kf6-kdesu >= %{version}

%description -n libKF6Su6
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package devel
Summary:        User interface for running shell commands with root privileges
Requires:       libKF6Su6 = %{version}
Requires:       cmake(KF6Pty) >= %{_kf6_bugfix_version}

%description devel
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.
Development files.

%lang_package -n libKF6Su6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kdesud6

%ldconfig_scriptlets -n libKF6Su6

%files -n libKF6Su6-lang -f kdesud6.lang

%files
%{_kf6_debugdir}/ksu.categories
%{_kf6_libexecdir}/kdesu_stub
%{_kf6_libexecdir}/kdesud

%files -n libKF6Su6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Su.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Su.*
%{_kf6_cmakedir}/KF6Su/
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so

%changelog
