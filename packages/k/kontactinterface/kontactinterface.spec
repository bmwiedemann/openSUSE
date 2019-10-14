#
# spec file for package kontactinterface
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
Name:           kontactinterface
Version:        19.08.2
Release:        0
Summary:        KDE PIM Libraries: Interface to Contacts
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kiconthemes-devel >= %{kf5_version}
BuildRequires:  kparts-devel >= %{kf5_version}
BuildRequires:  kwindowsystem-devel >= %{kf5_version}
BuildRequires:  kxmlgui-devel >= %{kf5_version}

%description
This package contains additional libraries for KDE PIM applications.

%package -n libKF5KontactInterface5
Summary:        KDE PIM Libraries: Interface to Contacts
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5KontactInterface5
This package provides the interface to contacts for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       kparts-devel >= %{kf5_version}
Requires:       libKF5KontactInterface5 = %{version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%setup -q -n kontactinterface-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=OFF -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5KontactInterface5 -p /sbin/ldconfig
%postun -n libKF5KontactInterface5 -p /sbin/ldconfig

%files -n libKF5KontactInterface5
%license COPYING.LIB
%{_kf5_libdir}/libKF5KontactInterface.so.*
%{_kf5_servicetypesdir}/kontactplugin.desktop
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5KontactInterface/
%{_kf5_includedir}/KontactInterface/
%{_kf5_includedir}/kontactinterface_version.h
%{_kf5_libdir}/libKF5KontactInterface.so
%{_kf5_mkspecsdir}/qt_KontactInterface.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
