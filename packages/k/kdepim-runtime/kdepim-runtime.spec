#
# spec file for package kdepim-runtime
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


%define kf5_version 5.103.0
%bcond_without released
Name:           kdepim-runtime
Version:        23.04.0
Release:        0
Summary:        Akonadi resources for PIM applications
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libkolabxml-devel >= 1.1
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5CalendarCore) >= %{kf5_version}
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5DAV)
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5Holidays) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5AkonadiNotes)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(KPim5GAPI)
BuildRequires:  cmake(KPim5IMAP)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5Mbox)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5TextToSpeech)
%ifarch %{ix86} x86_64 %{arm} aarch64
# Only the tomboy and ews resources need Qt5WebEngine
BuildRequires:  cmake(Qt5WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5XmlPatterns)
Recommends:     kalendarac
Requires:       akonadi-plugin-calendar
Requires:       akonadi-plugin-contacts
Requires:       akonadi-plugin-mime
Requires:       akonadi-server
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Provides:       kio-pimlibs = %{version}
Obsoletes:      kdepim4-runtime < %{version}
Obsoletes:      kio-pimlibs < %{version}

%description
This package contains the Akonadi resources, agents and plugins needed to
use PIM applications.

%lang_package

%prep
%autosetup -p1 -n kdepim-runtime-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%{_kf5_applicationsdir}/org.kde.akonadi_davgroupware_resource.desktop
%{_kf5_applicationsdir}/org.kde.akonadi_google_resource.desktop
%{_kf5_applicationsdir}/org.kde.akonadi_kolab_resource.desktop
%{_kf5_applicationsdir}/org.kde.akonadi_imap_resource.desktop
%{_kf5_bindir}/*
%{_kf5_dbusinterfacesdir}/*.xml
%{_kf5_debugdir}/kdepim-runtime.categories
%{_kf5_debugdir}/kdepim-runtime.renamecategories
%ifarch %{ix86} x86_64 %{arm} aarch64
%{_kf5_iconsdir}/hicolor/*/apps/akonadi-ews.png
%endif
%{_kf5_iconsdir}/hicolor/*/apps/ox.png
%{_kf5_libdir}/*.so.*
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/akonadi/
%{_kf5_sharedir}/mime/packages/kdepim-mime.xml

%files lang -f %{name}.lang

%changelog
