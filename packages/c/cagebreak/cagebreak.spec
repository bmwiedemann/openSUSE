#
# spec file for package cagebreak
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


Name:           cagebreak
Version:        2.3.1
Release:        0
Summary:        A Wayland Tiling Compositor Inspired by Ratpoison
License:        MIT
URL:            https://github.com/project-repo/cagebreak
Source0:        %{url}/releases/download/%{version}/release_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/release_%{version}.tar.gz.sig#/%{name}-%{version}.tar.gz.sig
Source10:       %{name}.keyring
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  scdoc
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildConflicts: pkgconfig(wlroots) >= 0.18.0
BuildRequires:  pkgconfig(wlroots) >= 0.17.0

%description
Cagebreak provides a ratpoison-inspired, cage-based, tiling Wayland
compositor.

%prep
%autosetup -p1 -n cagebreak

%build
%meson -Dman-pages=true -Dxwayland=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md FAQ.md Changelog.md
%{_bindir}/cagebreak
%dir %{_sysconfdir}/xdg/cagebreak
%config %{_sysconfdir}/xdg/cagebreak/config
%{_mandir}/man?/cagebreak*%{?ext_man}

%changelog
