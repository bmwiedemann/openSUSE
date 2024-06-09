#
# spec file for package kf6-kcodecs
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


%define qt6_version 6.6.0

%define rname   kcodecs
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kcodecs
Version:        6.3.0
Release:        0
Summary:        Method collection to manipulate strings using various encodings
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gperf
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KCodecs provides a collection of methods to manipulate strings using various
encodings.

%package -n libKF6Codecs6
Summary:        Method collection to manipulate strings using various encodings
Requires:       kf6-kcodecs >= %{version}

%description -n libKF6Codecs6
KCodecs provides a collection of methods to manipulate strings using various
encodings.

%package devel
Summary:        Header files for kcodecs, a method collection for string manipulation
Requires:       libKF6Codecs6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Development files for KCodecs, a method collection to manipulate
strings using various encodings.

%lang_package -n libKF6Codecs6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kcodecs6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Codecs6

%files
%{_kf6_debugdir}/*.categories
%{_kf6_debugdir}/*.renamecategories

%files -n libKF6Codecs6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Codecs.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Codecs.*
%{_kf6_includedir}/KCodecs/
%{_kf6_cmakedir}/KF6Codecs/
%{_kf6_libdir}/libKF6Codecs.so

%files -n libKF6Codecs6-lang -f kcodecs6.lang

%changelog
