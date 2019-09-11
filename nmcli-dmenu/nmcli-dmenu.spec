#
# spec file for package nmcli-dmenu
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           nmcli-dmenu
Version:        1.0.0
Release:        0
Summary:        Control NetworkManager via dmenu
License:        MIT
Group:          Productivity/Networking/Other
Url:            http://github.com/firecat53/nmcli-dmenu
Source:         https://github.com/firecat53/%{name}/archive/%{version}.tar.gz
BuildRequires:  update-desktop-files
Requires:       NetworkManager
Requires:       dmenu
Recommends:     NetworkManager-gnome
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Small script to manage NetworkManager connections with dmenu instead of
nm-applet. It can connect to existing NetworkManager wifi or wired connections,
connect to new wifi connections (requests passphrase if required), connect to
existing VPN connections, enable/disable networking, launch
nm-connection-editor GUI.

%prep
%setup -q

%build

%install
install -Dm0755 nmcli_dmenu %{buildroot}%{_bindir}/nmcli_dmenu
%suse_update_desktop_file -i nmcli_dmenu System

%files
%defattr(-,root,root)
%doc README.rst LICENSE.txt config.ini.example
%{_bindir}/nmcli_dmenu
%{_datadir}/applications/nmcli_dmenu.desktop

%changelog
