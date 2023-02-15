#
# spec file for package spotifyd
#
# Copyright (c) 2023 SUSE LLC
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


%define spotifyd_features alsa_backend,dbus_keyring,dbus_mpris,pulseaudio_backend
Name:           spotifyd
Version:        0.3.3
Release:        0
Summary:        Spotify client running as a UNIX daemon
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/Spotifyd/spotifyd
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rinstall
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openssl)

%description
Spotifyd streams music just like the official client, but is more lightweight
and supports more platforms. Spotifyd also supports the Spotify Connect
protocol, which makes it show up as a device that can be controlled from
the official clients.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build} --features %{spotifyd_features}

%install
install -pm0755 -D target/release/spotifyd %{buildroot}%{_bindir}/spotifyd
install -pm0644 -D contrib/spotifyd.service %{buildroot}%{_userunitdir}/spotifyd.service

%pre
%service_add_pre spotifyd.service

%post
%service_add_post spotifyd.service

%preun
%service_del_preun spotifyd.service

%postun
%service_del_postun spotifyd.service

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_userunitdir}/spotifyd.service
%{_bindir}/spotifyd

%changelog
