#
# spec file for package akonadi-import-wizard
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
Name:           akonadi-import-wizard
Version:        24.05.1
Release:        0
Summary:        Assistant to import PIM data
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailCommon) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailImporterAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.14.2
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Assistant to import PIM data from other applications into Akonadi for use in
KDE PIM applications.

%package -n libKPim6ImportWizard6
Summary:        Assistant to import PIM data
Recommends:     akonadi-import-wizard >= %{version}
Obsoletes:      libKPim5ImportWizard5 < %{version}
Obsoletes:      libKPimImportWizard5 < %{version}

%description -n libKPim6ImportWizard6
This package contains the shared libraries used to provide the mail import
wizard functionality to KDE PIM applications.

%package devel
Summary:        Development files for the PIM data import assistant
Requires:       libKPim6ImportWizard6 = %{version}

%description devel
This package contains development headers to build new import plugins for
KDE PIM applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n libKPim6ImportWizard6

%files
%doc %lang(en) %{_kf6_htmldir}/en/importwizard/
%{_kf6_applicationsdir}/org.kde.akonadiimportwizard.desktop
%{_kf6_bindir}/akonadiimportwizard
%{_kf6_debugdir}/importwizard.categories
%{_kf6_debugdir}/importwizard.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/kontact-import-wizard.png
%dir %{_kf6_plugindir}/pim6/
%{_kf6_plugindir}/pim6/importwizard
%dir %{_kf6_sharedir}/importwizard
%dir %{_kf6_sharedir}/importwizard/pics
%{_kf6_sharedir}/importwizard/pics/step1.png

%files -n libKPim6ImportWizard6
%license LICENSES/*
%{_kf6_libdir}/libKPim6ImportWizard.so.*

%files devel
%{_includedir}/KPim6/ImportWizard/
%{_kf6_cmakedir}/KPim6ImportWizard/
%{_kf6_libdir}/libKPim6ImportWizard.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/importwizard/

%changelog
