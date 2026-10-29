#
# spec file for package zed
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2025 Marvin Friedrich
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


# Upstream's release profile is thin LTO with one codegen unit; this replaces
# the distribution rustflags %%cargo_build would otherwise pass.
%global build_rustflags "-C" "linker=clang" "-C" "link-arg=-fuse-ld=%{_bindir}/mold" "-C" "debuginfo=1" "-C" "incremental=false" "-C" "strip=none"
%global appid dev.zed.Zed
Name:           zed
Version:        1.24.2
Release:        0
Summary:        A high-performance, multiplayer code editor
# The zed and cli crates are GPL-3.0-or-later. The rest of the tag is the
# licence closure of what is genuinely linked, derived from
# `cargo tree --offline -e normal --target x86_64-unknown-linux-gnu` run for
# -p zed and for -p cli: every dual-licensed crate is taken under Apache-2.0
# or MIT, and every licence left in the tag has no alternative to fall back
# on. MPL-2.0 covers 12 linked crates (the five symphonia 0.5.5 crates,
# cssparser 0.36.0, cssparser-macros, dtoa-short, nucleo-matcher,
# selectors 0.37.0, option-ext, yawc); cbindgen, dwrote, mdbook, cssparser
# 0.37.0, nvim-rs and webpki-roots 0.26.8 are vendored but not linked. The
# webpki-roots that does link is 1.0.8, whose license is CDLA-Permissive-2.0,
# not MPL-2.0.
# OFL-1.1 is the IBM Plex Sans and Lilex faces embedded in the binary. nvim-rs
# is LGPL-3.0 but sits behind the non-default "neovim" feature that nothing
# enables, so it is not linked and not declared here.
License:        GPL-3.0-or-later AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND bzip2-1.0.6 AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND MIT AND MIT-0 AND MPL-2.0 AND OFL-1.1 AND Unicode-3.0 AND Zlib
URL:            https://zed.dev
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE zed-system-node-only.patch -- never download a second Node.js at run time; the package Requires the distribution's
Patch0:         zed-system-node-only.patch
# PATCH-FIX-OPENSUSE zed-telemetry-off-by-default.patch -- diagnostics/metrics default off; still switchable in the settings UI
Patch1:         zed-telemetry-off-by-default.patch
# PATCH-FEATURE-OPENSUSE zed-opt-in-binary-downloads.patch -- built-in language servers, default Prettier and extension updates are fetched only with allow_binary_downloads
Patch2:         zed-opt-in-binary-downloads.patch
BuildRequires:  cargo >= 1.98.1
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-runtime
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  livekit-libwebrtc-devel
BuildRequires:  mold
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 18.5.12
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(zlib)
# NOT the spec-cleaner form: `--perl` expands git-core into git-core's Perl
# provides, which drags git-svn and subversion into a code editor. Zed shells
# out to the git CLI and contains no Perl, so the package name is the correct
# dependency, here and in the BuildRequires above, and both of those
# spec-cleaner hunks are deliberately not applied.
Requires:       git-core
# blade loads Vulkan at run time; without a loader zed starts and renders nothing
Requires:       libvulkan1
Requires:       nodejs >= 22
Requires:       npm
# software Vulkan fallback for machines without a hardware Vulkan driver
Recommends:     libvulkan_lvp
ExclusiveArch:  x86_64 aarch64

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code
editor from the creators of Atom and Tree-sitter.

%prep
%autosetup -p1 -a1

# webrtc-sys hard-codes a static link and otherwise downloads a prebuilt
# libwebrtc from GitHub, which OBS has no network for. livekit-libwebrtc ships
# the shared library; this one line is its documented consumer contract.
# The crate is vendored from a git dependency, so its directory carries the
# version. Fail loudly if it stops matching: silently leaving the static link
# in place makes webrtc-sys try to download a prebuilt library instead.
_wsys=$(ls -d vendor/webrtc-sys-[0-9]*/ | head -1)
test -f "${_wsys}build.rs"
grep -q 'cargo:rustc-link-lib=static=webrtc' "${_wsys}build.rs"
sed -i 's/cargo:rustc-link-lib=static=webrtc/cargo:rustc-link-lib=dylib=webrtc/' "${_wsys}build.rs"
# Cargo verifies every vendored file against .cargo-checksum.json, so the edit
# above has to be recorded or the build stops at "checksum has changed".
python3 - "${_wsys}" <<'CKSUM'
import hashlib, json, pathlib, sys
d = pathlib.Path(sys.argv[1])
cs = d / ".cargo-checksum.json"
j = json.loads(cs.read_text())
j["files"]["build.rs"] = hashlib.sha256((d / "build.rs").read_bytes()).hexdigest()
cs.write_text(json.dumps(j))
CKSUM

