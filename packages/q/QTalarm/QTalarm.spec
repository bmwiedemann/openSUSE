#
# spec file for package QTalarm
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


%define  _name  qtalarm
Name:           QTalarm
Version:        2.3.2
Release:        0
Summary:        A handy alarm clock Program written in QT
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://random-hackery.net/page/qtalarm/
Source:         https://github.com/CountMurphy/QTalarm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
A handy alarm clock Program written in QT.
Features:
 * Up to 15 Customization alarms
 * Can wake up using the default sound, or any of audio / video
   file of your choosing.
 * Custom Date alarms

%prep
%setup -q

%build
%qmake5
%make_jobs

%install
install -Dm 0755 %{_name} %{buildroot}%{_bindir}/%{_name}
install -Dm 0644 Icons/*_Clock.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{_name}.png
install -Dm 0644 Icons/*_Clock24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{_name}.png
install -Dm 0644 Icons/*_Clock16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{_name}.png
%suse_update_desktop_file -c %{_name} "QT Alarm" "Alarm Clock" %{_name} %{_name} Utility Clock

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{_name}.??g

%changelog
