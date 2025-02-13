#
# spec file for package tail-tray
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tail-tray
Version:        latest
Release:        0
Summary:        Tailscale tray menu and UI for the KDE Plasma Desktop
License:        GPL-3.0-only
URL:            https://github.com/SneWs/tail-tray
Source:         %{name}-%{version}.tar.gz
BuildRequires:  clang
BuildRequires:  cmake >= 3.21
%if 0%{?suse_version} < 1600
BuildRequires:  gcc14-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt6Core) >= 6.7
BuildRequires:  cmake(Qt6Linguist) >= 6.7
BuildRequires:  cmake(Qt6Network) >= 6.7
BuildRequires:  cmake(Qt6Tools) >= 6.7
BuildRequires:  cmake(Qt6Widgets) >= 6.7
BuildRequires:  pkgconfig(openssl)
Requires:       tailscale
Suggests:       davfs2

%description
Tailscale tray menu and UI for Plasma Desktop

Features

- Control your Tailscale connection from the tray
- Show IPs
- Show current connection status of your devices
- Overview of your network and network status
- Set and change your Tailscale exit node
- Proper multi account handling
- Tail drive support - Working with davfs2 support + additional help setting up
  davfs2 and mounting etc
- Send files to any device on your Tailnet directly from the tray menu
- Get notified and receive files from any device on your Tailnet to a
  pre-defined location on disk

%prep
%autosetup

%build
%if 0%{?suse_version} < 1600
export CC="/usr/bin/gcc14"
export CXX="/usr/bin/g++-14"
%endif
%cmake
%cmake_build

%install
%cmake_install

sed -i 's#/usr/local/bin/tail-tray#/usr/bin/tail-tray#g' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#Networking;##g' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#VPN;##g' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#Internet;##g' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/tailscale.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}

%changelog
