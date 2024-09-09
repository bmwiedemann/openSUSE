#
# spec file for package nm-tray
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


Name:           nm-tray
Version:        0.5.1
Release:        0
Summary:        NetworkManager Tray applet
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/palinek/nm-tray
Source:         https://github.com/palinek/nm-tray/archive/%{version}.tar.gz
BuildRequires:  cmake >= 3.1.0
BuildRequires:  pkgconfig
BuildRequires:  xdg-user-dirs
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
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
%{_prefix}%{_sysconfdir}/xdg/autostart/nm-tray-autostart.desktop
%{_datadir}/nm-tray/nm-tray.conf

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}

%changelog
