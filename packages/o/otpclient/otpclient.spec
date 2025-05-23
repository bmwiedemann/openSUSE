#
# spec file for package otpclient
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


%define uclname OTPClient
Name:           otpclient
Version:        4.1.0
Release:        0
Summary:        Simple GTK+ client for managing TOTP and HOTP
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://github.com/paolostivanin/%{name}
Source0:        https://github.com/paolostivanin/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/paolostivanin/%{uclname}/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:        otpclient.keyring
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libayatana-appindicator3-devel
BuildRequires:  libcotp-devel >= 3.0.0
BuildRequires:  libgcrypt-devel >= 1.10.1
BuildRequires:  libjansson-devel >= 2.12.0
BuildRequires:  libpng16-devel >= 1.6.30
BuildRequires:  libprotobuf-c-devel >= 1.3.0
BuildRequires:  libsecret-devel >= 0.20
BuildRequires:  libuuid-devel >= 2.34.0
BuildRequires:  libzbar-devel >= 0.20.0
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel >= 3.6.0
BuildRequires:  qrencode-devel >= 4.0.2
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24

%description
Highly secure and easy to use GTK+ software for two-factor authentication
that supports both Time-based One-time Passwords (TOTP) and
HMAC-Based One-Time Passwords (HOTP).

%prep
%autosetup -p1 -n %{uclname}-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_GUI=ON \
    -DBUILD_CLI=ON \
    -DENABLE_MINIMIZE_TO_TRAY=ON
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r com.github.paolostivanin.%{uclname} System Security GTK GNOME

%files
%dir %{_datadir}/%{name}

%{_bindir}/%{name}
%{_bindir}/%{name}-cli

%{_datadir}/%{name}/otpclient.ui
%{_datadir}/%{name}/add_popover.ui
%{_datadir}/%{name}/settings_popover.ui
%{_datadir}/%{name}/shortcuts.ui
%{_datadir}/%{name}/security_settings.ui
%{_datadir}/applications/com.github.paolostivanin.%{uclname}.desktop
%{_datadir}/metainfo/com.github.paolostivanin.%{uclname}.appdata.xml

%{_mandir}/man1/otpclient-cli.1.gz
%{_mandir}/man1/otpclient.1.gz

%{_datadir}/icons/hicolor/scalable/apps/com.github.paolostivanin.OTPClient-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/com.github.paolostivanin.OTPClient.svg

%changelog
