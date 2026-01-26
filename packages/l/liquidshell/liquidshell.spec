#
# spec file for package liquidshell
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Copyright (c) 2024 Martin Koller
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%bcond_without released
Name:           liquidshell
Version:        1.10.1
Release:        0
Summary:        Basic Desktop Shell leveraging KDE Frameworks6 libraries
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/liquidshell
Source0:        https://download.kde.org/stable/liquidshell/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/liquidshell/%{name}-%{version}.tar.xz.sig
Source2:        liquidshell.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  qt6-platformsupport-devel-static
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(packagekitqt6)
Requires:       kmenuedit6
Requires:       kscreen6
Requires:       plasma6-nm
Requires:       plasma6-workspace
Recommends:     bluedevil6
Recommends:     kwin6

%description
liquidshell is a basic Desktop Shell leveraging KDE Frameworks6 libraries.

%lang_package

%prep
%autosetup

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} %{name}.lang

%files lang -f %{name}.lang

%files
%doc README
%license COPYING
%{_datadir}/xsessions/liquidshell-session.desktop
%{_kf6_applicationsdir}/org.kde.liquidshell.desktop
%{_kf6_appstreamdir}/org.kde.liquidshell.appdata.xml
%{_kf6_bindir}/liquidshell
%{_kf6_bindir}/start_liquidshell
%{_kf6_iconsdir}/hicolor/48x48/apps/liquidshell.png
%{_kf6_notificationsdir}/liquidshell.notifyrc

%changelog
