#
# spec file for package messagelib
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


%bcond_without released
Name:           messagelib
Version:        23.04.0
Release:        0
Summary:        KDE PIM library for e-mail message parsing and display
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextAutoCorrection)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5GrantleeTheme)
BuildRequires:  cmake(KPim5Gravatar)
BuildRequires:  cmake(KPim5IMAP)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5Mbox)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KPim5TextEdit)
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
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
This package contains the messagelib library. It is used by KDE PIM to parse and
display emails.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5Libkleo)
Requires:       cmake(KF5PimCommon)
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KPim5AkonadiMime)
Requires:       cmake(KPim5IdentityManagement)
Requires:       cmake(KPim5Mime)
Requires:       cmake(Qt5WebEngineWidgets)

%description devel
This package contains source headers for messagelib.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTS=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_debugdir}/messagelib.categories
%{_kf5_debugdir}/messagelib.renamecategories
%{_kf5_knsrcfilesdir}/messageviewer_header_themes.knsrc
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting
%dir %{_kf5_sharedir}/org.kde.syntax-highlighting/syntax
%{_kf5_sharedir}/org.kde.syntax-highlighting/syntax/kmail-template.xml
%{_kf5_configkcfgdir}/*.kcfg
%{_kf5_libdir}/libKPim5MessageComposer.so.*
%{_kf5_libdir}/libKPim5MessageCore.so.*
%{_kf5_libdir}/libKPim5MessageList.so.*
%{_kf5_libdir}/libKPim5MessageViewer.so.*
%{_kf5_libdir}/libKPim5MimeTreeParser.so.*
%{_kf5_libdir}/libKPim5TemplateParser.so.*
%{_kf5_libdir}/libKPim5WebEngineViewer.so.*
%{_kf5_notifydir}/messageviewer.notifyrc
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/messageviewer
%dir %{_kf5_plugindir}/pim5/messageviewer/grantlee
%dir %{_kf5_plugindir}/pim5/messageviewer/grantlee/5.0
%dir %{_kf5_plugindir}/pim5/messageviewer/headerstyle
%{_kf5_plugindir}/pim5/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
%{_kf5_plugindir}/pim5/messageviewer/grantlee/5.0/messageviewer_grantlee_extension.so
%{_kf5_sharedir}/libmessageviewer/
%{_kf5_sharedir}/messagelist/
%{_kf5_sharedir}/messageviewer/

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/MessageComposer/
%{_includedir}/KPim5/MessageCore/
%{_includedir}/KPim5/MessageList/
%{_includedir}/KPim5/MessageViewer/
%{_includedir}/KPim5/MimeTreeParser/
%{_includedir}/KPim5/TemplateParser/
%{_includedir}/KPim5/WebEngineViewer/
%{_kf5_cmakedir}/KPim5MessageComposer/
%{_kf5_cmakedir}/KPim5MessageCore/
%{_kf5_cmakedir}/KPim5MessageList/
%{_kf5_cmakedir}/KPim5MessageViewer/
%{_kf5_cmakedir}/KPim5MimeTreeParser/
%{_kf5_cmakedir}/KPim5TemplateParser/
%{_kf5_cmakedir}/KPim5WebEngineViewer/
%{_kf5_libdir}/libKPim5MessageComposer.so
%{_kf5_libdir}/libKPim5MessageCore.so
%{_kf5_libdir}/libKPim5MessageList.so
%{_kf5_libdir}/libKPim5MessageViewer.so
%{_kf5_libdir}/libKPim5MimeTreeParser.so
%{_kf5_libdir}/libKPim5TemplateParser.so
%{_kf5_libdir}/libKPim5WebEngineViewer.so
%{_kf5_mkspecsdir}/qt_*.pri

%files lang -f %{name}.lang

%changelog
