#
# spec file for package kf6-kuserfeedback
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

%define rname kuserfeedback

# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kuserfeedback
Version:        6.3.0
Release:        0
Summary:        Framework for collecting feedback from application users
License:        MIT
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  bison
# # For icons
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  flex
BuildRequires:  fdupes
# # Needed for tests
BuildRequires:  Mesa-dri
BuildRequires:  xvfb-run
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. It is designed to be compliant with the
KDE Telemetry Policy, which forbids the usage of unique identification.

%package -n libKF6UserFeedbackCore6
Summary:        Framework for collecting feedback from application users
Requires:       kf6-kuserfeedback >= %{version}
Recommends:     kf6-kuserfeedback-imports
Recommends:     kf6-kuserfeedback-lang
Recommends:     libKF6UserFeedbackWidgets6

%description -n libKF6UserFeedbackCore6
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. It is designed to be compliant with the
KDE Telemetry Policy, which forbids the usage of unique identification.

%package -n libKF6UserFeedbackWidgets6
Summary:        User interface components for kf6-kuserfeedback
Requires:       kf6-kuserfeedback >= %{version}

%description -n libKF6UserFeedbackWidgets6
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides the user interface
components to integrate the framework in Qt applications.

%package imports
Summary:        QML interface components for kf6-kuserfeedback
Requires:       kf6-kuserfeedback >= %{version}
Requires:       libKF6UserFeedbackCore6 = %{version}
Requires:       libKF6UserFeedbackWidgets6 = %{version}

%description imports
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides the QtQuick components
needed to build QML interfaces leveraging the library.

%package server
Summary:        Server component of kf6-kuserfeedback
Requires:       (php-sqlite or php-mysql or php-pgsql)
Requires:       kf6-kuserfeedback >= %{version}
Requires:       php
Conflicts:      kuserfeedback-server

%description server
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides a server component
used to collect telemetry and feedback.

%package tools
Summary:        Command line utilities for the kuserfeedback server
Requires:       kf6-kuserfeedback >= %{version}
Suggests:       kf6-kuserfeedback-server
Conflicts:      kuserfeedback-tools

%description tools
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides tools to connect to
and query a local or remote KUserFeedback server.

%package devel
Summary:        Development files for kf6-kuserfeedback
Requires:       kf6-kuserfeedback >= %{version}
Requires:       libKF6UserFeedbackCore6 = %{version}
Requires:       libKF6UserFeedbackWidgets6 = %{version}
Conflicts:      kuserfeedback-devel

%description devel
Development files for kf6-kuserfeedback, a framework for collecting feedback from
application users via telemetry and targeted surveys.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# FIXME Docs use a hardcoded path in the application code
# Disable until fixed upstream
%cmake_kf6 -DQT_MAJOR_VERSION:STRING=6 \
  -DENABLE_DOCS:BOOL=FALSE \
  -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-qt --all-name

mkdir -p %{buildroot}%{_kf6_sharedir}/php/
cp -r src/server %{buildroot}%{_kf6_sharedir}/php/kuserfeedback6
# CMakeLists.txt is not needed there and will trigger a rpmlint warning
rm %{buildroot}%{_kf6_sharedir}/php/kuserfeedback6/CMakeLists.txt

install -Dm0644  %{_kf6_iconsdir}/breeze/actions/16/search.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/actions/search.svg
%suse_update_desktop_file -r %{buildroot}%{_kf6_applicationsdir}/org.kde.kuserfeedback-console.desktop Qt KDE Network RemoteAccess

%fdupes %{buildroot}

%check
pushd %__kf6_builddir
xvfb-run -s '-noreset +render' \
  ctest \
  --output-on-failure \
  --force-new-ctest-process \
  --parallel %{_smp_build_ncpus}
popd

%ldconfig_scriptlets -n libKF6UserFeedbackCore6
%ldconfig_scriptlets -n libKF6UserFeedbackWidgets6

%files
%{_kf6_debugdir}/org_kde_UserFeedback.categories

%files -n libKF6UserFeedbackCore6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6UserFeedbackCore.so.*

%files -n libKF6UserFeedbackWidgets6
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so.*

%files imports
%dir %{_kf6_qmldir}/org/kde/userfeedback
%{_kf6_qmldir}/org/kde/userfeedback/

%files tools
%{_kf6_appstreamdir}/org.kde.kuserfeedback-console.appdata.xml
%{_kf6_bindir}/UserFeedbackConsole
%{_kf6_bindir}/userfeedbackctl
%{_kf6_applicationsdir}/org.kde.kuserfeedback-console.desktop
%{_kf6_iconsdir}/hicolor/scalable/actions/search.svg

%files server
%doc composer.json
%doc INSTALL README.md
%dir %{_kf6_sharedir}/php
%{_kf6_sharedir}/php/kuserfeedback6/

%files devel
%dir %{_kf6_includedir}/KUserFeedback
%{_kf6_includedir}/KUserFeedback/kuserfeedback_version.h
%{_kf6_includedir}/KUserFeedbackCore/
%{_kf6_includedir}/KUserFeedbackWidgets/
%{_kf6_cmakedir}/KF6UserFeedback/
%{_kf6_libdir}/libKF6UserFeedbackCore.so
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so
%{_kf6_mkspecsdir}/qt_KF6UserFeedbackCore.pri
%{_kf6_mkspecsdir}/qt_KF6UserFeedbackWidgets.pri

%files lang -f %{name}.lang

%changelog
