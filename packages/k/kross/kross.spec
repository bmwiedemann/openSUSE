#
# spec file for package kross
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
Name:           kross
Version:        5.74.0
Release:        0
Summary:        Scripting bridge for programs
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_tar_path}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Completion) >= %{_tar_path}
BuildRequires:  cmake(KF5DocTools) >= %{_tar_path}
BuildRequires:  cmake(KF5I18n) >= %{_tar_path}
BuildRequires:  cmake(KF5IconThemes) >= %{_tar_path}
BuildRequires:  cmake(KF5KIO) >= %{_tar_path}
BuildRequires:  cmake(KF5Parts) >= %{_tar_path}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_tar_path}
BuildRequires:  cmake(KF5XmlGui) >= %{_tar_path}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Script) >= 5.12.0
BuildRequires:  cmake(Qt5UiTools) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
Obsoletes:      libKF5KrossCore4
Obsoletes:      libKF5KrossUi4
%if %{with lang}
Recommends:     %{name}-lang = %{version}
%endif

%description
Kross is a scripting bridge to embed scripting functionality
into an application. It supports QtScript as a scripting interpreter backend.

%package devel
Summary:        Development files for the Kross scripting bridge
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5I18n) >= %{_tar_path}
Requires:       cmake(KF5IconThemes) >= %{_tar_path}
Requires:       cmake(KF5KIO) >= %{_tar_path}
Requires:       cmake(KF5Parts) >= %{_tar_path}
Requires:       cmake(KF5WidgetsAddons) >= %{_tar_path}
Requires:       cmake(Qt5Core) >= 5.12.0
Requires:       cmake(Qt5Script) >= 5.12.0
Requires:       cmake(Qt5Widgets) >= 5.12.0
Requires:       cmake(Qt5Xml) >= 5.12.0

%description devel
Kross is a scripting bridge to embed scripting functionality
into an application. It supports QtScript as a scripting interpreter backend.
Development files.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
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
%license COPYING*
%{_kf5_libdir}/libKF5KrossCore.so.*
%{_kf5_libdir}/libKF5KrossUi.so.*
%{_kf5_plugindir}/

%files devel
%{_kf5_libdir}/libKF5KrossCore.so
%{_kf5_libdir}/libKF5KrossUi.so
%{_kf5_libdir}/cmake/KF5Kross/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_bindir}/kf5kross
%{_kf5_mandir}/man1/*kross.*
%{_kf5_mkspecsdir}/qt_KrossCore.pri
%{_kf5_mkspecsdir}/qt_KrossUi.pri

%changelog
