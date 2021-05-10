#
# spec file for package kdesu
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


%define lname   libKF5Su5
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdesu
Version:        5.82.0
Release:        0
Summary:        User interface for running shell commands with root privileges
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE fpie.patch -- make kdesud compile/link with -(f)pie flags
Patch0:         fpie.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Unset-QT_QPA_PLATFORM-to-get-xcb.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Pty) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  pkgconfig(x11)

%description
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package -n %{lname}
Summary:        User interface for running shell commands with root privileges
Group:          System/GUI/KDE
Requires(pre):  permissions
Requires(pre):  group(nogroup)
Obsoletes:      libKF5Su4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package devel
Summary:        User interface for running shell commands with root privileges
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Pty) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}

%description devel
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%if %{with lang}
%find_lang kdesud5 %{name}.lang
%endif

%post -n %{lname}
/sbin/ldconfig
%set_permissions %{_kf5_libexecdir}/kdesud

%postun -n %{lname} -p /sbin/ldconfig
%verifyscript -n %{lname}
%verify_permissions -e %{_kf5_libexecdir}/kdesud

%if %{with lang}
%files -n %{lname}-lang -f %{name}.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5Su.so.*
%{_kf5_libexecdir}/kdesu_stub
%{_kf5_debugdir}/ksu.categories
%verify(not mode) %attr(2755,root,nogroup) %{_kf5_libexecdir}/kdesud

%files devel
%{_kf5_libdir}/libKF5Su.so
%{_kf5_libdir}/cmake/KF5Su/
%{_kf5_includedir}/*.h
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_mkspecsdir}/qt_KDESu.pri

%changelog
