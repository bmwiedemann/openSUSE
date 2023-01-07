#
# spec file for package libkomparediff2
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


%define soname 5
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkomparediff2
Version:        22.12.1
Release:        0
Summary:        A library to compare files and strings
License:        (GPL-2.0-or-later AND LGPL-2.0-or-later) AND BSD-2-Clause
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}

%description
A library to compare files and strings, used in Kompare and KDevelop.

%package devel
Summary:        Development package for libkomparediff2
Requires:       %{name}-%{soname} = %{version}
Obsoletes:      %{name}-kf5-devel < %{version}
Provides:       %{name}-kf5-devel = %{version}

%description devel
Development package for libkomparediff2.

%package %{soname}
Summary:        A library to compare files and strings
Provides:       %{name} = %{version}
Recommends:     %{name}-lang

%description %{soname}
A library to compare files and strings, used in Kompare and KDevelop.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name


%post %{soname} -p /sbin/ldconfig
%postun %{soname} -p /sbin/ldconfig

%files %{soname}
%license COPYING*
%{_kf5_debugdir}/libkomparediff2.categories
%{_kf5_libdir}/libkomparediff2.so.*

%files devel
%{_kf5_cmakedir}/LibKompareDiff2/
%{_kf5_libdir}/libkomparediff2.so
%{_kf5_prefix}/include/libkomparediff2/

%files lang -f %{name}.lang

%changelog
