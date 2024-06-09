#
# spec file for package kf6-kservice
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

%define rname kservice
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kservice
Version:        6.3.0
Release:        0
Summary:        Plugin framework for desktop services
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Recommends:     kded6 >= %{_kf6_bugfix_version}

%description
Provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code.

%package -n libKF6Service6
Summary:        Plugin framework for desktop services
Requires:       kf6-kservice >= %{version}

%description -n libKF6Service6
Provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code.

%package devel
Summary:        Plugin framework for desktop services: Build Environment
Requires:       libKF6Service6 = %{version}
Requires:       cmake(KF6Config) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}

%description devel
Provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code. Development files

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kservice6 --with-man --all-name

%ldconfig_scriptlets -n libKF6Service6

%files
%doc %lang(en) %{_kf6_mandir}/*/kbuildsycoca6.*
%{_kf6_bindir}/kbuildsycoca6
%{_kf6_debugdir}/kservice.categories
%{_kf6_debugdir}/kservice.renamecategories

%files -n libKF6Service6
%license LICENSES/*
%{_kf6_libdir}/libKF6Service.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Service.*
%{_kf6_cmakedir}/KF6Service/
%{_kf6_includedir}/KService/
%{_kf6_libdir}/libKF6Service.so

%files lang -f kservice6.lang

%changelog
