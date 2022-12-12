#
# spec file for package kcoreaddons
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


%define lname   libKF5CoreAddons5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kcoreaddons
Version:        5.101.0
Release:        0
Summary:        Utilities for core application functionality and accessing the OS
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_tar_path}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
Requires:       shared-mime-info

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package -n %{lname}
Summary:        Utilities for core application functionality and accessing the OS
%requires_ge    libQt5Core5
Recommends:     %{name} = %{version}

%description -n %{lname}
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package devel
Summary:        Utilities for core application functionality and accessing the OS
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more. Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert -DKDE4_DEFAULT_HOME=".kde4"
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang %{name} --all-name --with-qt --without-mo

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%{_kf5_appsdir}/mime/packages/kde5.xml
%{_kf5_datadir}/

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/kcoreaddons.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5CoreAddons.so.*

%files devel
%{_kf5_bindir}/desktoptojson
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5CoreAddons/
%{_kf5_libdir}/libKF5CoreAddons.so
%{_kf5_mkspecsdir}/qt_KCoreAddons.pri

%changelog
