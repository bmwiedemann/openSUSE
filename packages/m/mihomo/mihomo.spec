#
# spec file for package mihomo
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


# Factory's rust ships the wasm32-wasip1 std only on x86_64/aarch64
%if 0%{?suse_version} > 1600
%ifarch x86_64 aarch64
%bcond_without easytier
%endif
%endif
%global gotags with_gvisor%{!?with_easytier:,no_easytier}
Name:           mihomo
Version:        1.19.34
Release:        0
Summary:        The universal proxy platform
# Legal-Review-Notice: mihomo's own code is GPL-3.0-only, but the Go binary
# statically links its whole vendored module set, so the tag covers the linked
# set. Copyleft actually linked into the shipped binary (derived from
# "go list -deps" for linux/amd64+arm64 with -tags with_gvisor, mapped onto
# vendor/modules.txt): GPL-3.0-or-later (the metacubex/sing* family, fswatch,
# randv2, enfein/mieru, sina-ghaderi/*) - absorbed by GPL-3.0-only -,
# LGPL-3.0-only (easytier/easytier-go for the EasyTier outbound, new
# in 1.19.31) and MPL-2.0 (metacubex/zerotier-go, metacubex/mipstack,
# metacubex/yamux, hashicorp/golang-lru). MPL-2.0 section 3.2 source
# availability is satisfied by vendor.tar.gz shipping in the src.rpm.
License:        GPL-3.0-only AND LGPL-3.0-only AND MPL-2.0
URL:            https://github.com/MetaCubeX/mihomo
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        config.yaml
Source3:        %{name}.service
Source4:        start.sh
Source5:        easytier-wasi-2.7.0+2abb167.tar.zst
# upstream go.mod asks for go 1.20, but %%check uses "go test -skip",
# which exists only since go 1.21
BuildRequires:  golang(API) >= 1.21
BuildRequires:  golang-packaging
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  zstd
Requires:       bash
# mihomo is the maintained successor to clash (the original Dreamacro/clash was
# archived; its final release was 1.18.0) and to the former Clash.Meta
Provides:       clash = %{version}
Obsoletes:      clash < %{version}
Provides:       clash-meta = %{version}
Obsoletes:      clash-meta < %{version}
# easytier_core.wasm is stripped from vendor.tar.gz after every service run
# and rebuilt from Source5 in %%build (see the recipe there)
# Source-Binary-Exception: vendor.tar.gz:vendor/github.com/metacubex/wazero/testdata/*.wasm -- test-data: wazero unit-test fixtures, never built or shipped
# Source-Binary-Exception: vendor.tar.gz:vendor/github.com/metacubex/wazero/*/testdata/*.wasm -- test-data: wazero unit-test fixtures, never built or shipped
# Source-Binary-Exception: vendor.tar.gz:vendor/github.com/metacubex/sing-tun/internal/wintun/*/*.dll -- other-platform: Windows wintun driver DLLs, unused on Linux builds
# binaryen, cargo, rust, protobuf: EasyTier WASI core rebuild in %%build;
# rust 1.95 is upstream's rust-version
%if %{with easytier}
BuildRequires:  binaryen
BuildRequires:  cargo >= 1.95
BuildRequires:  rust >= 1.95
# protobuf-devel: protoc and its well-known-type includes for prost-build
BuildRequires:  pkgconfig(protobuf) >= 35.1
%endif

%description
mihomo (formerly Clash.Meta) is a rule-based tunnel / universal proxy platform
written in Go. It is the actively maintained successor to the original clash.

%prep
%autosetup -a1
%setup -q -T -D -a5

%build
%limit_build -m 4000
%if %{with easytier}
# upstream's build-wasi-core.sh recipe; system wasm-opt, not pinned Binaryen 131
export CARGO_NET_OFFLINE=true
export RUSTFLAGS=
export CARGO_ENCODED_RUSTFLAGS="--remap-path-prefix=$PWD/easytier-wasi-2.7.0+2abb167=/workspace/EasyTier"
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
export CARGO_TARGET_DIR=$PWD/target-wasi
# commit-time epoch for cargo only (Go BuildTime keeps the changelog one);
# subshell: cargo reads .cargo/config.toml from the cwd only
(cd easytier-wasi-2.7.0+2abb167 &&
SOURCE_DATE_EPOCH=1794361856 cargo build --frozen --release --target wasm32-wasip1 \
    -p easytier-core --no-default-features \
    --features "management,proxy-smoltcp-stack,wasi-crypto-offload,aes-gcm,tcp-hole-punch" \
    --jobs %{_smp_build_ncpus})
wasm-opt -O4 --enable-bulk-memory --enable-bulk-memory-opt \
    --enable-nontrapping-float-to-int \
    target-wasi/wasm32-wasip1/release/easytier_core.wasm \
    -o vendor/github.com/easytier/easytier/easytier-go/internal/artifact/easytier_core.wasm
# Provenance in generator format for the rebuilt artifact (the Go host
# rejects an artifact/bindings commit mismatch, so both move together)
wasm_sha="$(sha256sum vendor/github.com/easytier/easytier/easytier-go/internal/artifact/easytier_core.wasm | cut -d' ' -f1)"
printf '// Code generated by go generate; DO NOT EDIT.\n\npackage artifact\n\nconst (\n\tCommit = "2abb1676b475947e46c527b57acc5f296cb48482"\n\tSHA256 = "%%s"\n)\n' \
    "${wasm_sha}" > vendor/github.com/easytier/easytier/easytier-go/internal/artifact/provenance.go
printf '// Code generated by go generate; DO NOT EDIT.\n\npackage proto\n\nconst (\n\tEasyTierCommit = "2abb1676b475947e46c527b57acc5f296cb48482"\n\tSchemaSHA256   = "fbf1c98738e0c452052223750f49612322dd04b5dadc7f7ac7c5d57254f0047f"\n)\n' \
    > vendor/github.com/easytier/easytier/easytier-go/proto/provenance.go
test -z "$(gofmt -l vendor/github.com/easytier/easytier/easytier-go/internal/artifact/ vendor/github.com/easytier/easytier/easytier-go/proto/provenance.go)"
%endif
# reproducible BuildTime from the changelog-derived SOURCE_DATE_EPOCH
build_time="$(date -u -d "@${SOURCE_DATE_EPOCH:-0}" +'%%Y-%%m-%%dT%%H:%%M:%%SZ')"
go build -trimpath -buildmode=pie \
    -ldflags "-X github.com/metacubex/mihomo/constant.Version=v%{version} \
              -X github.com/metacubex/mihomo/constant.BuildTime=${build_time}" \
    -tags %{gotags} -o %{name}

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0755 %{SOURCE4} %{buildroot}%{_libexecdir}/%{name}/start

%check
%{buildroot}%{_bindir}/%{name} -v
# Upstream's in-module unit tests run fully offline, with one exception: the
# listener/inbound *V2RayInterop tests shell out to
# "go get github.com/v2fly/v2ray-core/v5@v5.51.2" to build a v2ray binary at
# test time, which cannot work in the network-less build root - skip exactly
# those three. The separate test/ directory is its own module
# ("module mihomo-test") driving docker containers, so ./... never reaches it.
go test -mod=vendor -tags %{gotags} -skip V2RayInterop ./... >gotest.log 2>&1 || {
    cat gotest.log
    exit 1
}
cat gotest.log
# A suite that collects zero tests also exits 0, so assert it really ran
# (57 packages report "ok" as of 1.19.31).
test "$(grep -c '^ok ' gotest.log)" -ge 50

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.yaml
%{_unitdir}/%{name}.service
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/start
%{_bindir}/%{name}

%changelog
