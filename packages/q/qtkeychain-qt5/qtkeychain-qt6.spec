#
# spec file for package qtkeychain-qt6
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
Name:           qtkeychain-qt6
Version:        0.15.0
Release:        0
Summary:        Platform-independent Qt API for storing passwords securely
License:        BSD-2-Clause
URL:            https://github.com/frankosterfeld/qtkeychain
Source:         https://github.com/frankosterfeld/qtkeychain/archive/refs/tags/%{version}.tar.gz#/qtkeychain-qt5-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(libsecret-1)

%description
QtKeychain is a Qt API to store passwords and other secret data securely.

%package -n libqt6keychain%{sover}
Summary:        Qt 6 keychain library
Recommends:     qtkeychain-qt6-lang

%description -n libqt6keychain%{sover}
The Qt 6 keychain library.

%package devel
Summary:        Development files for libqt6keychain
Requires:       libqt6keychain%{sover} = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6DBus)

%description devel
This package contains development files for using the Qt6 keychain API.

%package lang
Summary:        Translations for package %{name}
Requires:       libqt6keychain%{sover} = %{version}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations for the "qtkeychain-qt6" package.

%prep
%autosetup -p1 -n qtkeychain-%{version}

%build
%cmake_qt6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DQMAKE_EXECUTABLE:STRING=%{_qt6_bindir}/qmake

%qt6_build

%install
%qt6_install

%find_lang qtkeychain --with-qt

%ldconfig_scriptlets -n libqt6keychain%{sover}

%files -n libqt6keychain%{sover}
%license COPYING
%doc ChangeLog ReadMe.md
%{_libdir}/libqt6keychain.so.%{sover}
%{_libdir}/libqt6keychain.so.%{version}

%files devel
%{_includedir}/qt6keychain
%{_libdir}/libqt6keychain.so
%{_libdir}/cmake/Qt6Keychain/
%{_qt6_mkspecsdir}/modules/qt_Qt6Keychain.pri

%files lang -f qtkeychain.lang
%dir %{_datadir}/qt6keychain
%dir %{_datadir}/qt6keychain/translations

%changelog
