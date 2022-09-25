#
# spec file for package gnome-shell-extension-pop-shell
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define extension_basedir %{_datadir}/gnome-shell/extensions
%define extension_name    pop-shell@system76.com
%define extension_dir     %{extension_basedir}/%{extension_name}
%define upstream_name shell
Name:           gnome-shell-extension-pop-shell
Version:        1.2.0
Release:        0
Summary:        Gnome Shell Extension to Auto Tiling
License:        GPL-3.0-only
URL:            https://github.com/pop-os/shell
Source:         https://github.com/pop-os/shell/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Source1:        series
Patch0:         0143b0b5eb14291cbd9e0b8328eeec93c4871ba9.patch
Patch1:         4520e7813dcbca57ff19cba68085f5d8adf4785e.patch
BuildRequires:  gnome-shell >= 3.36
BuildRequires:  gobject-introspection
BuildRequires:  typescript >= 3.8
Requires:       gnome-shell >= 3.36
BuildArch:      noarch

%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows. The core feature of Pop Shell is
the addition of advanced tiling window management — a feature that has been
highly-sought within our community. For many — ourselves included — i3wm has
become the leading competitor to the GNOME desktop.

Tiling window management in GNOME is virtually nonexistent, which makes the
desktop awkward to interact with when your needs exceed that of two windows at
a given time. Luckily, GNOME Shell is an extensible desktop with the
foundations that make it possible to implement a tiling window manager on top
of the desktop.

Therefore, we see an opportunity here to advance the usability of the GNOME
desktop to better accomodate the needs of our community with Pop Shell.
Advanced tiling window management is a must for the desktop, so we've merged
i3-like tiling window management with the GNOME desktop for the best of both
worlds.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%make_build

%install
%make_install

install -D -d -m 0755 \
  %{buildroot}%{_datadir}/gnome-control-center/keybindings \
  %{buildroot}%{_datadir}/glib-2.0/schemas
install -m 0644 keybindings/* %{buildroot}%{_datadir}/gnome-control-center/keybindings

mv    %{buildroot}%{_datadir}/gnome-shell/extensions/pop-shell@system76.com/schemas/org.gnome.shell.extensions.pop-shell.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas
rm -r %{buildroot}%{_datadir}/gnome-shell/extensions/pop-shell@system76.com/schemas/

%files
%doc *.md
%license LICENSE
%{extension_dir}
%{_prefix}/lib/pop-shell
%{_datadir}/gnome-control-center/keybindings/*
%{_datadir}/glib-2.0/schemas/*

%changelog
