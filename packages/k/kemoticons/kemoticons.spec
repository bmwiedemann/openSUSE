#
# spec file for package kemoticons
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


%define lname   libKF5Emoticons5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kemoticons
Version:        5.116.0
Release:        0
Summary:        Emoticon to graphical emoticon text converter
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Archive) >= %{_kf5_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
KEmoticons converts emoticons from text to a graphical representation with
images in HTML. It supports setting different themes for emoticons coming
from different providers.

%package -n %{lname}
Summary:        Emoticon to graphical emoticon text converter
Obsoletes:      libKF5Emoticons4

%description -n %{lname}
KEmoticons converts emoticons from text to a graphical representation with
images in HTML. It supports setting different themes for emoticons coming
from different providers.

%package devel
Summary:        Build environment for kemoticons, an emoticon text converter
Requires:       %{lname} = %{version}
Requires:       cmake(KF5Archive) >= %{_kf5_version}
Requires:       cmake(KF5Service) >= %{_kf5_version}
Requires:       cmake(Qt5Gui) >= %{qt5_version}

%description devel
KEmoticons converts emoticons from text to a graphical representation with
images in HTML. It supports setting different themes for emoticons coming
from different providers. Development files.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5Emoticons.so.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/emoticons/
%{_kf5_debugdir}/kemoticons.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5Emoticons.so
%{_kf5_libdir}/cmake/KF5Emoticons/
%{_kf5_includedir}/KEmoticons/
%{_kf5_mkspecsdir}/qt_KEmoticons.pri

%changelog
