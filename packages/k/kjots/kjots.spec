#
# spec file for package kjots
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
Name:           kjots
Version:        5.1.1
Release:        0
Summary:        A note taking application using Akonadi
License:        GPL-2.0-or-later
URL:            https://userbase.kde.org/KJots/
Source0:        https://download.kde.org/stable/kjots/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kjots/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        kjots.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiNotes)
BuildRequires:  cmake(KPim5KontactInterface)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)

%description
This package contains KJOTS, a note taking application using Akonadi.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%make_jobs

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -C "Note Taker" org.kde.kjots    Utility  DesktopUtility

%find_lang %{name}

%ldconfig_scriptlets

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/kontact
%{_kf5_applicationsdir}/org.kde.kjots.desktop
%{_kf5_appstreamdir}/org.kde.kjots.appdata.xml
%{_kf5_bindir}/kjots
%{_kf5_configkcfgdir}/kjots.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kjots.*
%{_kf5_kxmlguidir}/kjots/
%{_kf5_plugindir}/kcm_kjots.so
%{_kf5_plugindir}/kjotspart.so
%{_kf5_plugindir}/pim5/kontact/kontact_kjotsplugin.so
%{_kf5_servicesdir}/kjots_config_misc.desktop
%{_kf5_servicesdir}/kjotspart.desktop
%{_kf5_sharedir}/kjots/

%files lang -f kjots.lang

%changelog
