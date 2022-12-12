#
# spec file for package ki18n
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libKF5I18n5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ki18n
Version:        5.101.0
Release:        0
Summary:        KDE Gettext-based UI text internationalization
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE fallbackLang.diff -- look for translations in locale/kf5 also
Patch0:         fallbackLang.diff
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  python3
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package -n %{lname}
Summary:        KDE Gettext-based UI text internationalization
%requires_ge    libQt5Core5
Obsoletes:      libKF5I18n4
Requires:       iso-codes
# The lang package is not optional
Requires:       iso-codes-lang

%description -n %{lname}
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
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       gettext-runtime
Requires:       gettext-tools
Requires:       python3

%description devel
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang ki18n5
for i in `ls %{buildroot}%{_kf5_sharedir}/locale`
do
  if test -d  %{buildroot}%{_kf5_sharedir}/locale/$i/LC_SCRIPTS
  then
    echo "%dir %lang(${i%%_*}) %{_kf5_sharedir}/locale/$i/LC_SCRIPTS" >> ki18n5.lang
    echo "%lang(${i%%_*}) %{_kf5_sharedir}/locale/$i/LC_SCRIPTS/ki18n5/" >> ki18n5.lang
  fi
done

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f ki18n5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/ki18n.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_libdir}/libKF5I18nLocaleData.so.*
%{_kf5_plugindir}/

%files imports
%{_kf5_qmldir}/

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5I18n/
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_libdir}/libKF5I18nLocaleData.so
%{_kf5_mkspecsdir}/qt_KI18n.pri

%changelog
