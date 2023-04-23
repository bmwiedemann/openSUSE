#
# spec file for package akonadi-import-wizard
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


%define libname libKPim5ImportWizard5
%define kf5_version 5.104.0
%bcond_without released
Name:           akonadi-import-wizard
Version:        23.04.0
Release:        0
Summary:        Assistant to import PIM data
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5MailCommon)
BuildRequires:  cmake(KPim5MailImporterAkonadi)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5MessageViewer)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Widgets)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
Assistant to import PIM data from other applications into Akonadi for use in
KDE PIM applications.

%package -n %{libname}
Summary:        Assistant to import PIM data
Recommends:     %{name} = %{version}

%description -n %{libname}
This package contains the shared libraries used to provide the mail import
wizard functionality to KDE PIM applications.

%package devel
Summary:        Development files for the PIM data import assistant
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description devel
This package contains development headers to build new import plugins for
KDE PIM applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -u org.kde.akonadiimportwizard Network Email

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/importwizard
%dir %{_kf5_sharedir}/importwizard
%dir %{_kf5_sharedir}/importwizard/pics
%doc %lang(en) %{_kf5_htmldir}/en/importwizard/
%{_kf5_applicationsdir}/org.kde.akonadiimportwizard.desktop
%{_kf5_bindir}/akonadiimportwizard
%{_kf5_debugdir}/importwizard.categories
%{_kf5_debugdir}/importwizard.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/kontact-import-wizard.png
%{_kf5_plugindir}/pim5/importwizard/*.so
%{_kf5_sharedir}/importwizard/pics/step1.png

%files -n %{libname}
%{_kf5_libdir}/libKPim5ImportWizard.so.5*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/importwizard_version.h
%{_includedir}/KPim5/ImportWizard/
%{_includedir}/KPim5/importwizard/
%{_kf5_cmakedir}/KPimImportWizard/
%{_kf5_cmakedir}/KPim5ImportWizard/
%{_kf5_libdir}/libKPim5ImportWizard.so

%files lang -f %{name}.lang

%changelog
