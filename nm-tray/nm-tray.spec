#
# spec file for package nm-tray
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           nm-tray
Version:        0.4.3
Release:        0
Summary:        NetworkManager Tray applet
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/palinek/nm-tray
Source:         https://github.com/palinek/nm-tray/archive/%{version}.tar.gz
BuildRequires:  cmake >= 3.1.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       NetworkManager
Recommends:     %{name}-lang

%description
nm-tray is a simple NetworkManager front end with information icon residing in system tray (like nm-applet), but a pure Qt implementation.

%lang_package

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/applications
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

install -dm 0755 %{buildroot}/%{_sysconfdir}/xdg/autostart
cat > %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop <<-EOF
[Desktop Entry]
Name=LXQt Network Applet
GenericName=Network Management
Comment=LXQt panel applet to handle network connections
Icon=nm-device-wireless
Exec=nm-tray
Type=Application
Categories=Network;Monitor;
OnlyShowIn=LXQt;
X-LXQt-Need-Tray=true
EOF

%find_lang %{name} --with-qt

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%dir %{_prefix}%{_sysconfdir}
%dir %{_prefix}%{_sysconfdir}/xdg
%dir %{_prefix}%{_sysconfdir}/xdg/autostart
%{_prefix}%{_sysconfdir}/xdg/autostart/nm-tray-autostart.desktop
%{_datadir}/nm-tray/nm-tray.conf

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}

%changelog
