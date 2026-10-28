#
# spec file for package vectorcraft
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           vectorcraft
Version:        0.17.0
Release:        0
Summary:        Open-source vector illustration app
# Legal-Review-Notice: license audit 0.17.0, vendor-cratesio tag with locked
# offline build of vectorcraft plus vectorcraft-cli only. Upstream is MIT OR
# Apache-2.0. Linked third-party code adds BSD-2-Clause (arrayref),
# BSD-3-Clause (alloc-no-stdlib, brotli, tiny-skia and others), ISC
# (libloading), OFL-1.1 plus Ubuntu-font-1.0 (epaint default fonts, also
# shipped under assets/fonts), IJG (jpeg-encoder), Unicode-3.0 (icu and
# unicode-ident), Zlib (foldhash, zlib-rs). sctk-adwaita (MIT, Wayland
# window controls) is built without its title-font features, so its
# Cantarell font is not linked. Linked code has no MPL, LGPL, GPL, EPL,
# CDDL or CC-BY-SA; the vendor set carries colored (MPL-2.0) only as a
# dev-dependency of egui_kittest, never built. self_cell offers Apache-2.0
# OR GPL-2.0-only and is used under the Apache-2.0 option. r-efi offers
# MIT OR Apache-2.0 OR LGPL-2.1-or-later (MIT chosen). BSL-1.0, Unlicense,
# 0BSD and LLVM-exception appear only as OR alternatives alongside Apache
# or MIT and are not the chosen option. Trademarked ArtCraft marks under
# docs/brand are excluded from the tarball and never installed.
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND IJG AND ISC AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/vectorcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-cratesio.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
# wgpu GPU backend: Vulkan preferred, EGL fallback.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
# winit keyboard handling.
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     mesa-vulkan-drivers
Recommends:     vectorcraft-cli
Recommends:     xdg-desktop-portal
Recommends:     libX11.so.6()(64bit)
Recommends:     libXcursor.so.1()(64bit)
Recommends:     libXi.so.6()(64bit)
Recommends:     libXrandr.so.2()(64bit)
Recommends:     libwayland-client.so.0()(64bit)
ExclusiveArch:  %{rust_tier1_arches}

%description
Open-source, native vector illustration app: pen, shape and brush tools,
fills, strokes, gradients, live effects, artboards, type, and SVG plus PDF
open and save.

This package provides the desktop application; the companion vectorcraft-cli
subpackage provides the headless command runner and opt-in MCP server.

%package -n vectorcraft-cli
Summary:        Headless VectorCraft command runner and MCP server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND IJG AND ISC AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n vectorcraft-cli
Headless VectorCraft command runner: build, convert and inspect vector
documents from scripts and CI, plus an opt-in MCP server for agents.

%prep
%autosetup -p1 -a1
# Trademarked ArtCraft marks must never ship: belt-and-braces removal even
# though tar_scm already excludes docs/brand from the tarball.
rm -rf docs/brand
# Upstream metainfo declares the app icon as stock; it is a cached hicolor
# icon, otherwise appstream validation fails.
sed -i 's|<icon type="stock">ai.storyteller.vectorcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.vectorcraft.png</icon>|' packaging/linux/ai.storyteller.vectorcraft.metainfo.xml.in

%build
%limit_build -m 2000
# CRAFT_FONTS_DIR stays unset: use the bundled Latin fonts plus system
# fallback instead of embedding the craft-fonts checkout. Cargo.lock is
# committed upstream. The cargo build macro already passes offline mode;
# only add the locked flag.
%{cargo_build} --locked -p vectorcraft -p vectorcraft-cli

%install
install -D -m 0755 target/release/vectorcraft %{buildroot}%{_bindir}/vectorcraft
install -D -m 0755 target/release/vectorcraft-cli %{buildroot}%{_bindir}/vectorcraft-cli
install -D -m 0644 packaging/linux/ai.storyteller.vectorcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.vectorcraft.desktop
install -D -m 0644 packaging/linux/ai.storyteller.vectorcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.vectorcraft.xml
mkdir -p %{buildroot}%{_datadir}/metainfo
# Keep date command format literals unbraced: the cleaner would mistake them
# for RPM macros.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/$(date -u +%Y-%m-%d)/g" packaging/linux/ai.storyteller.vectorcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.vectorcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 NOTICE %{buildroot}%{_docdir}/%{name}/
install -m 0644 ASSETS.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 LICENSE-MIT LICENSE-APACHE %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/fonts/OFL-*.txt %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/icons/LICENSE-lucide.txt %{buildroot}%{_docdir}/%{name}/
install -d -m 0755 %{buildroot}%{_docdir}/vectorcraft-cli
ln -s ../vectorcraft/README.md %{buildroot}%{_docdir}/vectorcraft-cli/README.md
ln -s ../vectorcraft/NOTICE %{buildroot}%{_docdir}/vectorcraft-cli/NOTICE
ln -s ../vectorcraft/ASSETS.md %{buildroot}%{_docdir}/vectorcraft-cli/ASSETS.md
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.vectorcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.vectorcraft.metainfo.xml
%{buildroot}%{_bindir}/vectorcraft-cli --version
%{buildroot}%{_bindir}/vectorcraft-cli run --cmd file.new --params '{"width":200,"height":100}' --cmd shape.ellipse --params '{"x":10,"y":10,"width":80,"height":60}' --export /tmp/vectorcraft-check.svg > /dev/null
grep -q svg /tmp/vectorcraft-check.svg
%{buildroot}%{_bindir}/vectorcraft --version || %{buildroot}%{_bindir}/vectorcraft --help | head -n 5

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE-APACHE
%license %{_docdir}/%{name}/LICENSE-MIT
%license %{_docdir}/%{name}/OFL-*.txt
%license %{_docdir}/%{name}/LICENSE-lucide.txt
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/NOTICE
%doc %{_docdir}/%{name}/ASSETS.md
%{_bindir}/vectorcraft
%{_datadir}/applications/ai.storyteller.vectorcraft.desktop
%{_datadir}/metainfo/ai.storyteller.vectorcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.vectorcraft.xml
%{_datadir}/icons/hicolor/*

%files -n vectorcraft-cli
%{_bindir}/vectorcraft-cli
%dir %{_docdir}/vectorcraft-cli
%{_docdir}/vectorcraft-cli/*

%changelog
