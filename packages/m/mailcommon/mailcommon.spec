#
# spec file for package mailcommon
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
%define libname libKPim5MailCommon5
Name:           mailcommon
Version:        23.04.0
Release:        0
Summary:        Base KDE PIM library for mail-handling applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  xsltproc
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailImporter)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5MessageCore)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
The mailcommon library is a KDE PIM project to provide a
framework to build applications which handle e-mail.

%package -n %{libname}
Summary:        Common Mail library for KDE PIM applications
License:        LGPL-2.1-or-later
Requires:       %{name}

%description -n %{libname}
This package provides the mailcommon library, a base KDE PIM library
to build email-handling applications.

%package devel
Summary:        Development package for mailcommon
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Requires:       cmake(KF5Completion)
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KPim5AkonadiMime)
Requires:       cmake(KPim5Libkdepim)
Requires:       cmake(KPim5MessageCore)
Requires:       cmake(KF5PimCommon)

%description devel
This package contains the development headers for the mailcommon library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%{_kf5_debugdir}/mailcommon.categories
%{_kf5_debugdir}/mailcommon.renamecategories

%files -n %{libname}
%license LICENSES/*
%{_libdir}/libKPim5MailCommon.so.*

%files devel
%dir %{_includedir}/KPim5
%dir %{_kf5_plugindir}/designer
%{_includedir}/KPim5/MailCommon/
%{_kf5_cmakedir}/KF5MailCommon/
%{_kf5_cmakedir}/KPim5MailCommon/
%{_kf5_libdir}/libKPim5MailCommon.so
%{_kf5_mkspecsdir}/qt_MailCommon.pri
%{_kf5_plugindir}/designer/mailcommon5widgets.so

%files lang -f %{name}.lang

%changelog
