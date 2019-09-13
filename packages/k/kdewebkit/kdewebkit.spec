#
# spec file for package kdewebkit
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


%define lname   libKF5WebKit5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           kdewebkit
Version:        5.61.0
Release:        0
Summary:        Integration of the HTML rendering engine WebKit
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kbookmarks-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcompletion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdbusaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdesignerplugin-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kguiaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  kitemviews-devel >= %{_kf5_bugfix_version}
BuildRequires:  knotifications-devel >= %{_kf5_bugfix_version}
BuildRequires:  kparts-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  ktextwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwallet-framework-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  kxmlgui-devel >= %{_kf5_bugfix_version}
BuildRequires:  solid-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5Designer) >= 5.6.0
BuildRequires:  cmake(Qt5Network) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5WebKitWidgets) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5Xml) >= 5.6.0

%description
This library provides KDE integration of the QtWebKit library. If you are
using QtWebKit in your KDE application, you are encouraged to use this layer
instead of using the QtWebKit classes directly.

%package -n %{lname}
Summary:        Integration of the HTML rendering engine WebKit
Group:          System/GUI/KDE

%description -n %{lname}
This library provides KDE integration of the QtWebKit library. If you are
using QtWebKit in your KDE application, you are encouraged to use this layer
instead of using the QtWebKit classes directly.

%package devel
Summary:        Integration of the HTML rendering engine WebKit
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5WebKitWidgets) >= 5.6.0

%description devel
This library provides KDE integration of the QtWebKit library. If you are
using QtWebKit in your KDE application, you are encouraged to use this layer
instead of using the QtWebKit classes directly. Development files.

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
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5WebKit.so.*

%files devel
%{_kf5_libdir}/libKF5WebKit.so
%{_kf5_libdir}/cmake/KF5WebKit/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KDEWebKit.pri
%dir %{_kf5_plugindir}/designer/
%{_kf5_plugindir}/designer/kdewebkit5widgets.so

%changelog
