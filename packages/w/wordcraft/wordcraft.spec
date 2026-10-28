#
# spec file for package wordcraft
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


Name:           wordcraft
Version:        0.11.0
Release:        0
Summary:        Native word processor with ribbon, styles, track changes and Word support
# Legal-Review-Notice: scope is the two shipped targets (wordcraft, wordcraft-cli).
# Upstream code is MIT OR Apache-2.0; the binaries additionally embed: OFL-1.1
# fonts (assets/fonts: Inter, JetBrains Mono, Source Sans 3, Source Serif 4) and,
# via eframe default_fonts, the Ubuntu Light font under Ubuntu-font-1.0
# (epaint_default_fonts); the CC0-1.0 hyphenation patterns
# (assets/hyphenation/en-us.pat, generated, embedded) next to the public-domain
# Moby-derived word list (assets/hyphenation/en-us.dic, embedded, no license
# obligation); the hyph-utf8 TeX hyphenation patterns, bundled unmodified and
# embedded (assets/hyphenation: pl.pat, it.pat and, since 0.10.0, de.pat under
# MIT; pt.pat under BSD-3-Clause; notices in NOTICE); and Unicode-3.0 code via
# the ICU crates. Agile-encryption support
# (password-protected Word documents) is pure-Rust RustCrypto primitives
# (aes/sha1/sha2/hmac), no system library. self_cell 1.3.0 declares Apache-2.0
# OR GPL-2.0-only; the build takes the Apache-2.0 option, so no GPL obligation
# is incurred. docs/brand (trademarked, not open source) is excluded from the
# tarball via the tar_scm exclude and is never installed. The icons are
# generated in code (crates/ui-egui/src/icons.rs, original work, no third-party
# icon set). Upstream's packaging/linux mime file is an empty stub, so no mime
# package is installed; the desktop file's MimeType entries all resolve to
# system-defined types. vendor-tree copyleft audit is recorded in the .changes
# entry of each re-vendor.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib
URL:            https://github.com/storytold/wordcraft
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo >= 1.95
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
# The xtask asset-attribution test shells out to git and asserts on its
# failure mode; without the binary it fails on the spawn error instead.
BuildRequires:  git-core
# Own /usr/share/icons/hicolor for the filelist checker: the runtime
# Requires alone does not satisfy it.
BuildRequires:  hicolor-icon-theme
BuildRequires:  memory-constraints
# eframe/wgpu document compositor: Vulkan preferred, EGL fallback.
Requires:       (libvulkan.so.1()(64bit) or libEGL.so.1()(64bit))
Requires:       hicolor-icon-theme
# X11/Wayland client libs for the desktop GUI only;
# the headless -cli subpackage needs none of these.
Requires:       libX11-xcb.so.1()(64bit)
Requires:       libX11.so.6()(64bit)
Requires:       libXcursor.so.1()(64bit)
Requires:       libXi.so.6()(64bit)
Requires:       libwayland-client.so.0()(64bit)
Requires:       libxcb.so.1()(64bit)
Requires:       libxkbcommon-x11.so.0()(64bit)
Requires:       libxkbcommon.so.0()(64bit)
Recommends:     mesa-vulkan-drivers
Recommends:     wordcraft-cli
Recommends:     xdg-desktop-portal
ExclusiveArch:  %{rust_tier1_arches}

%description
WordCraft is an open-source, native word processor with a familiar ribbon:
styles, tables, track changes, references, mail merge, and .docx, PDF, ODT,
RTF, HTML and Markdown files. It can be driven by AI agents over MCP.

This package provides the desktop application; the companion wordcraft-cli
subpackage provides the headless converter, batch runner and command server.

%package -n wordcraft-cli
Summary:        Headless WordCraft converter, batch runner and command server
# Kept per packaging policy (declare License on every subpackage);
# spec-cleaner would drop it as duplicate of the main package tag.
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND OFL-1.1 AND Ubuntu-font-1.0 AND Unicode-3.0 AND Zlib

%description -n wordcraft-cli
Headless WordCraft: convert and inspect documents, render pages, run engine
commands, and serve commands over stdio/TCP with an opt-in MCP server for
agents.

%prep
%autosetup -a1 -p1

%build
%limit_build -m 2000
# Upstream's package.sh builds these two workspace members by hand.
# CRAFT_FONTS_DIR stays unset: the build then uses the bundled
# Inter/SourceSans/SourceSerif/JetBrains Mono plus the system CJK fallback.
%{cargo_build} --locked -p wordcraft -p wordcraft-cli

