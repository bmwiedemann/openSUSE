#
# spec file for package kf6-kcolorscheme
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

%define rname kcolorscheme
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kcolorscheme
Version:        6.3.0
Release:        0
Summary:        Classes to read and interact with KColorScheme
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Classes to read and interact with KColorScheme.

%package -n libKF6ColorScheme6
Summary:        Classes to read and interact with KColorScheme
Requires:       kf6-kcolorscheme >= %{version}

%description -n libKF6ColorScheme6
Classes to read and interact with KColorScheme.

%package devel
Summary:        Classes to read and interact with KColorScheme: Build Environment
Requires:       libKF6ColorScheme6 = %{version}
Requires:       cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6I18n) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
Classes to read and interact with KColorScheme. Development files.

%lang_package -n libKF6ColorScheme6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kcolorscheme6 --with-man --all-name

%ldconfig_scriptlets -n libKF6ColorScheme6

%files
%{_kf6_debugdir}/kcolorscheme.categories

%files -n libKF6ColorScheme6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ColorScheme.so.*

%files devel
%doc %{_kf6_qchdir}/KF6ColorScheme.*
%{_kf6_cmakedir}/KF6ColorScheme/
%{_kf6_includedir}/KColorScheme/
%{_kf6_libdir}/libKF6ColorScheme.so

%files -n libKF6ColorScheme6-lang -f kcolorscheme6.lang

%changelog
