#
# spec file for package rioterm
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.2.35
Release:        0
Summary:        A hardware-accelerated GPU terminal emulator powered by WebGPU
License:        MIT
URL:            https://raphamorim.io/rio/
Source0:        rio-%{version}.tar.zst
Source1:        vendor.tar.zst
Source99:       %{name}-rpmlintrc
%if 0%{?suse_version} <= 1500
Group:          System/X11/Terminals
BuildRequires:  gcc14
BuildRequires:  gcc14-c++
BuildRequires:  libstdc++-devel
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

%description
A hardware-accelerated GPU terminal emulator powered by WebGPU, focusing to run in desktops and browsers.

%prep
%setup -a1 -qn rio-%{version}

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-14
export CXX=g++-14
%endif
%{cargo_build} --no-default-features --features=x11,wayland

%install
mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 target/release/rio %{buildroot}%{_bindir}/rio
install -D -m 0644 misc/rio.desktop %{buildroot}/%{_datadir}/applications/rio.desktop
install -D -m 0644 misc/logo.svg %{buildroot}/%{_datadir}/pixmaps/rio.svg

%files
%license LICENSE
%{_bindir}/rio
%{_datadir}/applications/rio.desktop
%{_datadir}/pixmaps/rio.svg

%changelog