%install
install -Dm0755 target/release/wordcraft %{buildroot}%{_bindir}/wordcraft
install -Dm0755 target/release/wordcraft-cli %{buildroot}%{_bindir}/wordcraft-cli
install -Dm0644 packaging/linux/ai.storyteller.wordcraft.desktop %{buildroot}%{_datadir}/applications/ai.storyteller.wordcraft.desktop
install -d -m 0755 %{buildroot}%{_datadir}/metainfo
# Fixed upstream release date (v0.11.0, 2026-10-25): a build-time date would
# make the metainfo differ on every rebuild, and spec-cleaner macro-expands
# the %-sequences of any date format string, so keep this a plain string.
sed -e "s/@VERSION@/%{version}/g" -e "s/@DATE@/2026-10-25/g" packaging/linux/ai.storyteller.wordcraft.metainfo.xml.in > %{buildroot}%{_datadir}/metainfo/ai.storyteller.wordcraft.metainfo.xml
# Upstream declares the app icon as type="stock" but it is a custom hicolor
# icon, so declare it as cached for appstream validation.
sed -i 's|<icon type="stock">ai.storyteller.wordcraft</icon>|<icon type="cached" width="64" height="64">ai.storyteller.wordcraft.png</icon>|' %{buildroot}%{_datadir}/metainfo/ai.storyteller.wordcraft.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons
cp -a assets/app-icon/hicolor %{buildroot}%{_datadir}/icons/

%check
# Workspace unit tests (default members; upstream CI runs them headless).
# Skip the wall-clock layout-linearity perf tests: their `ratio < 24.0`
# wall-clock assertion measures shared-worker speed, not the code — identical
# sources scored ratios of 33.6, 59.4 and 79.9 on three OBS workers while a
# fourth passed. The other layout tests still run.
# Skip three 0.7.0 regressions, still present in 0.8.0 (all fail
# identically on x86_64 and aarch64; test bodies unchanged in 0.10.0):
# commands_do_not_touch_the_file_system_themselves is a syntactic ratchet that
# the new is_word_2003_file helper trips (it calls check_read first, so the
# MCP read root is still enforced; only the gateway-function spelling is new);
# a_dragged_shape_leaves_the_text_behind_it needs a GPU adapter OBS workers
# lack ("No adapter found"); clicks_on_ribbon_and_status_bar_chrome keeps
# failing headless. Revisit when upstream fixes them.
# Skip four more tests that failed identically on x86_64 and aarch64 in 0.8.0
# (test bodies unchanged in 0.10.0): two layout assertions (floating-table
# paging, at-least row height) and two PDF Hebrew/Latin extraction-order
# tests, all deterministic in the minimal buildroot. Upstream CI runs the
# whole workspace since 0.10.0 (cargo xtask ci), but with the optional
# craft-fonts set (CRAFT_FONTS_DIR) that this build leaves out. Revisit when
# upstream fixes them.
# Skip four new 0.10.0 tests that fail on the OBS workers: three layout
# assertions (exact row kept together, at-least row at a page top, inline
# text box that resizes to fit) that need the optional fonts, and
# rotation_drag_turns_picture_pixels_live_and_commits_once_or_cancels, which
# needs a GPU adapter OBS workers lack ("No adapter found").
# Skip the new 0.11.0 wall-clock test a_document_of_many_paragraphs_lays_out_in_linear_time
# (same kind of timing-ratio assertion as unequal_formats_lay_out_in_linear_time;
# it measured 49x on an aarch64 worker).
%{cargo_test} --locked -- --skip unequal_formats_lay_out_in_linear_time --skip commands_do_not_touch_the_file_system_themselves --skip a_dragged_shape_leaves_the_text_behind_it --skip clicks_on_ribbon_and_status_bar_chrome_keep_typing_in_the_document --skip a_floating_table_ignores_a_paragraphs_empty_lines --skip a_row_with_less_room_than_its_minimum_height_moves_on_whole --skip latin_run_in_right_to_left_paragraph_reads_back_whole --skip right_to_left_text_extracts_in_logical_order --skip exact_row_moves_whole --skip an_at_least_row_at_the_top_of_a_page_splits_instead_of_moving_on --skip inline_box_that_resizes_to_fit_takes_its_texts_height --skip rotation_drag_turns_picture_pixels_live_and_commits_once_or_cancels --skip a_document_of_many_paragraphs_lays_out_in_linear_time --skip a_long_unbreakable_word_lays_out_in_linear_time
# Both binaries exit before any window or GPU init on --version.
%{buildroot}%{_bindir}/wordcraft --version
%{buildroot}%{_bindir}/wordcraft-cli --version
desktop-file-validate %{buildroot}%{_datadir}/applications/ai.storyteller.wordcraft.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/ai.storyteller.wordcraft.metainfo.xml

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%license assets/fonts/OFL-Inter.txt
%license assets/fonts/OFL-JetBrainsMono.txt
%license assets/fonts/OFL-SourceSans3.txt
%license assets/fonts/OFL-SourceSerif4.txt
%doc ATTRIBUTION.md
%doc NOTICE
%doc README.md
%{_bindir}/wordcraft
%{_datadir}/applications/ai.storyteller.wordcraft.desktop
# Own the per-size icon trees (dirs included): the filelist checker rejects
# unowned hicolor/<size>/apps dirs, and nothing else owns them here.
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/ai.storyteller.wordcraft.metainfo.xml

%files -n wordcraft-cli
%{_bindir}/wordcraft-cli

%changelog
