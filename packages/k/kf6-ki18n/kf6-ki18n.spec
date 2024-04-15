#
# spec file for package kf6-ki18n
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

%define rname ki18n
# Full KF6 version (e.g. 6.1.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-ki18n
Version:        6.1.0
Release:        0
Summary:        KDE Gettext-based UI text internationalization
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  python3
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package -n libKF6I18n6
Summary:        KDE Gettext-based UI text internationalization
Requires:       iso-codes
# The lang package is not optional
Requires:       iso-codes-lang
Requires:       kf6-ki18n >= %{version}

%description -n libKF6I18n6
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package imports
Summary:        QML components for ki18n Framework

%description imports
This package contains QML imports for the ki18n framework.

%package devel
Summary:        KDE Gettext-based UI text internationalization
Requires:       gettext-runtime
Requires:       gettext-tools
Requires:       kf6-extra-cmake-modules
Requires:       libKF6I18n6 = %{version}
Requires:       python3
%requires_eq    cmake(Qt6Widgets)

%description devel
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.
Development files.

%lang_package -n libKF6I18n6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang ki18n6
for i in `ls %{buildroot}%{_kf6_sharedir}/locale`
do
  if test -d  %{buildroot}%{_kf6_sharedir}/locale/$i/LC_SCRIPTS
  then
    echo "%dir %lang(${i%%_*}) %{_kf6_sharedir}/locale/$i/LC_SCRIPTS" >> ki18n6.lang
    echo "%lang(${i%%_*}) %{_kf6_sharedir}/locale/$i/LC_SCRIPTS/ki18n6/" >> ki18n6.lang
  fi
done

%ldconfig_scriptlets -n libKF6I18n6

%files
%{_kf6_debugdir}/ki18n.categories
%{_kf6_debugdir}/ki18n.renamecategories
%{_kf6_plugindir}/kf6/ktranscript.so

%files -n libKF6I18n6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6I18n.so.*
%{_kf6_libdir}/libKF6I18nLocaleData.so.*

%files imports
%{_kf6_qmldir}/org/kde/i18n/

%files devel
%doc %{_kf6_qchdir}/KF6I18n.*
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_cmakedir}/KF6I18n/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nLocaleData.so

%files -n libKF6I18n6-lang -f ki18n6.lang

%changelog
