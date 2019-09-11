#
# spec file for package messagelib
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
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           messagelib
Version:        19.08.0
Release:        0
Summary:        KDE PIM library for e-mail message parsing and display
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-contact-devel
BuildRequires:  akonadi-mime-devel
BuildRequires:  akonadi-search-devel
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee5-devel
BuildRequires:  grantleetheme-devel
BuildRequires:  karchive-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kidentitymanagement-devel
BuildRequires:  kimap-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kldap-devel
BuildRequires:  kmailtransport-devel
BuildRequires:  kmbox-devel
BuildRequires:  kmime-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  libgravatar-devel
BuildRequires:  libkdepim-devel
BuildRequires:  libkleo-devel
BuildRequires:  libqgpgme-devel
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  syntax-highlighting-devel
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.4.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.4.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains the messagelib library. It is used by KDE PIM to parse and
display emails.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       akonadi-mime-devel
Requires:       akonadi-server-devel
Requires:       kcontacts-devel
Requires:       kidentitymanagement-devel
Requires:       kmime-devel
Requires:       libkleo-devel
Requires:       messagelib-devel
Requires:       pimcommon-devel
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif

%description devel
This package contains source headers for messagelib.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DMESSAGEVIEWER_USE_QTWEBENGINE=TRUE -DQTWEBENGINE_SUPPORT_OPTION=TRUE
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5MessageComposer/
%{_kf5_cmakedir}/KF5MessageCore/
%{_kf5_cmakedir}/KF5MessageList/
%{_kf5_cmakedir}/KF5MessageViewer/
%{_kf5_cmakedir}/KF5MimeTreeParser/
%{_kf5_cmakedir}/KF5TemplateParser/
%{_kf5_cmakedir}/KF5WebEngineViewer/
%{_kf5_includedir}/
%{_kf5_libdir}/libKF5MessageComposer.so
%{_kf5_libdir}/libKF5MessageCore.so
%{_kf5_libdir}/libKF5MessageList.so
%{_kf5_libdir}/libKF5MessageViewer.so
%{_kf5_libdir}/libKF5MimeTreeParser.so
%{_kf5_libdir}/libKF5TemplateParser.so
%{_kf5_libdir}/libKF5WebEngineViewer.so
%{_kf5_mkspecsdir}/qt_*.pri

%files
%license COPYING*
%{_kf5_debugdir}/messagelib.categories
%{_kf5_debugdir}/messagelib.renamecategories
%{_kf5_knsrcfilesdir}/messageviewer_header_themes.knsrc
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting/syntax
%{_kf5_sharedir}/org.kde.syntax-highlighting/syntax/kmail-template.xml
%{_kf5_configkcfgdir}/*.kcfg
%{_kf5_libdir}/libKF5MessageComposer.so.*
%{_kf5_libdir}/libKF5MessageCore.so.*
%{_kf5_libdir}/libKF5MessageList.so.*
%{_kf5_libdir}/libKF5MessageViewer.so.*
%{_kf5_libdir}/libKF5MimeTreeParser.so.*
%{_kf5_libdir}/libKF5TemplateParser.so.*
%{_kf5_libdir}/libKF5WebEngineViewer.so.*
%{_kf5_notifydir}/messageviewer.notifyrc
%{_kf5_plugindir}/messageviewer/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/libmessageviewer/
%{_kf5_sharedir}/messagelist/
%{_kf5_sharedir}/messageviewer/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
