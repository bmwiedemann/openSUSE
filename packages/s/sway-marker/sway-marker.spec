#
# spec file for package sway-marker
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


%define binname nvim-gtk
Name:           sway-marker
Version:        0.3~0
Release:        0
Summary:        Simple popup for using marks in Sway
License:        GPL-3.0-only
URL:            https://github.com/ilyazzz/sway-marker
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(pango)

%description
This allows you to use vim-like marks to switch between different
containers (windows) in sway easily.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
