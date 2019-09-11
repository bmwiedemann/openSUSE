#
# spec file for package plasma-mycroft
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define qt_version 5.9.0
%define kf5_version 5.0

Name:           plasma-mycroft
Version:        0.1git~20190117T001945~41ba381
Release:        0
Summary:        Plasmoid for Mycroft AI
License:        GPL-2.0-only AND LGPL-2.0-only AND Apache-2.0
Group:          System/GUI/KDE
Url:            https://cgit.kde.org/plasma-mycroft.git
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-scripts.patch
Patch1:         fix-config-install-dir.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  python3-dbus-python
BuildRequires:  python3-msm
BuildRequires:  python3-qt5
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= %{qt_version}
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5WebSockets)
Requires:       mycroft-core
Requires:       plasma5-desktop
Requires:       python3-dbus-python
Requires:       python3-qt5

%description
Mycroft AI Plasmoid for KDE Plasma 5 Desktop

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
chmod +x %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/startservice.sh
chmod +x %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/stopservice.sh
chmod +x %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/pkgstartservice.sh
chmod +x %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/pkgstopservice.sh
ln -sf /usr/bin/msm %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.mycroftplasmoid/contents/code/msm.sh
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%license COPYING COPYING.LGPL COPYING.APACHE2
%{_datadir}/plasma/plasmoids
%{_libdir}/qt5/qml/org/kde/private/mycroftplasmoid
%{_datadir}/icons/*
%{_datadir}/knotifications5/mycroftPlasmoid.notifyrc
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.mycroftplasmoid.desktop
%{_datadir}/metainfo/org.kde.plasma.mycroftplasmoid.appdata.xml
%{_docdir}/plasma-mycroft
%dir %{_datadir}/metainfo

%changelog