# .cargo/config.toml comes from the vendor tarball: obs-service-cargo merges
# upstream's settings (symbol-mangling-version=v0 and --cfg tokio_unstable,
# both of which the source needs) with the vendored-source replacements, so it
# must NOT be deleted -- without it cargo tries to fetch the git dependencies.
# Only upstream's aarch64 block goes, which forces lld to link the static
# libwebrtc.a we do not use; the linker comes from build_rustflags instead.
python3 - <<'CARGOCFG'
import pathlib, re
p = pathlib.Path(".cargo/config.toml")
s = p.read_text()
s2 = re.sub(r'^\[target\.aarch64-unknown-linux-gnu\]\n(?:(?!^\[)[^\n]*\n)*',
            '', s, count=1, flags=re.M)
assert s2 != s, "aarch64 lld block not found -- check whether upstream moved it"
p.write_text(s2)
CARGOCFG

%build
export ZED_UPDATE_EXPLANATION="Updates come from the distribution's packages"
export RELEASE_VERSION=%{version}
# Without this webrtc-sys fetches a prebuilt libwebrtc over the network.
export LK_CUSTOM_WEBRTC=%{_libdir}/livekit-webrtc
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export ZSTD_SYS_USE_PKG_CONFIG=1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
# webrtc-sys compiles its C++ shim with include paths copied from
# Chromium's bundled Debian sysroot, which a distribution build does not
# have, so gio/gio.h is not found. cc-rs honours CXXFLAGS; hand it the
# system glib flags. -fno-lto undoes the -flto=auto in %%optflags: rustc
# calls mold without -plugin, so an LTO bitcode object is fatal at link.
export CXXFLAGS="%{optflags} -fno-lto $(pkg-config --cflags gio-2.0 glib-2.0 gobject-2.0)"
%{cargo_build} --package zed --package cli

target/release/cli --completions bash > completions.bash
target/release/cli --completions fish > completions.fish
target/release/cli --completions zsh > completions.zsh

%install
# The cli looks for the editor next to its own bindir, as upstream's
# script/bundle-linux installs it.
install -D -m 0755 target/release/zed %{buildroot}%{_libexecdir}/zed-editor
install -D -m 0755 target/release/cli %{buildroot}%{_bindir}/zed

export DO_STARTUP_NOTIFY="true"
export APP_CLI="zed"
export APP_ICON="zed"
export APP_NAME="Zed"
export APP_ID="%{appid}"
export APP_ARGS="%%U"
export BRANDING_LIGHT="#99c1f1"
export BRANDING_DARK="#1a5fb4"
envsubst < crates/zed/resources/zed.desktop.in > %{appid}.desktop
envsubst < crates/zed/resources/flatpak/zed.metainfo.xml.in > %{appid}.metainfo.xml
sed -i '/@release_info@/d' %{appid}.metainfo.xml
install -D -m 0644 %{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
install -D -m 0644 %{appid}.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml
install -D -m 0644 crates/zed/resources/app-icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

install -D -m 0644 completions.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m 0644 completions.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m 0644 completions.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

# %%license installs by basename, so the per-face OFL texts need names of their
# own: upstream calls one OFL.txt and the other license.txt.
cp assets/fonts/lilex/OFL.txt OFL-Lilex.txt
cp assets/fonts/ibm-plex-sans/license.txt OFL-IBMPlexSans.txt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
# The cargo suite is not run: it wants a Vulkan device, a Wayland or X11
# display and the host keymap, none of which a build worker has.
%{buildroot}%{_bindir}/zed --version
# The point of this package: the editor links the packaged libwebrtc
# rather than a downloaded prebuilt archive.
readelf -d %{buildroot}%{_libexecdir}/zed-editor | grep -q 'NEEDED.*libwebrtc-suse\.so'

%files
%license LICENSE-GPL LICENSE-APACHE OFL-Lilex.txt OFL-IBMPlexSans.txt
%doc README.md
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
