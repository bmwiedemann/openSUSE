#
# spec file for package kjsembed
#
# Copyright (c) 2021 SUSE LLC
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


%define lname   libKF5JsEmbed5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kjsembed
Version:        5.101.0
Release:        0
Summary:        Method for binding Javascript objects to QObjects
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5JS) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Svg) >= 5.15.0
BuildRequires:  cmake(Qt5UiTools) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

%description
KSJEmbed provides a method for binding JavaScript objects to QObjects,
so you can script your applications.

%package -n %{lname}
Summary:        Method for binding Javascript objects to QObjects

%description -n %{lname}
KSJEmbed provides a method of binding JavaScript objects to QObjects,
so you can script your applications.

%package devel
Summary:        Build environment for kjsembed
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5I18n) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5JS) >= %{_kf5_bugfix_version}

%description devel
Development files for KSJEmbed, which provides a method of binding
JavaScript objects to QObjects, so applications can be scripted.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang %{name} --with-man --all-name

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f %{name}.lang

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5JsEmbed.so.*

%files devel
%{_kf5_bindir}/kjscmd5
%{_kf5_bindir}/kjsconsole
%{_kf5_includedir}/KJsEmbed/
%{_kf5_libdir}/cmake/KF5JsEmbed/
%{_kf5_libdir}/libKF5JsEmbed.so
%{_kf5_mandir}/man1/kjscmd5.1*
%{_kf5_mkspecsdir}/qt_KJsEmbed.pri

%changelog
