#
# spec file for package kjsembed
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


%define lname   libKF5JsEmbed5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kjsembed
Version:        5.75.0
Release:        0
Summary:        Method for binding Javascript objects to QObjects
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5JS) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Svg) >= 5.12.0
BuildRequires:  cmake(Qt5UiTools) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0

%description
KSJEmbed provides a method for binding JavaScript objects to QObjects,
so you can script your applications.

%package -n %{lname}
Summary:        Method for binding Javascript objects to QObjects
Group:          System/GUI/KDE
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KSJEmbed provides a method of binding JavaScript objects to QObjects,
so you can script your applications.

%package devel
Summary:        Build environment for kjsembed
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5I18n) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5JS) >= %{_kf5_bugfix_version}

%description devel
Development files for KSJEmbed, which provides a method of binding
JavaScript objects to QObjects, so applications can be scripted.

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
%find_lang %{name} --with-man --all-name
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}.lang
%endif

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5JsEmbed.so.*

%files devel
%{_kf5_libdir}/libKF5JsEmbed.so
%{_kf5_libdir}/cmake/KF5JsEmbed/
%{_kf5_bindir}/kjscmd5
%{_kf5_bindir}/kjsconsole
%{_kf5_mandir}/man1/kjscmd5.1*
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
#{_kf5_includedir}/*.h
%{_kf5_mkspecsdir}/qt_KJsEmbed.pri

%changelog
