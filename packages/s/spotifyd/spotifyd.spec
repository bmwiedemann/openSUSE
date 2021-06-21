#
# spec file for package spotifyd
#
# Copyright (c) 2021 SUSE LLC
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


Name:           spotifyd
Version:        0.3.2
Release:        0
Summary:        Spotify client running as a UNIX daemon
Group:          Productivity/Multimedia/Sound/Players
License:        GPL-3.0-or-later
URL:            https://github.com/Spotifyd/spotifyd
Source0:        https://github.com/Spotifyd/spotifyd/archive/refs/tags/v%{version}.tar.gz#/spotifyd-%{version}.tar.gz
Source1:        vendor.tar.bz2
BuildRequires:  cargo
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  systemd-rpm-macros

%description
Spotifyd streams music just like the official client, but is more lightweight
and supports more platforms. Spotifyd also supports the Spotify Connect
protocol, which makes it show up as a device that can be controlled from
the official clients.

%prep
%setup -q -a1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
cargo build \
  --release \
  --locked %{?_smp_mflags} \
  --features alsa_backend,dbus_keyring,dbus_mpris,pulseaudio_backend

%install
cargo install \
  --no-track \
  --root=%{buildroot}%{_prefix} \
  --path . \
  --features alsa_backend,dbus_keyring,dbus_mpris,pulseaudio_backend

install -pm0755 -D target/release/spotifyd %{buildroot}%{_bindir}/spotifyd
install -pm0644 -D contrib/spotifyd.service %{buildroot}%{_unitdir}/spotifyd.service

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
%{_unitdir}/spotifyd.service
%{_bindir}/spotifyd

%changelog
