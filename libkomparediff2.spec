#
# spec file for package libkomparediff2
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



%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           libkomparediff2
Version:        24.02.2
Release:        0
Summary:        A library to compare files and strings
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Add-changes-to-allow-coinstallation.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
A library to compare files and strings, used in Kompare and KDevelop.

# Both libkomparediff packages will have to coexist until kdevelop is ported
%package -n libkomparediff2-5_95
Summary:        A library to compare files and strings
# Conflicting translations catalog
Conflicts:      libkomparediff2-lang
Conflicts:      libkomparediff2-5-lang

%description -n libkomparediff2-5_95
A library to compare files and strings, used in Kompare and KDevelop.

%package devel
Summary:        Development package for libkomparediff2
Requires:       libkomparediff2-5_95 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6XmlGui) >= %{kf6_version}
Conflicts:      libkomparediff-kf5-devel

%description devel
Development package for libkomparediff2.

%lang_package -n libkomparediff2-5_95

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libkomparediff2-5_95

%files -n libkomparediff2-5_95
%license LICENSES/*
%{_kf6_debugdir}/libkomparediff2.categories
%{_kf6_libdir}/libkomparediff2.so.*

%files devel
%{_includedir}/KompareDiff2/
%{_kf6_cmakedir}/KompareDiff2/
%{_kf6_libdir}/libkomparediff2.so

%files -n libkomparediff2-5_95-lang -f %{name}.lang

%changelog
