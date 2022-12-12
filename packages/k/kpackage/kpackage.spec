#
# spec file for package kpackage
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kpackage
Version:        5.101.0
Release:        0
Summary:        Non-binary asset user-installable package managing framework
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
This framework lets applications to manage user installable packages of non-binary assets.

%package devel
Summary:        Non-binary asset user-installable package managing framework
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}

%description devel
This framework lets applications to manage user installable packages of non-binary assets.
Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%license LICENSES/*
%doc README*
%dir %{_kf5_servicetypesdir}
%doc %lang(en) %{_kf5_mandir}/*/kpackagetool*
%{_kf5_bindir}/kpackagetool*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Package.so.*
%{_kf5_servicetypesdir}/kpackage-generic.desktop
%{_kf5_servicetypesdir}/kpackage-genericqml.desktop
%{_kf5_servicetypesdir}/kpackage-packagestructure.desktop

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Package/
%{_kf5_libdir}/libKF5Package.so

%changelog
