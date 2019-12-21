#
# spec file for package ktimetracker
#
# Copyright (c) 2019 SUSE LLC
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


%bcond_without lang
Name:           ktimetracker
Version:        5.0.0
Release:        0
Summary:        Personal Time Tracker
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://userbase.kde.org/KTimeTracker
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus) >= 5.10.0
BuildRequires:  cmake(Qt5Gui) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
BuildRequires:  cmake(Qt5Xml) >= 5.10.0

%description
KTimeTracker tracks time spent on various tasks.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
# install application icon (kde#415387)
for i in 16 22 32 48 64 128
do
  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/${i}x${i}/apps
  cp icons/app/${i}-apps-ktimetracker.png %{buildroot}%{_kf5_iconsdir}/hicolor/${i}x${i}/apps/ktimetracker.png
done
%suse_update_desktop_file -r org.kde.ktimetracker Qt KDE Utility X-KDE-Utilities-PIM TimeUtility

%if %{with lang}
%find_lang %{name}
%{kf5_find_htmldocs}
%endif

%files
%license COPYING COPYING.DOC
%doc README ChangeLog.md
%doc %lang(en) %{_kf5_htmldir}/en/ktimetracker/
%{_kf5_applicationsdir}/org.kde.ktimetracker.desktop
%{_kf5_appstreamdir}/org.kde.ktimetracker.appdata.xml
%{_kf5_bindir}/ktimetracker
%{_kf5_dbusinterfacesdir}/org.kde.ktimetracker.ktimetracker.xml
%{_kf5_iconsdir}/hicolor/*/apps/ktimetracker.png

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING COPYING.DOC
%endif

%changelog
