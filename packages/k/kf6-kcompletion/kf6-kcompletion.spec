#
# spec file for package kf6-kcompletion
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

%define rname kcompletion
# Full KF6 version (e.g. 6.18.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kcompletion
Version:        6.18.0
Release:        0
Summary:        Widgets with advanced completion support
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package -n libKF6Completion6
Summary:        Widgets with advanced completion support
Requires:       kf6-kcompletion >= %{version}

%description -n libKF6Completion6
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package devel
Summary:        Header files for kcompletion, a widget collection with completion support
Requires:       libKF6Completion6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
Development files for KCompletion, a widget collection with advanced
completion support as well as a lower-level completion class which
can be used with own widgets.

%lang_package -n libKF6Completion6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kcompletion6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Completion6

%files
%{_kf6_debugdir}/kcompletion.categories

%files -n libKF6Completion6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Completion.so.*

%files devel
%{_kf6_cmakedir}/KF6Completion/
%{_kf6_includedir}/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_plugindir}/designer/kcompletion6widgets.so

%files -n libKF6Completion6-lang -f kcompletion6.lang

%changelog
