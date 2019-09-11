#
# spec file for package kdepim-apps-libs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-apps-libs
Version:        19.08.0
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-contact-devel >= %{_kapp_version}
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee5-devel
BuildRequires:  grantleetheme-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libkleo-devel
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  prison-qt5-devel
BuildRequires:  pkgconfig(Qt5DBus) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package contains mail related libraries

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary:        Mail related libraries
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       akonadi-server-devel
Requires:       grantlee5-devel

%description devel
The development package for the kdepim-apps-libs libraries

%files devel
%license COPYING*
%{_kf5_includedir}/
%{_kf5_cmakedir}/KF5KaddressbookImportExport/
%{_kf5_libdir}/cmake/KF5FollowupReminder/
%{_kf5_libdir}/cmake/KF5KaddressbookGrantlee/
%{_kf5_libdir}/cmake/KF5KdepimDBusInterfaces/
%{_kf5_libdir}/cmake/KF5SendLater/
%{_kf5_libdir}/libKF5FollowupReminder.so
%{_kf5_libdir}/libKF5KaddressbookGrantlee.so
%{_kf5_libdir}/libKF5KaddressbookImportExport.so
%{_kf5_libdir}/libKF5KdepimDBusInterfaces.so
%{_kf5_libdir}/libKF5SendLater.so
%{_kf5_mkspecsdir}/qt_FollowupReminder.pri
%{_kf5_mkspecsdir}/qt_KaddressbookGrantlee.pri
%{_kf5_mkspecsdir}/qt_KaddressbookImportExport.pri
%{_kf5_mkspecsdir}/qt_KdepimDBusInterfaces.pri
%{_kf5_mkspecsdir}/qt_SendLater.pri

%files
%license COPYING*
%{_kf5_debugdir}/kdepim-apps-lib.categories
%{_kf5_debugdir}/kdepim-apps-lib.renamecategories
%{_kf5_libdir}/libKF5FollowupReminder.so.*
%{_kf5_libdir}/libKF5KaddressbookGrantlee.so.*
%{_kf5_libdir}/libKF5KaddressbookImportExport.so.*
%{_kf5_libdir}/libKF5KdepimDBusInterfaces.so.*
%{_kf5_libdir}/libKF5SendLater.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
