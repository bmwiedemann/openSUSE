#
# spec file for package kcmutils
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


%define lname   libKF5KCMUtils5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kcmutils
Version:        5.74.0
Release:        0
Summary:        Classes to work with KCModules
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Declarative) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Package) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Quick) >= 5.12.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package -n %{lname}
Summary:        Classes to work with KCModules
Group:          System/GUI/KDE
Obsoletes:      libKF5KCMUtils4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package devel
Summary:        Build environment for kcmutils, a set of classes to work with KCModules
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}

%description devel
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework. Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5KCMUtils.so.*
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kcmodule.desktop
%{_kf5_servicetypesdir}/kcmoduleinit.desktop
%{_kf5_debugdir}/kcmutils.categories

%files devel
%{_kf5_libdir}/libKF5KCMUtils.so
%{_kf5_libdir}/cmake/KF5KCMUtils/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KCMUtils.pri

%changelog
