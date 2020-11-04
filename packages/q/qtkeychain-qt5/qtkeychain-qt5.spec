#
# spec file for package qtkeychain-qt5
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


%define lname   libqt5keychain1
Name:           qtkeychain-qt5
Version:        0.10.0
Release:        0
Summary:        A password store library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/frankosterfeld/qtkeychain
Source:         https://github.com/frankosterfeld/qtkeychain/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)

%description
qtkeychain can be used to store passwords.

%package -n %{lname}
Summary:        A password store library
Group:          System/Libraries
Recommends:     %{lname}-lang

%description -n %{lname}
qtkeychain can be used to store passwords.

%package devel
Summary:        Development files for the qtkeychain library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
qtkeychain can be used to store passwords.

This package contains development files for libqtkeychain.

%lang_package -n %{lname}

%prep
%autosetup -p1 -n qtkeychain-%{version}

%build
%cmake -DBUILD_WITH_QT4=OFF ..
%make_jobs

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libqt5keychain.so.*

%files devel
%license COPYING
%{_includedir}/qt5keychain
%{_libdir}/cmake/Qt5Keychain
%{_libdir}/libqt5keychain.so
%{_libdir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files -n %{lname}-lang
%license COPYING
%dir %{_datadir}/qt5
%dir %{_datadir}/qt5/translations
%{_datadir}/qt5/translations/*keychain*.qm

%changelog
