#
# spec file for package kservice
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


%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kservice
Version:        5.74.0
Release:        0
Summary:        Plugin framework for desktop services
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE kservice-desktop-translations.patch
Patch0:         kservice-desktop-translations.patch
# PATCH-FIX-OPENSUSE dont-show-yast-modules-in-the-applications-menu.patch -- hide the YaST modules from the application menu
Patch1:         dont-show-yast-modules-in-the-applications-menu.patch
BuildRequires:  bison
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
Recommends:     kded >= %{_kf5_bugfix_version}
Obsoletes:      libKF5Service4
%if %{with lang}
Recommends:     %{name}-lang = %{version}
%endif

%description
Provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code.

%package devel
Summary:        Plugin framework for desktop services: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Config) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}

%description devel
Provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code. Development files

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
  %cmake_kf5 -d build -- -DAPPLICATIONS_MENU_NAME="kf5-applications.menu"
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%{_kf5_libdir}/libKF5Service.so.*
%{_kf5_bindir}/kbuildsycoca5
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/application.desktop
%{_kf5_servicetypesdir}/kplugininfo.desktop
%dir %{_kf5_sysconfdir}/xdg/menus
%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu
%doc %lang(en) %{_kf5_mandir}/*/kbuildsycoca5.*
%doc %lang(en) %{_kf5_mandir}/*/desktoptojson.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5Service.so
%{_kf5_libdir}/cmake/KF5Service/
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_KService.pri

%changelog
