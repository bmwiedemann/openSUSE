#
# spec file for package wayshot
#
# Copyright (c) 2022 SUSE LLC
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

Name:           wayshot
Version:        1.1.2
Release:        0
Summary:        Screenshot tool for wlroots based compositors
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR MIT ) AND ( Apache-2.0 OR MIT ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND BSD-3-Clause AND ISC AND MIT AND Zlib AND BSD-2-Clause
Group:          Productivity/Graphics/Other
Url:            https://github.com/waycrate/wayshot
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.52.1
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots) >= 0.15.0

%description
A screenshot tool for wlroots based compositors implementing zwlr_screencopy_v1

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%{_bindir}/wayshot
%license LICENSE
%doc README.md

%changelog
