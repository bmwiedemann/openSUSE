#
# spec file for package rioterm
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Nicolas Lorin <androw95220@gmail.com>
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


Name:           rioterm
Version:        0.1.1
Release:        0
Summary:        A hardware-accelerated GPU terminal emulator powered by WebGPU
License:        MIT
URL:            https://raphamorim.io/rio/
Source0:        rio-%{version}.tar.zst
Source1:        vendor.tar.zst
#Requires:       rioterm-terminfo
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  freetype2-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python311
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)

%description
A hardware-accelerated GPU terminal emulator powered by WebGPU, focusing to run in desktops and browsers.

%package terminfo
Summary:        Terminfo for %{name}
Supplements:    (%{name})
BuildArch:      noarch

%description terminfo
The official terminfo for rioterm.

%prep
%setup -a1 -qn rio-%{version}

%build
%{cargo_build} --no-default-features --features=x11,wayland
#tic -e rio -x -o terminfo misc/rio.terminfo

%install
mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 target/release/rio %{buildroot}%{_bindir}/rio
#install -D -m 0644 terminfo/r/rio %{buildroot}/usr/share/terminfo/r/rio
install -D -m 0644 misc/rio.desktop %{buildroot}/%{_datadir}/applications/rio.desktop
install -D -m 0644 misc/logo.svg %{buildroot}/%{_datadir}/pixmaps/rio.svg

# install desktop file
%suse_update_desktop_file rio

%files
%license LICENSE
%{_bindir}/rio
%{_datadir}/applications/rio.desktop
%{_datadir}/pixmaps/rio.svg

#%files terminfo
#/usr/share/terminfo/r/rio

%changelog
