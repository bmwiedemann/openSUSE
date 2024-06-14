#
# spec file for package mailcommon
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
Name:           mailcommon
Version:        24.05.1
Release:        0
Summary:        Base KDE PIM library for mail-handling applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailImporter) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageComposer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageList) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TemplateParser) >= %{kpim6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
The mailcommon library is a KDE PIM project to provide a
framework to build applications which handle e-mail.

%package -n libKPim6MailCommon6
Summary:        Common Mail library for KDE PIM applications
Requires:       mailcommon >= %{version}
Obsoletes:      libKF5MailCommon5 < %{version}
Obsoletes:      libKPim5MailCommon5 < %{version}

%description -n libKPim6MailCommon6
This package provides the mailcommon library, a base KDE PIM library
to build email-handling applications.

%package devel
Summary:        Development package for mailcommon
Requires:       libKPim6MailCommon6 = %{version}
Requires:       cmake(KF6Completion) >= %{kf6_version}
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6AkonadiMime) >= %{kpim6_version}
Requires:       cmake(KPim6Libkdepim) >= %{kpim6_version}
Requires:       cmake(KPim6MessageComposer) >= %{kpim6_version}
Requires:       cmake(KPim6PimCommon) >= %{kpim6_version}
Requires:       cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}

%description devel
This package contains the development headers for the mailcommon library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6MailCommon6

%files
%{_kf6_debugdir}/mailcommon.categories
%{_kf6_debugdir}/mailcommon.renamecategories

%files -n libKPim6MailCommon6
%license LICENSES/*
%{_libdir}/libKPim6MailCommon.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6MailCommon.*
%{_includedir}/KPim6/MailCommon/
%{_kf6_cmakedir}/KPim6MailCommon/
%{_kf6_libdir}/libKPim6MailCommon.so
%{_kf6_plugindir}/designer/mailcommon6widgets.so

%files lang -f %{name}.lang

%changelog
