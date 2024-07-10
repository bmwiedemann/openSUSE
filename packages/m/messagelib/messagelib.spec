#
# spec file for package messagelib
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           messagelib
Version:        24.05.2
Release:        0
Summary:        KDE PIM library for e-mail message parsing and display
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiSearch) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Gravatar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mbox) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TextEdit) >= %{kpim6_version}
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package contains the messagelib library. It is used by KDE PIM to parse and
display emails.

%package devel
Summary:        Library for messages
License:        LGPL-2.1-or-later
Requires:       messagelib = %{version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}
Requires:       cmake(KF6Service) >= %{kf6_version}
Requires:       cmake(KF6TextAutoCorrectionWidgets)
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6AkonadiMime) >= %{kpim6_version}
Requires:       cmake(KPim6IdentityManagementWidgets) >= %{kpim6_version}
Requires:       cmake(KPim6Libkleo) >= %{kpim6_version}
Requires:       cmake(KPim6MessageCore) >= %{kpim6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}
Requires:       cmake(KPim6MimeTreeParser) >= %{kpim6_version}
Requires:       cmake(KPim6PimCommon) >= %{kpim6_version}
Requires:       cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
Requires:       cmake(KPim6TemplateParser) >= %{kpim6_version}
Requires:       cmake(KPim6WebEngineViewer) >= %{kpim6_version}
Requires:       cmake(Qt6WebEngineWidgets) >= %{qt6_version}

%description devel
This package contains source headers for messagelib.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_debugdir}/messagelib.categories
%{_kf6_debugdir}/messagelib.renamecategories
%{_kf6_knsrcfilesdir}/messageviewer_header_themes.knsrc
%dir %{_kf6_sharedir}/org.kde.syntax-highlighting
%dir %{_kf6_sharedir}/org.kde.syntax-highlighting/syntax
%{_kf6_sharedir}/org.kde.syntax-highlighting/syntax/kmail-template.xml
%{_kf6_configkcfgdir}/customtemplates_kfg.kcfg
%{_kf6_configkcfgdir}/templatesconfiguration_kfg.kcfg
%{_kf6_libdir}/libKPim6MessageComposer.so.*
%{_kf6_libdir}/libKPim6MessageCore.so.*
%{_kf6_libdir}/libKPim6MessageList.so.*
%{_kf6_libdir}/libKPim6MessageViewer.so.*
%{_kf6_libdir}/libKPim6MimeTreeParser.so.*
%{_kf6_libdir}/libKPim6TemplateParser.so.*
%{_kf6_libdir}/libKPim6WebEngineViewer.so.*
%{_kf6_notificationsdir}/messageviewer.notifyrc
%dir %{_kf6_plugindir}/pim6
%{_kf6_plugindir}/pim6/messageviewer/
%{_kf6_sharedir}/libmessageviewer/
%{_kf6_sharedir}/messagelist/
%{_kf6_sharedir}/messageviewer/

%files devel
%doc %{_kf6_qchdir}/*
%{_includedir}/KPim6/MessageComposer/
%{_includedir}/KPim6/MessageCore/
%{_includedir}/KPim6/MessageList/
%{_includedir}/KPim6/MessageViewer/
%{_includedir}/KPim6/MimeTreeParser/
%{_includedir}/KPim6/TemplateParser/
%{_includedir}/KPim6/WebEngineViewer/
%{_kf6_cmakedir}/KPim6MessageComposer/
%{_kf6_cmakedir}/KPim6MessageCore/
%{_kf6_cmakedir}/KPim6MessageList/
%{_kf6_cmakedir}/KPim6MessageViewer/
%{_kf6_cmakedir}/KPim6MimeTreeParser/
%{_kf6_cmakedir}/KPim6TemplateParser/
%{_kf6_cmakedir}/KPim6WebEngineViewer/
%{_kf6_libdir}/libKPim6MessageComposer.so
%{_kf6_libdir}/libKPim6MessageCore.so
%{_kf6_libdir}/libKPim6MessageList.so
%{_kf6_libdir}/libKPim6MessageViewer.so
%{_kf6_libdir}/libKPim6MimeTreeParser.so
%{_kf6_libdir}/libKPim6TemplateParser.so
%{_kf6_libdir}/libKPim6WebEngineViewer.so

%files lang -f %{name}.lang

%changelog
