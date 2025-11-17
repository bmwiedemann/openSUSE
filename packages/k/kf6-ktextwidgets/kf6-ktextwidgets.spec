#
# spec file for package kf6-ktextwidgets
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname ktextwidgets
# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-ktextwidgets
Version:        6.20.0
Release:        0
Summary:        KDE Text editing widgets
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package -n libKF6TextWidgets6
Summary:        KDE Text editing widgets

%description -n libKF6TextWidgets6
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package devel
Summary:        KDE Text editing widgets: Build Environment
Requires:       kf6-extra-cmake-modules
Requires:       libKF6TextWidgets6 = %{version}
Requires:       cmake(KF6I18n) >= %{_kf6_version}
Requires:       cmake(KF6Sonnet) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text. Development files.

%lang_package -n libKF6TextWidgets6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang ktextwidgets6

%ldconfig_scriptlets -n libKF6TextWidgets6

%files -n libKF6TextWidgets6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6TextWidgets.so.*

%files devel
%{_kf6_libdir}/libKF6TextWidgets.so
%{_kf6_cmakedir}/KF6TextWidgets/
%{_kf6_includedir}/KTextWidgets/
%{_kf6_plugindir}/designer/ktextwidgets6widgets.so

%files -n libKF6TextWidgets6-lang -f ktextwidgets6.lang

%changelog
