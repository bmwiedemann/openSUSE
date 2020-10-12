#
# spec file for package ki18n
#
# Copyright (c) 2020 SUSE LLC
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
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ki18n
Version:        5.75.0
Release:        0
Summary:        KDE Gettext-based UI text internationalization
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE fallbackLang.diff -- look for translations in locale/kf5 also
Patch0:         fallbackLang.diff
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  kf5-filesystem
BuildRequires:  python3
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package -n %{lname}
Summary:        KDE Gettext-based UI text internationalization
Group:          System/GUI/KDE
%requires_ge    libQt5Core5
Obsoletes:      libKF5I18n4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package devel
Summary:        KDE Gettext-based UI text internationalization
Group:          Development/Libraries/KDE
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
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
for i in `ls %{buildroot}%{_kf5_sharedir}/locale`
do
  if test -d  %{buildroot}%{_kf5_sharedir}/locale/$i/LC_SCRIPTS
  then
    echo "%dir %lang(${i%%_*}) %{_kf5_sharedir}/locale/$i/LC_SCRIPTS" >>%{name}5.lang
    echo "%lang(${i%%_*}) %{_kf5_sharedir}/locale/$i/LC_SCRIPTS/ki18n5/" >>%{name}5.lang
  fi
done
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/ki18n.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_plugindir}/

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5I18n/
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_mkspecsdir}/qt_KI18n.pri

%changelog
