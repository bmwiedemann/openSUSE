#
# spec file for package kshutdown
#
# Copyright (c) 2020 SUSE LLC
# Copyright © 2010 Lubos Lunak <llunak@novell.com>
# Copyright © 2011 Buschmann <buschmann23@opensuse.org>
# Copyright © 2014–2019 Markus S <kamikazow@opensuse.org>
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


Name:           kshutdown
Version:        5.2
Release:        0
Summary:        Graphical shutdown utility
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://kshutdown.sourceforge.io/
Source0:        %{name}-source-%{version}.zip
BuildRequires:  extra-cmake-modules
Requires(post):   hicolor-icon-theme
Requires(post):   update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
BuildRequires:  unzip
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KShutdown is a graphical shutdown utility that works
with many Desktop Environments. It allows you to turn off
or suspend a computer at a specified time. It features
various time and delay options, command-line support,
and notifications.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kf5 -d build -- -DKS_KF5=ON -DCMAKE_CXX_STANDARD=14
%make_jobs

%install
%kf5_makeinstall -C build

%suse_update_desktop_file %{name}

%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog LICENSE TODO
%{_kf5_bindir}/%{name}
%{_kf5_applicationsdir}/%{name}.desktop
%{_kf5_notifydir}/%{name}.notifyrc
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
