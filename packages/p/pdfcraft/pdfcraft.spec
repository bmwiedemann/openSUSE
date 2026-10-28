#
# spec file for package pdfcraft
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


Name:           pdfcraft
Version:        0.13.0
Release:        0
Summary:        Open-source PDF workbench
# Legal-Review-Notice: scope is the offline vendor build of the two
# shipped targets (-p pdfcraft -p pdfcraft-cli, 498 crates via cargo
# tree -e normal). Upstream code is MIT OR Apache-2.0. Patched vendor
# crates (vendor/): hayro 0.7.1, hayro-interpret 0.7.0, hayro-syntax
# 0.7.2, hayro-jbig2 0.3.0, hayro-cmap 0.1.0, vello_common 0.0.8 (all
# Apache-2.0 OR MIT), lopdf 0.45.0 (MIT), winit 0.30.13 (Apache-2.0),
# egui-wgpu 0.36.2 (MIT OR Apache-2.0); licence files unchanged.
# Embedded hayro assets: Foxit standard-14 fonts (BSD-3-Clause), Adobe
# CMaps in hayro-cmap (BSD-3-Clause, same blob as the crates.io 0.1.0
# used up to 0.9.0), CGATS001Compat ICC profile (CC0-1.0); their texts
# ship under pdf-backend/. Linked third-party code adds
# BSD-2-Clause (arrayref 0.3.9), BSD-3-Clause, CC0-1.0, ISC, OFL-1.1
# plus Ubuntu-font-1.0 (epaint default fonts, also shipped under
# assets/fonts), MIT, Bitstream-Vera (Hack-Regular via ATTRIBUTION.toml
# entry MIT AND Bitstream-Vera), Unicode-3.0 (ICU crates), Zlib
# (foldhash 0.2.0). self_cell 1.3.0 (Apache-2.0 OR GPL-2.0-only) is
# taken under the Apache-2.0 option. ryu-js 1.0.3 (Apache-2.0 OR
# BSL-1.0) is likewise taken under the Apache-2.0 option. No MPL/LGPL/GPL/EPL/CDDL/CC-BY-SA
# is linked. OCR code is linked but its CC-BY-SA-4.0 models are not
# shipped (assets/models absent). docs/brand (trademarked, not open
# source) is excluded via tar_scm, removed via rm -rf, and its
# include_bytes! embeds are patched to the open-source tile.
# CRAFT_FONTS_DIR stays unset (system CJK fallback). No webpki-roots:
# TLS uses rustls-native-certs 0.8.4 with OS roots.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND Bitstream-Vera AND CC0-1.0 AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/pdfcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-cratesio.tar.zst
# PATCH-FIX-OPENSUSE pdfcraft-no-brand-assets.patch -- replace trademarked
# ArtCraft marks (docs/brand/, NOT open source) embedded via include_bytes!
# with the open-source PdfCraft tile; permanent downstream carry, not
# upstreamable (upstream ships the marks intentionally).
Patch0:         pdfcraft-no-brand-assets.patch
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
# aws-lc-sys via pdfcraft-sign -> aws-lc-rs compiles C sources with cmake.
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
# aws-lc-sys (via pdfcraft-sign) runs perl build scripts; keep the package-name
# form: spec-cleaner --perl would explode this into hundreds of perl() lines.
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
# wgpu GPU backend: Vulkan preferred, EGL fallback.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
# winit keyboard handling.
Requires:       libxkbcommon.so.0()(64bit)
# mesa provides Vulkan in a VM; the -cli companion is optional at
# runtime but installed by default; portal enables file choosers.
Recommends:     mesa-vulkan-drivers
Recommends:     pdfcraft-cli
Recommends:     xdg-desktop-portal
# X11/Wayland client libs for the desktop GUI only; the headless
# -cli subpackage needs none of these.
Recommends:     libX11.so.6()(64bit)
Recommends:     libXcursor.so.1()(64bit)
Recommends:     libXi.so.6()(64bit)
Recommends:     libXrandr.so.2()(64bit)
Recommends:     libwayland-client.so.0()(64bit)
ExclusiveArch:  %{rust_tier1_arches}

%description
Open-source, native PDF workbench: read, comment, fill and sign forms,
organize, combine, split, edit, redact, protect and export PDFs.

This package provides the desktop application; the companion pdfcraft-cli
subpackage provides the headless command runner and opt-in MCP server.

%package -n pdfcraft-cli
Summary:        Headless PdfCraft command runner and MCP server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND Bitstream-Vera AND CC0-1.0 AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n pdfcraft-cli
Headless PdfCraft command runner: inspect, render and robustness-check PDFs
from scripts and CI, plus an opt-in MCP server for agents.

