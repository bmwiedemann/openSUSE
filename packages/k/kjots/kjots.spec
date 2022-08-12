#
# spec file for package kjots
#
# Copyright (c) 2022 SUSE LLC
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


Name:           kjots
Version:        5.1.0
Release:        0
Summary:        A note taking application using Akonadi
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://userbase.kde.org/KJots/
Source0:        https://download.kde.org/stable/kjots/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         noteshared-add-missing-library-to-link-list.patch
Patch1:         Adapt-to-new-Akonadi-libraries.patch
# PATCH-FIX-UPSTREAM
Patch2:         Fix-akonadi-includes.patch
Patch3:         Fix-build-with-Akonadi-21.12.patch
Patch4:         0001-Adapt-to-new-KontactInterface-Plugin-ctor.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5XmlGui)
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc ANNOUNCE CHANGES README
%{_kf5_appstreamdir}/
%{_kf5_applicationsdir}/org.kde.kjots.desktop
%{_kf5_bindir}/kjots
%{_kf5_configkcfgdir}/kjots.kcfg
%{_kf5_kxmlguidir}/kjots/
%{_kf5_servicesdir}/kjotspart.desktop
%{_kf5_plugindir}/kjotspart.so
%{_kf5_plugindir}/kcm_kjots.so
%{_kf5_servicesdir}/kjots_config_misc.desktop
%{_kf5_sharedir}/kjots/
%{_kf5_iconsdir}/hicolor/*/apps/kjots.*
%dir %{_kf5_plugindir}/kontact5/
%{_kf5_plugindir}/kontact5/kontact_kjotsplugin.so
%{_kf5_sharedir}/kontact/
%{_kf5_servicesdir}/kontact/

%files lang -f kjots.lang

%changelog
