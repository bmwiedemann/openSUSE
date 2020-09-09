#
# spec file for package kdepim-runtime
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.63.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-runtime
Version:        20.08.1
Release:        0
Summary:        Akonadi resources for PIM applications
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libkolabxml-devel >= 1.1
BuildRequires:  libxslt-devel
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5AlarmCalendar)
BuildRequires:  cmake(KF5CalendarCore) >= %{kf5_version}
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5DAV)
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5Holidays) >= %{kf5_version}
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mbox)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5DBus) >= 5.11.0
BuildRequires:  cmake(Qt5Network) >= 5.11.0
BuildRequires:  cmake(Qt5NetworkAuth) >= 5.11.0
BuildRequires:  cmake(Qt5Test) >= 5.11.0
BuildRequires:  cmake(Qt5TextToSpeech) >= 5.11.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.11.0
BuildRequires:  cmake(Qt5Widgets) >= 5.11.0
BuildRequires:  cmake(Qt5XmlPatterns) >= 5.11.0
Requires:       akonadi-plugin-calendar
Requires:       akonadi-plugin-contacts
Requires:       akonadi-plugin-kalarmcal
Requires:       akonadi-plugin-mime
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
Provides:       kio-pimlibs = %{version}
Obsoletes:      kdepim4-runtime < %{version}
Obsoletes:      kio-pimlibs < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the Akonadi resources, agents and plugins needed to
use PIM applications.

%lang_package

%prep
%setup -q -n kdepim-runtime-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}

%cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  rm -rvf %{buildroot}%{_kf5_libdir}/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/kdepim-runtime.categories
%{_kf5_debugdir}/kdepim-runtime.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/72x72
%dir %{_kf5_iconsdir}/hicolor/96x96
%{_kf5_iconsdir}/hicolor/24x24/apps
%{_kf5_iconsdir}/hicolor/72x72/apps
%{_kf5_iconsdir}/hicolor/96x96/apps
%{_kf5_bindir}/*
%{_kf5_dbusinterfacesdir}/*.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/*.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}
%{_kf5_sharedir}/akonadi/
%{_kf5_sharedir}/mime/packages/kdepim-mime.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
