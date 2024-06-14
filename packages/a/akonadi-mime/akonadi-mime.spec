#
# spec file for package akonadi-mime
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           akonadi-mime
Version:        24.05.1
Release:        0
Summary:        MIME email parser for KDE PIM
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(libxslt)
Conflicts:      libKF6AkonadiMime5 < %{version}

%description
This package provides libraries needed for the correct parsing of email
messages.

%package -n libKPim6AkonadiMime6
Summary:        MIME email parser for KDE PIM - core library
Requires:       akonadi-mime >= %{version}
Obsoletes:      akonadi-mime-lang <= 23.04.0
Obsoletes:      libKF5AkonadiMime5 < %{version}
Obsoletes:      libKPim5AkonadiMime5 < %{version}
Obsoletes:      libKPim5AkonadiMime5-lang < %{version}

%description  -n libKPim6AkonadiMime6
This package contains the core libraries needed for the correct parsing of email
messages.

%package -n akonadi-plugin-mime
Summary:        MIME email parser for KDE PIM - runtime plugins
Requires:       libKPim6AkonadiMime6 >= %{version}

%description -n akonadi-plugin-mime
This package provides plugins required by PIM applications read and write parsed
email data.

%package devel
Summary:        MIME email parser for KDE PIM - development files
Requires:       libKPim6AkonadiMime6 = %{version}
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}

%description devel
This package contains development headers needed to use MIME message parsing
in KDE PIM applications.

%lang_package -n libKPim6AkonadiMime6

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6AkonadiMime6 --all-name

%ldconfig_scriptlets -n libKPim6AkonadiMime6

%files
%{_kf6_debugdir}/akonadi-mime.categories

%files -n libKPim6AkonadiMime6
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiMime.so.*

%files -n akonadi-plugin-mime
%{_kf6_configkcfgdir}/specialmailcollections.kcfg
%{_kf6_plugindir}/akonadi_serializer_mail.so
%dir %{_kf6_sharedir}/akonadi
%dir %{_kf6_sharedir}/akonadi/plugins
%dir %{_kf6_sharedir}/akonadi/plugins/serializer
%{_kf6_sharedir}/akonadi/plugins/serializer/akonadi_serializer_mail.desktop
%{_kf6_sharedir}/mime/packages/x-vnd.kde.contactgroup.xml

%files devel
%doc %{_kf6_qchdir}/KPim6AkonadiMime.*
%{_includedir}/KPim6/AkonadiMime/
%{_kf6_cmakedir}/KPim6AkonadiMime/
%{_kf6_libdir}/libKPim6AkonadiMime.so

%files -n libKPim6AkonadiMime6-lang -f libKPim6AkonadiMime6.lang

%changelog
