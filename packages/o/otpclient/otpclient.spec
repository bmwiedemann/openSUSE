#
# spec file for package otpclient
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.3.1
Release:        0
Summary:        Simple GTK+ client for managing TOTP and HOTP
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://github.com/paolostivanin/%{name}
Source0:        https://github.com/paolostivanin/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/paolostivanin/%{uclname}/releases/download/v%{version}/v%{version}.tar.gz.asc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libbaseencode-devel >= 1.0.9
BuildRequires:  libcotp-devel >= 1.2.1
BuildRequires:  libgcrypt-devel >= 1.6.0
BuildRequires:  libjansson-devel >= 2.8.0
BuildRequires:  libpng16-devel >= 1.6.0
BuildRequires:  libzbar-devel >= 0.10.0
BuildRequires:  libzip-devel >= 1.1.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18

%description
Highly secure and easy to use GTK+ software for two-factor authentication
that supports both Time-based One-time Passwords (TOTP) and
HMAC-Based One-Time Passwords (HOTP).

%prep
%setup -q -n %{uclname}-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_GUI=ON \
    -DBUILD_CLI=ON
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r com.github.paolostivanin.%{uclname} System Security GTK GNOME

%files
%dir %{_datadir}/%{name}

%{_bindir}/%{name}
%{_bindir}/%{name}-cli

%{_datadir}/%{name}/otpclient.ui
%{_datadir}/%{name}/shortcuts.ui
%{_datadir}/applications/com.github.paolostivanin.%{uclname}.desktop
%{_datadir}/metainfo/com.github.paolostivanin.%{uclname}.appdata.xml

%{_datadir}/icons/hicolor/16x16/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/24x24/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/32x32/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/48x48/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/64x64/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/128x128/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/256x256/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/512x512/apps/com.github.paolostivanin.%{uclname}.png
%{_datadir}/icons/hicolor/scalable/apps/com.github.paolostivanin.OTPClient.svg

%changelog
