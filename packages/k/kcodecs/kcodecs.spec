#
# spec file for package kcodecs
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


%define lname   libKF5Codecs5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kcodecs
Version:        5.116.0
Release:        0
Summary:        Method collection to manipulate strings using various encodings
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  gperf
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}

%description
KCodecs provides a collection of methods to manipulate strings using various
encodings.

%package -n %{lname}
Summary:        Method collection to manipulate strings using various encodings
%requires_ge    libQt5Core5

%description -n %{lname}
KCodecs provides a collection of methods to manipulate strings using various
encodings.

%package devel
Summary:        Header files for kcodecs, a method collection for string manipulation
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
Development files for KCodecs, a method collection to manipulate
strings using various encodings.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kcodecs5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f kcodecs5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Codecs.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Codecs/
%{_kf5_libdir}/libKF5Codecs.so
%{_kf5_mkspecsdir}/qt_KCodecs.pri

%changelog
