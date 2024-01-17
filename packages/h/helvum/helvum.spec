#
# spec file for package helvum
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


%define app_id org.pipewire.Helvum
Name:           helvum
Version:        0.5.1
Release:        0
Summary:        A GTK patchbay for pipewire
License:        GPL-3.0-only AND ( (MIT OR Apache-2.0) AND Unicode-DFS-2016 ) AND ( Apache-2.0 OR MIT ) AND ( Unlicense OR MIT ) AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND ISC AND MIT AND
URL:            https://gitlab.freedesktop.org/pipewire/helvum
Source:         https://gitlab.freedesktop.org/pipewire/helvum/uploads/f523a2c71046fb21a7584fca80fc0ee9/%{name}-%{version}.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.4.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.3
BuildRequires:  pkgconfig(libpipewire-0.3)
ExclusiveArch:  %{rust_tier1_arches}

%description
Helvum is a GTK-based patchbay for pipewire, inspired by the JACK tool catia.

%prep
%setup -q

%build
%{cargo_build}

%install
%{cargo_install}
sed 's/@icon@/%{app_id}/g' data/%{app_id}.desktop.in > data/%{app_id}.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/applications/ data/%{app_id}.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps data/icons/%{app_id}.svg
install -D -m0644 -t %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps data/icons/%{app_id}-symbolic.svg

%files
%{_bindir}/helvum
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/

%changelog
