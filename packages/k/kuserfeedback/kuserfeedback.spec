#
# spec file for package kuserfeedback
#
# Copyright (c) 2022 SUSE LLC
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


%define soversion 1
%bcond_without released
Name:           kuserfeedback
Version:        1.2.0
Release:        0
Summary:        Framework for collecting feedback from application users
License:        MIT
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kuserfeedback.keyring
%endif
BuildRequires:  bison
# For icons
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules >= 5.44.0
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf5-filesystem
# Needed instead of cmake(...) to build on Leap
BuildRequires:  libqt5-qttools-doc
# Needed for tests
BuildRequires:  Mesa-dri
BuildRequires:  update-desktop-files
BuildRequires:  xvfb-run
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Core) >= 5.4
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Network) >= 5.4
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. It is designed to be compliant with the
KDE Telemetry Policy, which forbids the usage of unique identification.

%package -n libKUserFeedbackCore%{soversion}
Summary:        Framework for collecting feedback from application users
Group:          System/Libraries
Recommends:     %{name}-imports
Recommends:     %{name}-lang
Recommends:     libKUserFeedbackWidgets%{soversion}
Provides:       %{name} = %{version}

%description -n libKUserFeedbackCore%{soversion}
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. It is designed to be compliant with the
KDE Telemetry Policy, which forbids the usage of unique identification.

%package -n libKUserFeedbackWidgets%{soversion}
Summary:        User interface components for kuserfeedback
Group:          System/Libraries

%description -n libKUserFeedbackWidgets%{soversion}
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides the user interface
components to integrate the framework in Qt applications.

%package imports
Summary:        QML interface components for kuserfeedback
Group:          System/Libraries
Requires:       libKUserFeedbackCore%{soversion} = %{version}
Requires:       libKUserFeedbackWidgets%{soversion} = %{version}

%description imports
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides the QtQuick components
needed to build QML interfaces leveraging the library.

%package server
Summary:        Server component of kuserfeedback
Group:          Productivity/Networking/Web/Servers
Requires:       php
Requires:       (php-sqlite or php-mysql or php-pgsql)

%description server
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides a server component
used to collect telemetry and feedback.

%package tools
Summary:        Command line utilities for the kuserfeedback server
Group:          Productivity/Networking/Web/Utilities
Suggests:       kuserfeedback-server

%description tools
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides tools to connect to
and query a local or remote KUserFeedback server.

%package devel
Summary:        Development files for kuserfeedback
Group:          Development/Libraries/KDE
Requires:       libKUserFeedbackCore%{soversion} = %{version}
Requires:       libKUserFeedbackWidgets%{soversion} = %{version}

%description devel
Development files for kuserfeedback, a framework for collecting feedback from
application users via telemetry and targeted surveys.

%lang_package

%prep
%setup -q

%build
  # Docs use a hardcoded path in the application code
  # Disable until fixed upstream
  %cmake_kf5 -d build -- -DENABLE_DOCS=OFF -DBUILD_TESTING=ON -DQT_MAJOR_VERSION=5
  %cmake_build

%install
  %kf5_makeinstall -C build
  mkdir -p %{buildroot}%{_kf5_sharedir}/php/
  cp -r src/server %{buildroot}%{_kf5_sharedir}/php/%{name}
  # CMakeLists.txt is not needed there and will trigger a rpmlint warning
  rm -f %{buildroot}%{_kf5_sharedir}/php/%{name}/CMakeLists.txt

  %if %{with released}
    %find_lang %{name} --with-man --with-qt --all-name
  %endif

  install -Dm0644  %{_kf5_iconsdir}/breeze/actions/16/search.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions/search.svg
  %suse_update_desktop_file -r %{buildroot}%{_kf5_applicationsdir}/org.kde.kuserfeedback-console.desktop Qt KDE Network RemoteAccess

  %fdupes %{buildroot}

%check

export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -s '-noreset +render' -a %cmake_build -C build test

%post -n libKUserFeedbackCore%{soversion} -p /sbin/ldconfig
%post -n libKUserFeedbackWidgets%{soversion} -p /sbin/ldconfig
%postun -n libKUserFeedbackCore%{soversion} -p /sbin/ldconfig
%postun -n libKUserFeedbackWidgets%{soversion} -p /sbin/ldconfig

%files -n libKUserFeedbackCore%{soversion}
%license COPYING.LIB
%{_kf5_libdir}/libKUserFeedbackCore.so.%{soversion}
%{_kf5_libdir}/libKUserFeedbackCore.so.%{soversion}.*
%{_kf5_debugdir}/org_kde_UserFeedback.categories

%files -n libKUserFeedbackWidgets%{soversion}
%license COPYING.LIB
%{_kf5_libdir}/libKUserFeedbackWidgets.so.%{soversion}
%{_kf5_libdir}/libKUserFeedbackWidgets.so.%{soversion}.*

%files imports
%license COPYING.LIB
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%dir %{_kf5_qmldir}/org/kde/userfeedback
%{_kf5_qmldir}/org/kde/userfeedback/qmldir
%{_kf5_qmldir}/org/kde/userfeedback/libKUserFeedbackQml.so

%files tools
%license COPYING.LIB
%{_kf5_bindir}/UserFeedbackConsole
%{_kf5_bindir}/userfeedbackctl
%{_kf5_applicationsdir}/org.kde.kuserfeedback-console.desktop
%{_kf5_appstreamdir}/org.kde.kuserfeedback-console.appdata.xml
%{_kf5_iconsdir}/hicolor/scalable/actions/search.svg

%files server
%license COPYING.LIB
%doc composer.json
%doc INSTALL README.md
%dir %{_kf5_sharedir}/php
%{_kf5_sharedir}/php/%{name}/

%files devel
%license COPYING.LIB
%dir %{_includedir}/KUserFeedback
%{_includedir}/KUserFeedback
%{_kf5_cmakedir}/KUserFeedback
%{_kf5_libdir}/libKUserFeedbackCore.so
%{_kf5_libdir}/libKUserFeedbackWidgets.so
%{_kf5_mkspecsdir}/qt_KUserFeedbackCore.pri
%{_kf5_mkspecsdir}/qt_KUserFeedbackWidgets.pri

%if %{with released}
%files lang -f %{name}.lang
%license COPYING.LIB
%endif

%changelog
