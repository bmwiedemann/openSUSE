#
# spec file for package kshutdown
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        6.2
Release:        0
Summary:        Graphical shutdown utility
License:        GPL-2.0-or-later
URL:            https://kshutdown.sourceforge.io/
Source0:        https://downloads.sourceforge.net/project/kshutdown/KShutdown/%{version}/%{name}-source-%{version}.zip
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-tools
BuildRequires:  unzip
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6XmlGui)

%description
KShutdown is a graphical shutdown utility that works
with many Desktop Environments. It allows you to turn off
or suspend a computer at a specified time. It features
various time and delay options, command-line support,
and notifications.

%prep
%autosetup -p1

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_applicationsdir}/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc ChangeLog README.html TODO
%{_kf6_bindir}/%{name}
%{_kf6_applicationsdir}/%{name}.desktop
%{_kf6_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
