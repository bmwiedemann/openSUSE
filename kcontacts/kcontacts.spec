#
# spec file for package kcontacts
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


%define kf5_version 5.26.0
%define lname libKF5Contacts5
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang

Name:           kcontacts
Version:        19.08.1
Release:        0
Summary:        KDE Frameworks based address book API
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  kcodecs-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.3.0

%description
kcontacts is a Qt5 based library which provides an API
to access address book data stored in different formats.

%package -n %{lname}
Summary:        KDE Frameworks based address book API
Group:          System/Libraries
Provides:       %{name} = %{version}
# package existed in KDE:Unstable:Applications for a short while
Provides:       %{name}-data = %{version}
Obsoletes:      %{name}-data < %{version}
Recommends:     %{name}-lang

%description  -n libKF5Contacts5
kcontacts is a Qt5 based library which provides an API
to access address book data stored in different formats.

%package devel
Summary:        Development files for kcontacts
Group:          Development/Libraries/KDE
Requires:       kcoreaddons-devel >= %{kf5_version}
Requires:       libKF5Contacts5 = %{version}
Provides:       kcontacts5-devel = %{version}
Obsoletes:      kcontacts5-devel < %{version}

%description devel
Development files for kcontacts, a Qt5 library to access
address books.

%lang_package

%prep
%setup -q -n kcontacts-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5Contacts5 -p /sbin/ldconfig
%postun -n libKF5Contacts5 -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_kf5_libdir}/libKF5Contacts.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Contacts/
%{_kf5_includedir}/KContacts/
%{_kf5_includedir}/kcontacts_version.h
%{_kf5_libdir}/libKF5Contacts.so
%{_kf5_mkspecsdir}/qt_KContacts.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