%prep
%autosetup -p1 -a1
# Trademarked ArtCraft marks must never ship: belt-and-braces removal even
# though tar_scm already excludes docs/brand from the tarball.
rm -rf docs/brand
# Upstream metainfo declares the app icon as stock; it is a cached hicolor
# icon, otherwise appstream validation fails.
sed -i 's|<icon type="stock">ai.storyteller.pdfcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.pdfcraft.png</icon>|' packaging/linux/ai.storyteller.pdfcraft.metainfo.xml.in

%build
%limit_build -m 2000
# CRAFT_FONTS_DIR stays unset: use system CJK fallback instead of embedding
# the OFL craft-fonts checkout. Cargo.lock is committed upstream.
# cargo_build already passes --offline; only add --locked.
%{cargo_build} --locked -p pdfcraft -p pdfcraft-cli

%install
install -D -m 0755 target/release/pdfcraft %{buildroot}%{_bindir}/pdfcraft
install -D -m 0755 target/release/pdfcraft-cli %{buildroot}%{_bindir}/pdfcraft-cli
install -D -m 0644 packaging/linux/ai.storyteller.pdfcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.pdfcraft.desktop
install -D -m 0644 packaging/linux/ai.storyteller.pdfcraft.mime.xml %{buildroot}%{_datadir}/mime/packages/ai.storyteller.pdfcraft.xml
mkdir -p %{buildroot}%{_datadir}/metainfo
# Keep date(1) format literals: spec-cleaner would brace them as RPM macros.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/$(date -u +%Y-%m-%d)/g" packaging/linux/ai.storyteller.pdfcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.pdfcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 NOTICE %{buildroot}%{_docdir}/%{name}/
install -m 0644 ATTRIBUTION.md %{buildroot}%{_docdir}/%{name}/
install -m 0644 LICENSE-MIT LICENSE-APACHE %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/fonts/OFL-*.txt %{buildroot}%{_docdir}/%{name}/
install -m 0644 assets/icons/LICENSE-lucide.txt %{buildroot}%{_docdir}/%{name}/
# Texts of the assets the vendored hayro crates embed (NOTICE "Required
# notices"): Foxit fonts, CGATS ICC profile, Adobe CMaps.
install -D -m 0644 vendor/hayro-interpret/assets/LICENSE_FOXIT %{buildroot}%{_docdir}/%{name}/pdf-backend/LICENSE_FOXIT
install -D -m 0644 vendor/hayro-interpret/assets/CGATS_LICENSE.txt %{buildroot}%{_docdir}/%{name}/pdf-backend/CGATS_LICENSE.txt
install -D -m 0644 vendor/hayro-cmap/assets/LICENSE.txt %{buildroot}%{_docdir}/%{name}/pdf-backend/LICENSE-cmap-resources.txt
install -d -m 0755 %{buildroot}%{_docdir}/pdfcraft-cli
ln -s ../pdfcraft/README.md %{buildroot}%{_docdir}/pdfcraft-cli/README.md
ln -s ../pdfcraft/NOTICE %{buildroot}%{_docdir}/pdfcraft-cli/NOTICE
ln -s ../pdfcraft/ATTRIBUTION.md %{buildroot}%{_docdir}/pdfcraft-cli/ATTRIBUTION.md
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.pdfcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.pdfcraft.metainfo.xml
%{buildroot}%{_bindir}/pdfcraft-cli --version
%{buildroot}%{_bindir}/pdfcraft-cli info crates/ui-egui/tests/data/form.pdf > /dev/null
%{buildroot}%{_bindir}/pdfcraft --version || %{buildroot}%{_bindir}/pdfcraft --help | head -n 5

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE-APACHE
%license %{_docdir}/%{name}/LICENSE-MIT
%license %{_docdir}/%{name}/OFL-*.txt
%license %{_docdir}/%{name}/LICENSE-lucide.txt
%license %{_docdir}/%{name}/pdf-backend
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/NOTICE
%doc %{_docdir}/%{name}/ATTRIBUTION.md
%{_bindir}/pdfcraft
%{_datadir}/applications/ai.storyteller.pdfcraft.desktop
%{_datadir}/metainfo/ai.storyteller.pdfcraft.metainfo.xml
%{_datadir}/mime/packages/ai.storyteller.pdfcraft.xml
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*

%files -n pdfcraft-cli
%{_bindir}/pdfcraft-cli
%dir %{_docdir}/pdfcraft-cli
%{_docdir}/pdfcraft-cli/*

%changelog
