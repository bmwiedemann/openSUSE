#
# spec file for package wdisplays
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


Name:           wdisplays
Version:        1.1.3
Release:        0%{?dist}
Summary:        GUI display configurator for wlroots compositors

License:        GPL-3.0-or-later
URL:            https://github.com/artizirk/wdisplays
Source:         https://github.com/artizirk/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libepoxy-devel
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

Requires:       hicolor-icon-theme

%description
wdisplays is a graphical application for configuring displays in
Wayland compositors. It requires a compositor with the
wlr-output-management-unstable-v1 protocol, e.g. sway.
This program can perform adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot}

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --set-icon %{name} \
    --set-key=Terminal --set-value=false \
    --remove-key=Version \
    --add-category=Settings --add-category=HardwareSettings \
    %{buildroot}/%{_datadir}/applications/network.cycles.%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*

%doc README.md

%license LICENSES/*

%changelog
