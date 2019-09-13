#
# spec file for package knotifyconfig
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


%define lname   libKF5NotifyConfig5
%define _tar_path 5.61
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           knotifyconfig
Version:        5.61.0
Release:        0
Summary:        Configuration dialog for desktop notifications
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
BuildRequires:  kbookmarks-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcompletion-devel >= %{_kf5_bugfix_version}
BuildRequires:  kconfigwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kcoreaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kdbusaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kguiaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  ki18n-devel >= %{_kf5_bugfix_version}
BuildRequires:  kiconthemes-devel >= %{_kf5_bugfix_version}
BuildRequires:  kio-devel >= %{_kf5_bugfix_version}
BuildRequires:  kitemviews-devel >= %{_kf5_bugfix_version}
BuildRequires:  knotifications-devel >= %{_kf5_bugfix_version}
BuildRequires:  kservice-devel >= %{_kf5_bugfix_version}
BuildRequires:  ktextwidgets-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwidgetsaddons-devel >= %{_kf5_bugfix_version}
BuildRequires:  kwindowsystem-devel >= %{_kf5_bugfix_version}
BuildRequires:  kxmlgui-devel >= %{_kf5_bugfix_version}
BuildRequires:  phonon4qt5-devel
BuildRequires:  solid-devel >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5TextToSpeech) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0

%description
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package -n %{lname}
Summary:        Configuration dialog for desktop notifications
Group:          System/GUI/KDE
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package devel
Summary:        Configuration dialog for desktop notifications
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Widgets) >= 5.6.0

%description devel
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application. Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

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
%license COPYING*
%{_kf5_libdir}/libKF5NotifyConfig.so.*

%files devel
%{_kf5_libdir}/libKF5NotifyConfig.so
%{_kf5_libdir}/cmake/KF5NotifyConfig/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KNotifyConfig.pri

%changelog
