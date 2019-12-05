#
# spec file for package neovim-gtk
#
# Copyright (c) 2019 SUSE LLC
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


%define icondir %{_datadir}/icons
%define binname nvim-gtk

Name:           neovim-gtk
Version:        0.2.0+git.1575188169.31fd179
Release:        0
Summary:        GTK UI for Neovim
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://github.com/daa84/neovim-gtk
Source0:        neovim-gtk-%{version}.tar.xz
Source1:        neovim-gtk-vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pango-devel

%description
GTK UI for Neovim written in Rust using gtk-rs bindings. With ligatures
support.

%prep
%setup -q -a1
%autopatch -p1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "./vendor"
EOF

%build
cargo build --release

%install
# %%makeinstall PREFIX=%%{_prefix}
mkdir -p %{buildroot}%{_datadir}/%{binname}/
cp -p -r runtime %{buildroot}%{_datadir}/%{binname}/
install -p -m 0644 -D desktop/org.daa.NeovimGtk.desktop \
    %{buildroot}%{_datadir}/applications/org.daa.NeovimGtk.desktop
install -p -m 0644 -D desktop/org.daa.NeovimGtk_128.png \
    %{buildroot}%{icondir}/hicolor/128x128/apps/org.daa.NeovimGtk.png
install -p -m 0644 -D desktop/org.daa.NeovimGtk_48.png \
    %{buildroot}%{icondir}/hicolor/48x48/apps/org.daa.NeovimGtk.png
install -p -m 0644 -D desktop/org.daa.NeovimGtk.svg \
    %{buildroot}%{icondir}/hicolor/scalable/apps/org.daa.NeovimGtk.svg
install -p -m 0644 -D desktop/org.daa.NeovimGtk-symbolic.svg \
    %{buildroot}%{icondir}/hicolor/symbolic/apps/org.daa.NeovimGtk-symbolic.svg

install -p -m 0755 -D target/release/nvim-gtk \
    %{buildroot}%{_bindir}/nvim-gtk

rm -vf %%{buildroot}%%{_prefix}/.crates.toml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{binname}
%{_datadir}/%{binname}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/org.daa.NeovimGtk.desktop

%changelog
