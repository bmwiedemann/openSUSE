#
# spec file for package hatchzip
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


Name:           hatchzip
Version:        0.1.10
Release:        0
Summary:        Archive extractor that needs free space for the extracted files only
# Legal-Review-Notice: UnRAR is not built or shipped: unrar-ng-sys is
# left out of vendor.tar.zst. Its licence text (LICENSE-UNRAR,
# packaging/linux/copyright) is in the source tarball only.
License:        MIT AND Apache-2.0 AND BSD-3-Clause AND MIT-0 AND Unicode-3.0 AND Zlib AND bzip2-1.0.6
URL:            https://github.com/xevrion/hatchzip
Source0:        %{name}-%{version}.tar.zst
# cargo_vendor's output without UnRAR, whose licence is not open source:
# zstd -d --rm vendor.tar.zst && tar --delete -f vendor.tar --wildcards 'vendor/unrar-ng-sys-*' && zstd -19 --rm vendor.tar
# Codec and fuzz-corpus test archives embed a Windows game/tool.exe fixture;
# the libloading crate ships its Windows-only test DLLs. All are read only
# by tests, never built, loaded or shipped on Linux.
# Source-Binary-Exception: hatchzip-0.1.10.tar.zst:**/tests/fixtures/** -- test-data: upstream codec and RAR test vectors, read only by the test suite
# Source-Binary-Exception: hatchzip-0.1.10.tar.zst:**/src/archive/fixtures/** -- test-data: upstream xz decoder test vectors, read only by unit tests
# Source-Binary-Exception: hatchzip-0.1.10.tar.zst:**/fuzz/corpus/** -- test-data: fuzz corpus archives, read only by fuzz targets and tests
# Source-Binary-Exception: vendor.tar.zst:vendor/libz-rs-sys-*/src/test-data/* -- test-data: libz-rs-sys gzip decoder test vector, read only by its tests
# Source-Binary-Exception: vendor.tar.zst:vendor/libloading-*/tests/*.dll -- test-data: fixtures loaded only by libloading's Windows-only tests, never on Linux
# Source-Binary-Exception: vendor.tar.zst:vendor/sevenz-rust2-*/tests/** -- test-data: sevenz-rust2's own test archives, read only by its test suite
# Source-Binary-Exception: vendor.tar.zst:vendor/sevenz-rust2-*/examples/** -- test-data: sevenz-rust2 example input archive, read only by its examples
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE hatchzip-no-unrar.patch -- Build without UnRAR, and claim no RAR support in the desktop metadata
Patch0:         hatchzip-no-unrar.patch
BuildRequires:  cargo-packaging
# %%check: the GUI tests need a font
BuildRequires:  google-noto-sans-fonts
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.93
# %%check builds a test archive with it
BuildRequires:  zip
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libzstd)

%description
HatchZip extracts ZIP, 7z, tar, tar.gz, tar.xz and split archives
in place: the
archive shrinks as the files come out, so the extraction needs free
space for the extracted files only. It can be stopped, or crash, at any
point and continues where it left off. The archive is gone once the
extraction finishes.

This build does not extract RAR archives; it refuses them without
changing anything.

%package gui
Summary:        Desktop app for HatchZip
# Legal-Review-Notice: Slint is used under its GPL-3.0-only option.
# Slint's AboutSlint widget embeds the "Made with Slint" logo
# (CC-BY-ND-4.0); sctk-adwaita embeds Cantarell-Regular.ttf (OFL-1.1).
# Slint's Inter font is built only for wasm/nto and tests.
License:        GPL-3.0-only AND MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-ND-4.0 AND ISC AND MIT-0 AND OFL-1.1 AND Unicode-3.0 AND Zlib AND bzip2-1.0.6
# winit loads its X11 and Wayland libraries at run time
Requires:       libX11-6
Requires:       libX11-xcb1
Requires:       libXcursor1
Requires:       libXi6
Requires:       libwayland-client0
Requires:       libxkbcommon-x11-0
Requires:       libxkbcommon0
# OpenGL drawing; without it the app draws on the CPU
Recommends:     libglvnd
Recommends:     libwayland-egl1
# The file dialog
Recommends:     xdg-desktop-portal

%description gui
The HatchZip desktop app extracts ZIP, 7z, tar, tar.gz, tar.xz and
split archives in place, freeing the archive as it goes, and can add itself
to the file manager's right-click menu.

%package bash-completion
Summary:        Bash completion for %{name}
License:        MIT OR Apache-2.0
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command-line completion for hatchzip.

%package zsh-completion
Summary:        Zsh completion for %{name}
License:        MIT OR Apache-2.0
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion for hatchzip.

%package fish-completion
Summary:        Fish completion for %{name}
License:        MIT OR Apache-2.0
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command-line completion for hatchzip.

%prep
%autosetup -a1 -p1
# A cargo_vendor re-run puts UnRAR back
test ! -e vendor/unrar-ng-sys-*

%build
export ZSTD_SYS_USE_PKG_CONFIG=1
%cargo_build -- -p hatchzip -p hatchzip-gui
for shell in bash zsh fish; do
  target/release/hatchzip completions $shell > hatchzip.$shell
done
target/release/hatchzip man > hatchzip.1

%install
install -Dm0755 target/release/hatchzip %{buildroot}%{_bindir}/hatchzip
install -Dm0755 target/release/hatchzip-gui %{buildroot}%{_bindir}/hatchzip-gui
ln -s hatchzip %{buildroot}%{_bindir}/hz
install -Dm0644 hatchzip.1 %{buildroot}%{_mandir}/man1/hatchzip.1
ln -s hatchzip.1 %{buildroot}%{_mandir}/man1/hz.1
install -Dm0644 hatchzip.bash %{buildroot}%{_datadir}/bash-completion/completions/hatchzip
install -Dm0644 hatchzip.zsh %{buildroot}%{_datadir}/zsh/site-functions/_hatchzip
install -Dm0644 hatchzip.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/hatchzip.fish
install -Dm0644 packaging/linux/io.github.xevrion.hatchzip.desktop \
  %{buildroot}%{_datadir}/applications/io.github.xevrion.hatchzip.desktop
install -Dm0644 packaging/linux/io.github.xevrion.hatchzip.metainfo.xml \
  %{buildroot}%{_datadir}/metainfo/io.github.xevrion.hatchzip.metainfo.xml
for icon in packaging/linux/icons/hicolor/*/apps/io.github.xevrion.hatchzip.*; do
  install -Dm0644 $icon %{buildroot}%{_datadir}/icons/${icon#packaging/linux/icons/}
done

%check
export ZSTD_SYS_USE_PKG_CONFIG=1
%cargo_test -- --workspace

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/hatchzip
%{_bindir}/hz
%{_mandir}/man1/hatchzip.1%{?ext_man}
%{_mandir}/man1/hz.1%{?ext_man}

%files gui
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/hatchzip-gui
%{_datadir}/applications/io.github.xevrion.hatchzip.desktop
%{_datadir}/metainfo/io.github.xevrion.hatchzip.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.github.xevrion.hatchzip.*

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/hatchzip

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_hatchzip

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/hatchzip.fish

%changelog
