#
# spec file for package kimap
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
Name:           kimap
Version:        19.08.1
Release:        0
Summary:        KDE PIM Libraries: IMAP library
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
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kmime-devel >= %{kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test)

%description
KIMAP provides libraries to interface and communicate with
IMAP mail servers.

%package -n libKF5IMAP5
Summary:        KDE PIM Libraries: IMAP APIs
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5IMAP5
This package provides the core library to interface and communicate with
IMAP mail servers.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       cyrus-sasl-devel
Requires:       kcoreaddons-devel >= %{kf5_version}
Requires:       kmime-devel >= %{_kapp_version}
Requires:       libKF5IMAP5 = %{version}

%description devel
This package contains development headers to add IMAP support to PIM
applications.

%lang_package

%prep
%setup -q -n kimap-%{version}

%build
  %global _lto_cflags %{_lto_cflags} -ffat-lto-objects
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5IMAP5 -p /sbin/ldconfig
%postun -n libKF5IMAP5 -p /sbin/ldconfig

%files -n libKF5IMAP5
%license COPYING*
%{_kf5_libdir}/libKF5IMAP.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5IMAP/
%{_kf5_includedir}/KIMAP/
%{_kf5_includedir}/kimap_version.h
%{_kf5_includedir}/kimaptest/
%{_kf5_libdir}/libKF5IMAP.so
%{_kf5_libdir}/libkimaptest.a
%{_kf5_mkspecsdir}/qt_KIMAP.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
