#
# spec file for package alkimia
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%define sonum 8
%ifarch aarch64 x86_64 %{x86_64} riscv64
%define with_qtwebengine 1
%endif

# QtQuick.Controls.1 and QtQuick.Dialogs.1 imports are upstream code issues
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.alkimia|QtQuick\\.Controls\\.1|QtQuick\\.Dialogs\\.1).*

%bcond_without released
Name:           alkimia
Version:        8.2.1
Release:        0
Summary:        Library with common classes and functionality used by finance applications
License:        LGPL-2.1-or-later
URL:            https://kmymoney.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        alkimia.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  gmp-devel
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuffCore) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= 6.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%if 0%{?with_qtwebengine}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
libalkimia is a library with common classes and functionality used by finance
applications.

%package -n libalkimia6-%{sonum}
Summary:        Library with common classes and functionality used by finance applications

%description -n libalkimia6-%{sonum}
libalkimia is a library for Qt6 with common classes and functionality used by finance
applications.

%package devel
Summary:        Development Files for libalkimia
Requires:       libalkimia6-%{sonum} = %{version}
%if 0%{?with_qtwebengine}
Requires:       cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif

%description devel
The development files for libalkimia.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

# Versioned CMake dirs is almost never a good idea
mv %{buildroot}%{_kf6_cmakedir}/LibAlkimia6-* %{buildroot}%{_kf6_cmakedir}/LibAlkimia6

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libalkimia6-%{sonum}

%files
%{_kf6_applicationsdir}/org.kde.onlinequoteseditor6.desktop
%{_kf6_appstreamdir}/org.kde.onlinequoteseditor6.appdata.xml
%{_kf6_bindir}/onlinequoteseditor6
%{_kf6_iconsdir}/hicolor/*/apps/onlinequoteseditor6.*
%{_kf6_knsrcfilesdir}/alkimia-quotes.knsrc
%{_kf6_knsrcfilesdir}/kmymoney-quotes.knsrc
%{_kf6_knsrcfilesdir}/skrooge-quotes.knsrc
%{_kf6_qmldir}/org/kde/alkimia6/
%dir %{_kf6_plasmadir}/plasmoids
%{_kf6_plasmadir}/plasmoids/org.wincak.foreigncurrencies26/

%files devel
%dir %{_includedir}/alkimia/
%{_includedir}/alkimia/Qt6/
%{_kf6_cmakedir}/LibAlkimia6/
%{_kf6_libdir}/libalkimia6.so
%{_libdir}/pkgconfig/libalkimia6.pc
%dir %{_kf6_sharedir}/gdb
%dir %{_kf6_sharedir}/gdb/auto-load
%dir %{_kf6_sharedir}/gdb/auto-load%{_kf6_libdir}
%{_kf6_sharedir}/gdb/auto-load%{_kf6_libdir}/libalkimia6*-gdb.py

%files -n libalkimia6-%{sonum}
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libalkimia6.so.*

%files lang -f %{name}.lang

%changelog
