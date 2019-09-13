#
# spec file for package way-cooler
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           way-cooler
Version:        0.8.1
Release:        0
Summary:        Customizeable Wayland compositor written in Rust
License:        MIT
Group:          System/GUI/Other
Url:            http://way-cooler.org/
Source0:        https://github.com/way-cooler/way-cooler/archive/v%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  gdk-pixbuf-devel >= 2.26
BuildRequires:  git
BuildRequires:  libcurl-devel
BuildRequires:  lua53-devel
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlc)
BuildRequires:  pkgconfig(xkbcommon)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Way Cooler is a customizable tiling window manager written in Rust for Wayland and configurable using Lua.

%prep
%setup -q
%setup -q -D -T -a 1
mkdir cargo-home
cat >cargo-home/config <<EOF

[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export CARGO_HOME=`pwd`/cargo-home/
RUST_BACKTRACE=1 cargo build --release %{?_smp_mflags}

%install
mkdir build
export CARGO_HOME=`pwd`/cargo-home/
cargo install --root=build
install -Dm0755 build/bin/way-cooler	%{buildroot}%{_bindir}/way-cooler
install -Dm644 config/init.lua			%{buildroot}%{_sysconfdir}/way-cooler/init.lua
install -Dm644 way-cooler.desktop		%{buildroot}%{_datadir}/wayland-sessions/way-cooler.desktop

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/way-cooler
%dir %{_sysconfdir}/way-cooler
%config %{_sysconfdir}/way-cooler/init.lua
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/way-cooler.desktop

%changelog
