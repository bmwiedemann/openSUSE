#
# spec file for package qtkeychain-qt5
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 1
Name:           qtkeychain-qt5
Version:        0.15.0
Release:        0
Summary:        A password store library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/frankosterfeld/qtkeychain
Source:         https://github.com/frankosterfeld/qtkeychain/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(libsecret-1)

%description
qtkeychain can be used to store passwords.

%package -n libqt5keychain%{sover}
Summary:        A password store library
Group:          System/Libraries
Recommends:     libqt5keychain%{sover}-lang

%description -n libqt5keychain%{sover}
qtkeychain can be used to store passwords.

%package devel
Summary:        Development files for the qtkeychain library
Group:          Development/Libraries/C and C++
Requires:       libqt5keychain%{sover} = %{version}
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5DBus)

%description devel
qtkeychain can be used to store passwords.

This package contains development files for libqtkeychain.

%lang_package -n libqt5keychain%{sover}

%prep
%autosetup -p1 -n qtkeychain-%{version}

%build
%cmake -DBUILD_TEST_APPLICATION:BOOL=FALSE
%cmake_build

%install
%cmake_install
%find_lang qtkeychain --with-qt

%ldconfig_scriptlets -n libqt5keychain%{sover}

%files -n libqt5keychain%{sover}
%license COPYING
%{_libdir}/libqt5keychain.so.%{sover}
%{_libdir}/libqt5keychain.so.%{version}

%files devel
%license COPYING
%{_includedir}/qt5keychain
%{_libdir}/cmake/Qt5Keychain
%{_libdir}/libqt5keychain.so
%{_libdir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files -n libqt5keychain%{sover}-lang -f qtkeychain.lang
%license COPYING
%dir %{_datadir}/qt5keychain
%dir %{_datadir}/qt5keychain/translations

%changelog
