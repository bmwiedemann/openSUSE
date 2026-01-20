#
# spec file for package qt6gtk2
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


%define qt_version 6.0.0
Name:           qt6gtk2
Version:        0.7
Release:        0
Summary:        Qt6 Gtk2 Style Plugin
License:        GPL-2.0-or-later
URL:            https://www.opencode.net/trialuser/qt6gtk2
Source:         https://www.opencode.net/trialuser/qt6gtk2/-/archive/%{version}/qt6gtk2-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt_version}
BuildRequires:  qt6-gui-private-devel >= %{qt_version}
BuildRequires:  qt6-widgets-private-devel >= %{qt_version}
BuildRequires:  pkgconfig(libudev)
%requires_eq    libQt6Core6
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)

%description
Qt 6 plugin for better integration with gtk-based desktop enviroments.

%prep
%autosetup -p1

%build
%qmake6
%make_build

%install
%qmake6_install

%ldconfig_scriptlets

%files
%dir %{_qt6_pluginsdir}/platformthemes/
%{_qt6_pluginsdir}/platformthemes/*.so
%dir %{_qt6_pluginsdir}/styles/
%{_qt6_pluginsdir}/styles/*.so

%changelog
