#
# spec file for package karukan
#
# Copyright (c) 2026 Gakuto Furuya <g.furuya@gaato.net>
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

Name:           karukan
Version:        0.1.0
Release:        0
Summary:        Japanese input method for Fcitx5 powered by neural kana-kanji conversion
Summary(ja):    ニューラルかな漢字変換を搭載した Fcitx5 用日本語入力メソッド
License:        MIT OR Apache-2.0
Group:          System/I18n/Japanese
URL:            https://github.com/togatoga/karukan
Source0:        karukan-%{version}.tar.zst
Source1:        vendor.tar.zst
# Skip cargo build in CMake -- already built in %%build via cargo_build
Patch0:         fcitx5-karukan-skip-cargo-build.patch
# Make karukan-server serve packaged static files from %%{_datadir}
Patch1:         karukan-server-static-path.patch
# KDE icon theme engine strips hyphens on fallback; use underscores
Patch2:         fcitx5-karukan-icon-underscore.patch
ExclusiveArch:  %{rust_arches}
ExcludeArch:    armv7l

BuildRequires:  cargo >= 1.92
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  cmake >= 3.16
BuildRequires:  cmake(Fcitx5Core) >= 5.0
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  rust >= 1.92
BuildRequires:  zstd

%description
Karukan is a Japanese Input Method Engine for Linux that uses neural
kana-kanji conversion powered by llama.cpp.

%package -n fcitx5-karukan
Summary:        Japanese input method for Fcitx5 powered by neural kana-kanji conversion
Summary(ja):    ニューラルかな漢字変換を搭載した Fcitx5 用日本語入力メソッド
Group:          System/I18n/Japanese
Requires:       fcitx5

%description -n fcitx5-karukan
Karukan is a Japanese Input Method Engine for Linux that uses neural
kana-kanji conversion powered by llama.cpp. It provides a fcitx5 addon
for romaji-to-hiragana conversion and intelligent kana-kanji conversion
using small neural network models (auto-downloaded on first use).

Features:
- Romaji-to-hiragana conversion with 200+ rules
- Neural kana-kanji conversion via llama.cpp (GGUF models)
- Adaptive model selection for low-latency input
- Learning cache for user conversion history
- System dictionary with double-array trie

%description -n fcitx5-karukan -l ja
Karukan は、llama.cpp を利用したニューラルかな漢字変換を搭載する
Linux 向け日本語入力メソッドエンジンです。Fcitx5 アドオンとして
ローマ字からひらがなへの変換と、小規模ニューラルネットワークモデル
（初回使用時に自動ダウンロード）によるインテリジェントなかな漢字変換を
提供します。

主な機能:
- 200 以上のルールによるローマ字→ひらがな変換
- llama.cpp (GGUF モデル) によるニューラルかな漢字変換
- 低レイテンシ入力のための適応的モデル選択
- ユーザー変換履歴の学習キャッシュ
- ダブル配列トライによるシステム辞書

%package tools
Summary:        CLI tools for Karukan (dictionary builder, server, benchmark)
Summary(ja):    Karukan の CLI ツール（辞書ビルダー、サーバー、ベンチマーク）
Group:          System/I18n/Japanese
Suggests:       fcitx5-karukan = %{version}-%{release}

%description tools
Command-line tools for the Karukan Japanese input method:
- karukan-dict: dictionary management tool
- karukan-server: HTTP server for testing kana-kanji conversion
- sudachi-dict: Sudachi dictionary builder
- ajimee-bench: benchmark tool for conversion accuracy evaluation

These tools are intended for development, testing, and dictionary
maintenance. They are not required for normal IME usage.

%description tools -l ja
Karukan 日本語入力メソッドのコマンドラインツール:
- karukan-dict: 辞書管理ツール
- karukan-server: かな漢字変換テスト用 HTTP サーバー
- sudachi-dict: Sudachi 辞書ビルダー
- ajimee-bench: 変換精度評価用ベンチマークツール

これらのツールは開発・テスト・辞書メンテナンス用です。
通常の IME 使用には必要ありません。

%prep
%autosetup -p1 -n karukan-%{version} -a1

%build
# Workaround: llama-cpp-sys-2 build.rs requires CARGO_CFG_TARGET_FEATURE
# which is unset on some architectures (ppc64le, s390x, armv7l)
export CARGO_CFG_TARGET_FEATURE="${CARGO_CFG_TARGET_FEATURE:-}"

# Build the Rust shared library and CLI tools (vendored, offline)
export CARGO_HOME=$PWD/.cargo
%{cargo_build} -p karukan-im -p karukan-cli

# Build the fcitx5 C++ addon
pushd karukan-im/fcitx5-addon
%cmake
%cmake_build
popd

%install
# Install the fcitx5 C++ addon via cmake
pushd karukan-im/fcitx5-addon
%cmake_install
popd

# CLI tools
install -Dm755 target/release/karukan-dict %{buildroot}%{_bindir}/karukan-dict
install -Dm755 target/release/karukan-server %{buildroot}%{_bindir}/karukan-server
install -Dm755 target/release/sudachi-dict %{buildroot}%{_bindir}/sudachi-dict
install -Dm755 target/release/ajimee-bench %{buildroot}%{_bindir}/ajimee-bench

# Server static assets (served by karukan-server at runtime)
install -d %{buildroot}%{_datadir}/karukan/static
install -Dm644 karukan-cli/static/index.html %{buildroot}%{_datadir}/karukan/static/index.html
install -Dm644 karukan-cli/static/app.js %{buildroot}%{_datadir}/karukan/static/app.js
install -Dm644 karukan-cli/static/styles.css %{buildroot}%{_datadir}/karukan/static/styles.css

# Flatpak-style icon symlinks required by fcitx5 system tray
for size in 16 24 32 48 128; do
    ln -s fcitx_karukan.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/org.fcitx.Fcitx5.fcitx_karukan.png
done

# Default config and user dictionary
install -Dm644 karukan-im/config/default.toml \
    %{buildroot}%{_datadir}/fcitx5/karukan/default.toml
install -Dm644 karukan-im/config/default_user_dict.txt \
    %{buildroot}%{_datadir}/fcitx5/karukan/default_user_dict.txt

%check
export CARGO_CFG_TARGET_FEATURE="${CARGO_CFG_TARGET_FEATURE:-}"
export CARGO_HOME=$PWD/.cargo
# Skip tests that require downloading models from Hugging Face (no network in OBS)
%{cargo_test} -p karukan-engine --lib -- --skip kanji::backend::tests
%{cargo_test} -p karukan-engine --test romaji_tests -- --skip test_zenninn_kanji_conversion
%{cargo_test} -p karukan-im --lib

%files -n fcitx5-karukan
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_fcitx5_libdir}/karukan.so
%{_fcitx5_libdir}/libkarukan_im.so
%{_fcitx5_addondir}/karukan.conf
%{_fcitx5_imconfdir}/karukan.conf
%{_fcitx5_datadir}/karukan/
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Karukan.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/fcitx_karukan.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_karukan.png

%files tools
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/karukan-dict
%{_bindir}/karukan-server
%{_bindir}/sudachi-dict
%{_bindir}/ajimee-bench
%{_datadir}/karukan/

%changelog
