#
# spec file for package akonadi-mime
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


%define sonum   5
%define kf5_version 5.104.0
%define libname libKPim5AkonadiMime5
%bcond_without released
Name:           akonadi-mime
Version:        23.04.0
Release:        0
Summary:        MIME email parser for KDE PIM
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libxslt-devel
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test) >= 5.15.2
BuildRequires:  cmake(Qt5Widgets) >= 5.15.2
Conflicts:      libKF5AkonadiMime5 < %{version}

%description
This package provides libraries needed for the correct parsing of email
messages.

%package -n %{libname}
Summary:        MIME email parser for KDE PIM - core library
%requires_eq    akonadi-mime
# Renamed
Obsoletes:      akonadi-mime-lang <= 23.04.0

%description  -n %{libname}
This package contains the core libraries needed for the correct parsing of email
messages.

%package -n akonadi-plugin-mime
Summary:        MIME email parser for KDE PIM - runtime plugins
Requires:       %{libname} >= %{version}

%description -n akonadi-plugin-mime
This package provides plugins required by PIM applications read and write parsed
email data.

%package devel
Summary:        MIME email parser for KDE PIM - development files
Requires:       %{libname} = %{version}
Requires:       cmake(KPim5Akonadi)

%description devel
This package contains development headers needed to use MIME message parsing
in KDE PIM applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n akonadi-mime-%{version}

%build
%cmake_kf5 -d build -- -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%{_kf5_configkcfgdir}/specialmailcollections.kcfg
%{_kf5_debugdir}/*.categories
%{_kf5_mkspecsdir}/qt_AkonadiMime.pri
%{_kf5_sharedir}/mime/packages/x-vnd.kde.contactgroup.xml

%files -n %{libname}
%{_kf5_libdir}/libKPim5AkonadiMime.so.*

%files -n akonadi-plugin-mime
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_plugindir}/akonadi_serializer_mail.so
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_mail.desktop

%files devel
%dir %{_includedir}/KPim5
%{_kf5_cmakedir}/KF5AkonadiMime/
%{_kf5_cmakedir}/KPim5AkonadiMime/
%{_includedir}/KPim5/AkonadiMime/
%{_kf5_libdir}/libKPim5AkonadiMime.so

%files -n %{libname}-lang -f %{libname}.lang

%changelog
