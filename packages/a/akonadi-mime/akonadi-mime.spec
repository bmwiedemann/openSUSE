#
# spec file for package akonadi-mime
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


%define sonum   5
%define kf5_version 5.23.0
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-mime
Version:        19.08.2
Release:        0
Summary:        MIME email parser for KDE PIM
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kdbusaddons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kitemmodels-devel >= %{kf5_version}
BuildRequires:  kmime-devel
BuildRequires:  kxmlgui-devel >= %{kf5_version}
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
Recommends:     %{name}-lang

%description
This package provides libraries needed for the correct parsing of email messages.

%package -n libKF5AkonadiMime5
Summary:        MIME email parser for KDE PIM - core library
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description  -n libKF5AkonadiMime5
This package contains the core libraries needed for the correct parsing of email messages.

%package -n akonadi-plugin-mime
Summary:        MIME email parser for KDE PIM - runtime plugins
Group:          System/Libraries
Requires:       libKF5AkonadiMime5 >= %{version}

%description -n akonadi-plugin-mime
This package provides plugins required by PIM applications read and write parsed email data.

%package devel
Summary:        MIME email parser for KDE PIM - development files
Group:          Development/Libraries/KDE
Requires:       akonadi-server-devel
Requires:       libKF5AkonadiMime5 = %{version}

%description devel
This package contains development headers needed to use MIME message parsing
in KDE PIM applications.

%lang_package

%prep
%setup -q -n akonadi-mime-%{version}

%build
%cmake_kf5 -d build -- -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5AkonadiMime5 -p /sbin/ldconfig
%postun -n libKF5AkonadiMime5 -p /sbin/ldconfig

%files -n libKF5AkonadiMime5
%license COPYING*
%{_kf5_libdir}/libKF5AkonadiMime.so.*
%{_kf5_debugdir}/*.categories

%files
%license COPYING*
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/specialmailcollections.kcfg
%{_kf5_mkspecsdir}/qt_AkonadiMime.pri
%{_kf5_sharedir}/mime/packages/x-vnd.kde.contactgroup.xml

%files -n akonadi-plugin-mime
%{_kf5_plugindir}/akonadi_serializer_mail.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_mail.desktop

%files devel
%license COPYING*
%dir %{_kf5_includedir}/Akonadi
%dir %{_kf5_includedir}/akonadi
%{_kf5_includedir}/Akonadi/KMime/
%{_kf5_includedir}/akonadi-mime_version.h
%{_kf5_includedir}/akonadi/kmime/
%{_kf5_cmakedir}/KF5AkonadiMime/
%{_kf5_libdir}/libKF5AkonadiMime.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
