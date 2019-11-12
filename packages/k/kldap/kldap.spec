#
# spec file for package kldap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.19.0
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kldap
Version:        19.08.3
Release:        0
Summary:        KDE PIM Libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kcompletion-devel >= %{kf5_version}
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kio-devel
BuildRequires:  kmbox-devel
BuildRequires:  kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test)
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKF5Ldap5
Summary:        KDE PIM Libraries: LDAP support
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description  -n libKF5Ldap5
This package provides LDAP support for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       cyrus-sasl-devel
Requires:       kcoreaddons-devel >= %{kf5_version}
Requires:       libKF5Ldap5 = %{version}
Requires:       openldap2-devel

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kldap-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post -n libKF5Ldap5 -p /sbin/ldconfig
%postun -n libKF5Ldap5 -p /sbin/ldconfig

%files
%license COPYING.LIB
%{_kf5_debugdir}/kldap.categories
%{_kf5_debugdir}/kldap.renamecategories
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kio
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%{_kf5_plugindir}/kf5/kio/ldap.so
%{_kf5_servicesdir}/ldap*.protocol

%files -n libKF5Ldap5
%license COPYING.LIB
%{_kf5_libdir}/libKF5Ldap.so.*

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5Ldap/
%{_kf5_includedir}/KLDAP/
%{_kf5_includedir}/kldap_version.h
%{_kf5_libdir}/libKF5Ldap.so
%{_kf5_mkspecsdir}/qt_Ldap.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
