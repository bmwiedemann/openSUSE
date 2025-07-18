#
# spec file for package wbg
#
# Copyright (c) 2025 SUSE LLC
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


Name:           wbg
Version:        1.3.0
Release:        0
Summary:        Wallpaper application for layer-shell Wayland compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://codeberg.org/dnkl/wbg
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xb19964fbba09664cc81027ed5bbd4992c116573f
Source2:        %{name}.keyring
BuildRequires:  c_compiler
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
Wbg is a wallpaper setter for Wayland compositors that implement the
layer-shell protocol.

It takes a single argument, the image filename, which is displayed
scaled-to-fit on all monitors.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/wbg

%changelog
