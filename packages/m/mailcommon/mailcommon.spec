#
# spec file for package mailcommon
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
Name:           mailcommon
Version:        21.04.0
Release:        0
Summary:        Base KDE PIM library for mail-handling applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  xsltproc
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
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
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailImporter)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
The mailcommon library is a KDE PIM project to provide a
framework to build applications which handle e-mail.

%if %{with lang}
%lang_package
%endif

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

%package -n libKF5MailCommon5
Summary:        Common Mail library for KDE PIM applications
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}

%description -n libKF5MailCommon5
This package provides the mailcommon library, a base KDE PIM library
to build email-handling applications.

%post -n libKF5MailCommon5 -p /sbin/ldconfig
%postun -n libKF5MailCommon5 -p /sbin/ldconfig

%package devel
Summary:        Development package for mailcommon
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5MailCommon5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5Completion)
Requires:       cmake(KF5Libkdepim)
Requires:       cmake(KF5MessageCore)
Requires:       cmake(KF5PimCommon)

%description devel
This package contains the development headers for the mailcommon library.

%files
%license LICENSES/*
%{_kf5_debugdir}/mailcommon.categories
%{_kf5_debugdir}/mailcommon.renamecategories

%files devel
%license LICENSES/*
%dir %{_kf5_plugindir}/designer
%{_kf5_includedir}/MailCommon/
%{_kf5_includedir}/mailcommon/
%{_kf5_includedir}/mailcommon_version.h
%{_kf5_libdir}/cmake/KF5MailCommon/
%{_kf5_libdir}/libKF5MailCommon.so
%{_kf5_mkspecsdir}/qt_MailCommon.pri
%{_kf5_plugindir}/designer/mailcommonwidgets.so

%files -n libKF5MailCommon5
%license LICENSES/*
%{_libdir}/libKF5MailCommon.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
