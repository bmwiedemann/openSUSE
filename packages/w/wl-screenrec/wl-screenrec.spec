#
# spec file for package wl-screenrec
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


Name:           wl-screenrec
Version:        0.1.0
License:        Apache-2.0
Release:        0
Summary:        High performance hardware accelerated wlroots screen recorder
Group:          Productivity/Graphics/Other
URL:            https://github.com/russelltg/wl-screenrec
Source0:        https://github.com/russelltg/wl-screenrec/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  ffmpeg-devel
BuildRequires:  libdrm-devel
BuildRequires:  llvm-devel
BuildRequires:  llvm-gold
BuildRequires:  pkg-config
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel

%description
High performance screen recorder for wlroots Wayland.

Uses dma-buf transfers to get surface, and uses the GPU to do both the pixel format conversion and the encoding, meaning the raw video data never touches the CPU, leaving it free to run your applications.

%prep
%autosetup -a1
mkdir -p .cargo/
cp cargo_config .cargo/config

%build
export CC=clang
export CXX=clang++
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%{cargo_build} --all-features

%install
export CC=clang
export CXX=clang++
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%{cargo_install} --all-features

%files
%{_bindir}/wl-screenrec
%license LICENSE
%doc *.md

%changelog
