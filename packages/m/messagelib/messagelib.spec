#
# spec file for package messagelib
#
# Copyright (c) 2021 SUSE LLC
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


%define kf5_version 5.79.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           messagelib
Version:        21.04.0
Release:        0
Summary:        KDE PIM library for e-mail message parsing and display
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-CVE-2021-31855.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5Gravatar)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mbox)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  libboost_headers-devel
Recommends:     %{name}-lang

%description
This package contains the messagelib library. It is used by KDE PIM to parse and
display emails.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IdentityManagement)
Requires:       cmake(KF5Libkleo)
Requires:       cmake(KF5MessageCore)
Requires:       cmake(KF5Mime)
Requires:       cmake(KF5PimCommon)

%description devel
This package contains source headers for messagelib.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files devel
%license LICENSES/*
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
%license LICENSES/*
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
%license LICENSES/*
%endif

%changelog
