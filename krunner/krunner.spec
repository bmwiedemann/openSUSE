#
# spec file for package krunner
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


%define lname   libKF5Runner5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           krunner
Version:        5.61.0
Release:        0
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kconfig-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  plasma-framework-devel >= %{_kf5_bugfix_version}
BuildRequires:  solid-devel >= %{_kf5_bugfix_version}
BuildRequires:  threadweaver-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Gui) >= 5.6.0
BuildRequires:  cmake(Qt5Quick) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0

%description
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package -n %{lname}
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          System/GUI/KDE

%description -n %{lname}
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package devel
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       plasma-framework-devel >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Core) >= 5.6.0
Conflicts:      kapptemplate <= 16.03.80

%description devel
Framework Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly. Development files

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
# no license yet
#doc COPYING* README*
%{_kf5_libdir}/libKF5Runner.so.*
%{_kf5_qmldir}/
%{_kf5_servicetypesdir}/plasma-runner.desktop
%{_kf5_debugdir}/*.categories

%files devel
#doc COPYING* README*
%{_kf5_libdir}/libKF5Runner.so
%{_kf5_libdir}/cmake/KF5Runner/
%dir %{_kf5_includedir}/KRunner/
%{_kf5_includedir}/KRunner/
%{_kf5_includedir}/*.h
%{_kf5_mkspecsdir}/qt_KRunner.pri
%{_kf5_sharedir}/kdevappwizard
%{_kf5_dbusinterfacesdir}/kf5_org.kde.krunner1.xml

%changelog
