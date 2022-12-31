#
# spec file for package ncspot
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           ncspot
Version:        0.12.0
Release:        0
Summary:        Ncurses Spotify client
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/hrkfdn/ncspot
Source:         https://github.com/hrkfdn/ncspot/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo >= 1.58
BuildRequires:  libpulse-devel
BuildRequires:  libxcb-devel
BuildRequires:  ncurses5-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.61
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1) >= 1.6

%description
Cross-platform ncurses Spotify client written in Rust, inspired
by ncmpc and the likes.

%prep
%autosetup -p 1 -a 1
install -D -m 0644 %{SOURCE2} .cargo/config

%build
# HACK: https://github.com/jeaye/ncurses-rs/issues/191
export NCURSES_RS_RUSTC_FLAGS="-L /usr/lib64/ncurses5"
cargo build --release --locked %{?_smp_mflags}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .
install -Dm 0644 misc/ncspot.desktop %{buildroot}/%{_datadir}/applications/ncspot.desktop
%suse_update_desktop_file ncspot

%files
%license LICENSE
%doc README.md
%{_bindir}/ncspot
%{_datadir}/applications/ncspot.desktop

%changelog
