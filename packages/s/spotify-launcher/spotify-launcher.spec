#
# spec file for package spotify-launcher
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


Name:           spotify-launcher
Version:        0.6.0
Release:        0
Summary:        Client for spotify's apt repository written in Rust
License:        Apache-2.0 OR MIT
URL:            https://github.com/kpcyrd/spotify-launcher
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  rust >= 1.70
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_tier1_arches}
Requires:       sequoia-sqv
# Spotify dependencies
Requires:       libayatana-appindicator3-1
Requires:       desktop-file-utils
Requires:       libSM6
Requires:       libasound2 >= 1.0.14
Requires:       libatomic1
Requires:       mozilla-nss
Requires:       zenity

%description
Client for spotify's apt repository written in Rust

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

install -Dm644 %{_builddir}/%{name}-%{version}/data/pubkey_6224F9941A8AA6D1.gpg %{buildroot}%{_datadir}/%{name}/keyring.pgp

install -Dm644 %{_builddir}/%{name}-%{version}/contrib/%{name}.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 %{_builddir}/%{name}-%{version}/contrib/icons/spotify-linux-512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{_builddir}/%{name}-%{version}/contrib/%{name}.conf -t %{buildroot}%{_sysconfdir}

for size in 22 24 32 48 64 128 256 512; do
  install -Dm644 %{_builddir}/%{name}-%{version}/contrib/icons/spotify-linux-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%fdupes %{buildroot}%{_datadir}/pixmaps/ %{buildroot}%{_datadir}/icons/hicolor/

%files
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%config %{_sysconfdir}/%{name}.conf
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
