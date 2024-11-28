#
# spec file for package diskmonitor
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


Name:           diskmonitor
Version:        0.3.4
Release:        0
Summary:        Tools to monitor SMART devices and MDRaid health status
License:        GPL-2.0-only
URL:            https://github.com/papylhomme/diskmonitor
Source0:        https://github.com/papylhomme/diskmonitor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Install-the-application-icon-in-the-right-directory.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
Requires:       udisks2 >= 2.1

%description
Tools to monitor SMART devices and MDRaid health status.
Features a full application and a Plasma applet.

Application:

- Display S.M.A.R.T. attributes for harddrives supporting it.
- Start and monitor progress of S.M.A.R.T. Short and Extended self test.
- Display properties for MDRaid arrays.
- Start and monitor progress of data scrubbing on MDRaid arrays.

Applet:

- Display basic health status for storage units.
- Can be used on the desktop, on a panel or as a systray icon (see systray settings to activate).
- Use KDE notification for health status change.
- Highly configurable interface.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang diskmonitor diskmonitor.lang
%find_lang plasma_applet_org.papylhomme.diskmonitor diskmonitor.lang

%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md CHANGELOG
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_qmldir}/org/
%{_kf5_appstreamdir}/org.papylhomme.diskmonitor.appdata.xml
%{_kf5_bindir}/diskmonitor
%{_kf5_configkcfgdir}/diskmonitor.kcfg
%{_kf5_iconsdir}/hicolor/scalable/apps/diskmonitor.svg
%{_kf5_notifydir}/diskmonitor.notifyrc
%{_kf5_plasmadir}/plasmoids/
%{_kf5_qmldir}/org/papylhomme/
%if %{pkg_vcmp plasma-framework-devel < 5.84} || %{pkg_vcmp plasma-framework-devel > 5.89}
%{_kf5_servicesdir}/plasma-applet-org.papylhomme.diskmonitor.desktop
%endif
%{_kf5_sharedir}/applications/diskmonitor.desktop

%files lang -f diskmonitor.lang

%changelog
