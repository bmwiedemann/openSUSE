#
# spec file for package kidentitymanagement
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kidentitymanagement
Version:        20.08.1
Release:        0
Summary:        KDE PIM Libraries: Identity Management
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Emoticons) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package provides a library to handle multiple email identities and
associated settings.

%package -n libKF5IdentityManagement5
Summary:        KDE PIM Libraries: Identity Management - core library
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5IdentityManagement5
This package provides the core library to handle multiple email identities and
associated settings.

%package devel
Summary:        KDE PIM Libraries: Identity Management - development files
Group:          Development/Libraries/KDE
Requires:       libKF5IdentityManagement5 = %{version}
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5PimTextEdit)

%description devel
This package contains necessary include files and libraries needed
to develop applications that make use of multiple email identities.

%lang_package

%prep
%setup -q -n kidentitymanagement-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5IdentityManagement5 -p /sbin/ldconfig
%postun -n libKF5IdentityManagement5 -p /sbin/ldconfig

%files -n libKF5IdentityManagement5
%license COPYING.LIB
%{_kf5_libdir}/libKF5IdentityManagement.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5IdentityManagement/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.pim.IdentityManager.xml
%{_kf5_includedir}/KIdentityManagement/
%{_kf5_includedir}/kidentitymanagement_version.h
%{_kf5_libdir}/libKF5IdentityManagement.so
%{_kf5_mkspecsdir}/qt_KIdentityManagement.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
