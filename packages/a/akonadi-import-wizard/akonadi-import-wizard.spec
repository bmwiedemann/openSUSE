#
# spec file for package akonadi-import-wizard
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


%define lname libKPimImportWizard5
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-import-wizard
Version:        20.08.1
Release:        0
Summary:        Assistant to import PIM data
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5MailImporter)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Gui) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Assistant to import PIM data from other applications into Akonadi for use in KDE PIM applications.

%package -n %{lname}
Summary:        Assistant to import PIM data
Group:          System/GUI/KDE
Recommends:     %{name} = %{version}

%description -n %{lname}
This package contains the shared libraries used to provide the mail import
wizard functionality to KDE PIM applications.

%package devel
Summary:        Development files for the PIM data import assistant
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}

%description devel
This package contains development headers to build new import plugins for KDE PIM.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file -u org.kde.akonadiimportwizard    Network Email
rm -rf %{buildroot}%{_libdir}/libimportwizard.so

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/importwizard.categories
%{_kf5_debugdir}/importwizard.renamecategories
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_plugindir}/importwizard
%dir %{_kf5_sharedir}/importwizard
%dir %{_kf5_sharedir}/importwizard/pics
%dir %{_kf5_sharedir}/kconf_update/
%{_kf5_applicationsdir}/org.kde.akonadiimportwizard.desktop
%{_kf5_bindir}/akonadiimportwizard
%doc %lang(en) %{_kf5_htmldir}/en/importwizard/
%{_kf5_iconsdir}/hicolor/*/apps/kontact-import-wizard.png
%{_kf5_plugindir}/importwizard/*.so
%{_kf5_sharedir}/importwizard/pics/step1.png
%{_kf5_sharedir}/kconf_update/importwizard-15.08-kickoff.sh
%{_kf5_sharedir}/kconf_update/importwizard.upd

%files -n %{lname}
%{_kf5_libdir}/libKPimImportWizard.so.5*

%files devel
%dir %{_includedir}/KPim
%dir %{_kf5_includedir}/KPim
%{_kf5_cmakedir}/KPimImportWizard/
%{_kf5_includedir}/KPim/ImportWizard/
%{_kf5_includedir}/KPim/importwizard/
%{_includedir}/KPim/importwizard_version.h
%{_kf5_libdir}/libKPimImportWizard.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
