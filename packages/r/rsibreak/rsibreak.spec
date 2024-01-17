#
# spec file for package rsibreak
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


%define base_ver 0.12
%bcond_without released
Name:           rsibreak
Version:        0.12.15
Release:        0
Summary:        Repetetive Strain Injury recovery and prevention assistance utility
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://apps.kde.org/rsibreak
Source0:        https://download.kde.org/stable/rsibreak/%{base_ver}/rsibreak-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/rsibreak/%{base_ver}/rsibreak-%{version}.tar.xz.sig
Source2:        rsibreak.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.79.0
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus) >= 5.10.0
BuildRequires:  cmake(Qt5Test) >= 5.10.0
Requires:       hicolor-icon-theme
Recommends:     %{name}-lang = %{version}
Obsoletes:      %{name}-doc < %{version}
# REMOVE AFTER Leap 42.1 is out of scope
Provides:       kde4-rsibreak = %{version}
Obsoletes:      kde4-rsibreak < %{version}

%description
Repetitive Strain Injury is an illness which can occur as a result of
working with a mouse and keyboard. This utility can be used to remind
you to take a break now and then.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -G "RSI Prevention" org.kde.rsibreak Qt KDE TimeUtility
%if %{with released}
%find_lang %{name} --all-name
%{kf5_find_htmldocs}
%endif
%fdupes -s %{buildroot}%{_kf5_sharedir}

%if %{with released}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%doc AUTHORS ChangeLog NEWS
%doc %{_kf5_htmldir}/en/
%{_kf5_applicationsdir}/org.kde.rsibreak.desktop
%{_kf5_appstreamdir}/org.kde.rsibreak.appdata.xml
%{_kf5_bindir}/rsibreak
%{_kf5_configdir}/autostart/rsibreak_autostart.desktop
%{_kf5_dbusinterfacesdir}/org.rsibreak.rsiwidget.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_notifydir}/rsibreak.notifyrc

%changelog
