#
# spec file for package niri
#
# Copyright (c) 2025 mantarimay
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


%bcond_without test
Name:           niri
Version:        25.05.1
Release:        0
Summary:        Scrollable-tiling Wayland compositor
License:        GPL-3.0-or-later
URL:            https://github.com/YaLTeR/niri
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}-vendored-dependencies.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  pango-devel
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80.0
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xkbcommon)
# Portal implementations used by niri
Recommends:     xdg-desktop-portal-gtk
Recommends:     gnome-keyring
Recommends:     polkit-gnome
Recommends:     xdg-desktop-portal-gnome
# Recommended utilities, bound in the default config
Recommends:     alacritty
Recommends:     fuzzel
Recommends:     swaylock
Recommends:     waybar
# Recommended utilities
Recommends:     swaybg
Recommends:     mako
Recommends:     xwayland-satellite

%description
A scrollable-tiling Wayland compositor.

Windows are arranged in columns on an infinite strip going to the right.
Opening a new window never causes existing windows to resize.

%prep
%autosetup -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -Dm755 -t %{buildroot}%{_bindir} target/release/%{name}
install -Dm755 -t %{buildroot}%{_bindir} resources/niri-session
install -Dm644 -t %{buildroot}%{_datadir}/wayland-sessions resources/niri.desktop
install -Dm644 -t %{buildroot}%{_datadir}/xdg-desktop-portal resources/niri-portals.conf
install -Dm644 -t %{buildroot}%{_userunitdir} resources/niri{.service,-shutdown.target}

comp="target/release/%{name} completions"
$comp bash > "target/release/%{name}.bash"
$comp fish > "target/release/%{name}.fish"
$comp zsh > "target/release/_%{name}"

install -Dm644 target/release/%{name}.bash -t \
    %{buildroot}%{_datadir}/bash-completion/completions
install -Dm644 target/release/%{name}.fish -t \
    %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 target/release/_%{name} -t \
    %{buildroot}%{_datadir}/zsh/site-functions

%if %{with test}
%check
%cargo_test -- --workspace --exclude niri-visual-tests
%endif

%files
%license LICENSE
%doc README.md resources/default-config.kdl wiki
%{_bindir}/niri
%{_bindir}/niri-session
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/niri.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/niri-portals.conf
%{_userunitdir}/niri.service
%{_userunitdir}/niri-shutdown.target
%{_datadir}/bash-completion/completions
%{_datadir}/fish
%{_datadir}/zsh

%changelog
