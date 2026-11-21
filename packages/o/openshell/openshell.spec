#
# spec file for package openshell
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


%{?nil}
# Build from scratch - upstream's openshell.spec only wraps prebuilt binaries;

# Feature facts for Linux from the 0.1.5 tree:
#   openshell-gateway:    default = ["telemetry", "in-tree-compute-drivers"]
#                         in-tree-compute-drivers = docker, kubernetes, podman,
#                         vm (libkrun)
#   openshell-prover-cli: vendored-z3 (Z3 5.1.0 built from the vendored
#                         z3-src crate), prebuilt-z3 (downloads Z3 at build
#                         time; never usable in OBS)
#   openshell-supervisor: default = ["telemetry", "bundled-ca-roots"].
#                         bundled-ca-roots compiles the Mozilla roots
#                         (webpki-roots) into the binary and overlays the
#                         system store; without it the binary uses the system
#                         trust store exclusively (rustls-native-certs) and
#                         refuses to start when that store is empty. The
#                         SUSE build takes the system store: one bundle,
#                         maintained by ca-certificates-mozilla.
#   openshell-sandbox:    no features (perf-harness is a test binary)

# Build compiles telemetry out and takes the three drivers a SLE host can
# run; vm (needs libkrun) stays out.

%bcond_with telemetry
# --with vendored_z3 compiles the vendored Z3 5.1.0 source into the
# binaries instead and declares bundled(z3)
%bcond_with vendored_z3

# prover-cli and gateway are built in ONE cargo invocation so that z3-sys
# (and every shared crate) is compiled once; with two invocations cargo
# re-runs the Z3 build because feature unification differs between them.
# With several -p, features need the package/feature syntax.
%if %{with vendored_z3}
# feature chain: openshell-gateway/vendored-z3 -> openshell-server -> openshell-prover -> z3/vendored
%global z3_features openshell-prover-cli/vendored-z3,openshell-gateway/vendored-z3,
%else
%global z3_features %{nil}
%endif
%if %{with telemetry}
%global gw_telemetry ,openshell-gateway/telemetry,openshell-supervisor/telemetry
%else
%global gw_telemetry %{nil}
%endif
%global gw_drivers openshell-gateway/compute-driver-docker,openshell-gateway/compute-driver-podman,openshell-gateway/compute-driver-kubernetes
# --no-default-features also applies to openshell-supervisor in the shared
# invocation: that is what drops bundled-ca-roots. The only crate that would
# pull openshell-supervisor-network back in with its default features is the
# mxc driver, which is not built.
%global server_features --no-default-features --features %{z3_features}%{gw_drivers}%{gw_telemetry}

# The sandbox runtime is side-loaded into workload containers built from
# images OpenShell did not build, so it must not depend on the image's libc:
# a static PIE against glibc (upstream reaches the same goal with musl).
# cargo applies RUSTFLAGS to host artifacts (build scripts, proc macros) too
# unless --target is explicit, and a proc macro cannot be built with
# crt-static, hence the explicit triple on that one invocation.
%global rust_triple %{_target_cpu}-unknown-linux-gnu

# Rust binaries with vendored crates: no usable debugsource split yet.
%global debug_package %{nil}

Name:           openshell
Version:        0.1.8
# Release carries the revision of this spec file
Release:        0
Summary:        Sandboxed runtime for autonomous AI agents
# Expression computed upstream from cargo tree for the statically linked
# crates. CHECK with cargo-about before submission; the OpenSSL-licensed
# parts of AWS-LC (aws-lc-sys) look missing from upstream's list.
License:        Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND CDLA-Permissive-2.0 AND ISC AND MIT AND Unicode-3.0 AND Zlib
Group:          System/Management
URL:            https://github.com/NVIDIA/OpenShell
Source0:        https://github.com/NVIDIA/OpenShell/archive/refs/tags/v%{version}.tar.gz#/OpenShell-%{version}.tar.gz
# cargo_vendor service output: vendor/, .cargo/config.toml and Cargo.lock
Source1:        vendor.tar.gz
# Example systemd drop-in: cgroup controller delegation for user sessions,
# which SUSE disables by default and rootless podman needs for the limits
# the Podman driver sets. Shipped under /usr/share, never installed into
# /etc by the package (README.SUSE explains the activation).
Source3:        80-openshell-delegate.conf
Source4:        openshell-gateway-README.SUSE
Source5:        openshell-rpmlintrc
ExclusiveArch:  x86_64 aarch64

# MSRV from Cargo.toml (rust-version = "1.94")
BuildRequires:  cargo >= 1.94
BuildRequires:  cmake >= 3.16
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.94
# system protoc instead of the prebuilt one in the protoc-bin-vendored crate
BuildRequires:  protobuf-devel
BuildRequires:  systemd-rpm-macros
# libc.a for the static sandbox runtime (glibc >= 2.34 folds libpthread and
# libdl into it, so this one package is the whole static C runtime)
BuildRequires:  glibc-devel-static
%if 0%{?suse_version} < 1600
BuildRequires:  gcc15-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{with vendored_z3}
# Z3's CMake build generates code with Python
# CHECK on SLE 15: python3 is 3.6 there; use python311-base if Z3 rejects it
BuildRequires:  python3-base
%else
# the API level of the z3-sys 0.13 bindings
BuildRequires:  z3-devel >= 5.1
%endif
BuildRequires:  pandoc
Recommends:     podman

%description
OpenShell runs autonomous AI agents in sandboxes that are isolated with
Linux kernel facilities (Landlock, seccomp, network namespaces) and governed
by declarative YAML policies for filesystem, process, network and inference
access. This package contains the openshell command line client.

%package gateway
Summary:        OpenShell gateway: control plane for agent sandboxes
Group:          System/Management
%if 0%{?suse_version} < 1600
# SLE 15 SP7 ships Podman 4.9.5. Verified 2026-10-22: its libpod API accepts
# the v5.0.0 prefix the driver hardcodes.
Requires:       podman >= 4.9.5
%else
# upstream qualification scope: Podman 5.x with cgroup v2 and a user socket
Requires:       podman >= 5.0
%endif
Requires:       %{name} = %{version}
Requires:       openssl
%if %{with vendored_z3}
Provides:       bundled(z3) = 5.1.0
%endif

%description gateway
The OpenShell gateway manages sandbox lifecycle through a compute driver
(Podman, Docker, Kubernetes) and enforces sandbox policies. This package
installs a systemd user unit; enable it with
"systemctl --user enable --now openshell-gateway". On SUSE hosts, rootless
podman needs cgroup controller delegation that the distribution does not
enable by default; README.SUSE in the package documentation and the example
drop-in /usr/share/openshell-gateway/80-openshell-delegate.conf cover it.

%package prover
Summary:        OpenShell policy boundary prover
Group:          System/Management
%if %{with vendored_z3}
Provides:       bundled(z3) = 5.1.0
%endif

%description prover
Standalone checker that proves whether a candidate sandbox policy stays
within an operator-defined boundary policy, without a gateway connection.

%package sandbox
Summary:        OpenShell sandbox runtime (static binary behind the sandbox runtime image)
Group:          System/Management

%description sandbox
The sandbox runtime is the process on the untrusted side of the OpenShell
boundary: it starts the agent as its child, identifies the calling program
of every request, applies Landlock and seccomp restrictions and hands TCP
and DNS requests to the supervisor for a policy decision. It is a static
binary because it runs inside workload images OpenShell did not build.

The Podman driver mounts the sandbox runtime image into every workload
container and executes the binary from there, never from the host. This
package is the build input for that image (see the openshell-sandbox-image
package); installing it on a host has no effect on a running gateway.

%package supervisor
Summary:        OpenShell sandbox supervisor (binary behind the supervisor image)
Group:          System/Management
# Built without bundled-ca-roots: TLS trust comes from the system store and
# the binary refuses to start when the store is empty.
Requires:       (ca-certificates-mozilla or ca-certificates-mozilla-prebuilt)

%description supervisor
The supervisor is the process on the trusted side of the OpenShell boundary:
it checks every connection the sandbox forwards against policy, resolves
DNS, attaches provider credentials only to requests bound for approved
endpoints and keeps the session with the gateway. Agents never reach it
directly.

The Podman driver runs the supervisor as its own container from the
supervisor image; this package is the build input for that image (see the
openshell-supervisor-image package). TLS trust comes from the system
certificate store of whatever root filesystem the binary runs in.

%prep
%setup -q -n OpenShell-%{version}
# vendored crates, the matching .cargo/config.toml and the lock file
tar xzf %{SOURCE1}
# distro cargo ignores rust-toolchain.toml; a rustup-managed one must not see it
rm -f rust-toolchain.toml
# upstream keeps a 0.0.0 placeholder; patch manifest and lock file together,
# otherwise cargo refuses the stale lock
sed -i 's/^version = "0.0.0"/version = "%{version}"/' Cargo.toml
sed -i '/^name = "openshell-/{n;s/^version = "0.0.0"/version = "%{version}"/}' Cargo.lock
grep -q '^version = "%{version}"' Cargo.toml
# upstream declares #!/bin/sh but the script needs bash
sed -i '1s|^#!/bin/sh|#!/bin/bash|' deploy/rpm/migrate-gateway-config.sh

%build
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
export CARGO_INCREMENTAL=0
%if 0%{?suse_version} < 1600
# one GCC for the C/C++ parts (aws-lc-sys, vendored Z3) and for the link
# step, pinned instead of relying on rustc's default linker choice
export CC=gcc-15
export CXX=g++-15
export RUSTFLAGS="-C linker=gcc-15"
%endif
%if %{with vendored_z3}
# CHECK: if Z3's CMake step rejects the SLE 15 python3 (3.6), steer it to
# python311 with: export Python3_ROOT_DIR=/usr  (plus python311-base in
# BuildRequires) or put a python3 -> python3.11 symlink first in PATH.
%else
# z3-sys default mode: system libz3 and header
export Z3_SYS_Z3_HEADER=%{_includedir}/z3.h
%endif
# Compiled-in tag for the supervisor and sandbox-runtime image references
# (crates/openshell-core/src/config.rs reads OPENSHELL_IMAGE_TAG at build time).
# CHECK the expected format in config.rs ("0.1.5" or "v0.1.5"), then verify:
#   strings target/release/openshell-gateway | grep 'openshell/supervisor'
export OPENSHELL_IMAGE_TAG=%{version}
cargo build --offline --release %{?_smp_mflags} -p openshell-cli
cargo build --offline --release %{?_smp_mflags} -p openshell-prover-cli -p openshell-gateway -p openshell-supervisor %{server_features}
# the sandbox runtime as a static PIE; see rust_triple above.
RUSTFLAGS="${RUSTFLAGS:-} -C target-feature=+crt-static" \
    cargo build --offline --release %{?_smp_mflags} --target %{rust_triple} -p openshell-sandbox
pandoc -s -t man deploy/man/openshell.1.md -o openshell.1
pandoc -s -t man deploy/man/openshell-gateway.8.md -o openshell-gateway.8

%install
install -Dpm 0755 target/release/openshell         %{buildroot}%{_bindir}/openshell
install -Dpm 0755 target/release/openshell-prover  %{buildroot}%{_bindir}/openshell-prover
install -Dpm 0755 target/release/openshell-gateway %{buildroot}%{_bindir}/openshell-gateway
install -Dpm 0755 target/release/openshell-supervisor %{buildroot}%{_bindir}/openshell-supervisor
install -Dpm 0755 target/%{rust_triple}/release/openshell-sandbox %{buildroot}%{_bindir}/openshell-sandbox

install -Dpm 0644 deploy/rpm/gateway.toml.default    %{buildroot}%{_datadir}/%{name}-gateway/gateway.toml.default
install -Dpm 0644 deploy/rpm/gateway.toml.default.v1 %{buildroot}%{_datadir}/%{name}-gateway/gateway.toml.default.v1
install -Dpm 0755 deploy/rpm/migrate-gateway-config.sh %{buildroot}%{_libexecdir}/%{name}-gateway-migrate-config
install -d %{buildroot}%{_docdir}/%{name}-gateway
install -pm 0644 deploy/rpm/QUICKSTART.md deploy/rpm/CONFIGURATION.md deploy/rpm/TROUBLESHOOTING.md \
    %{buildroot}%{_docdir}/%{name}-gateway/
install -pm 0644 %{SOURCE4} %{buildroot}%{_docdir}/%{name}-gateway/README.SUSE
# example drop-in, activated by the administrator (see README.SUSE)
install -pm 0644 %{SOURCE3} %{buildroot}%{_datadir}/%{name}-gateway/80-openshell-delegate.conf
# Include registry URLs for supervisor and & images when known. Tag: 'latest' or %version?
%if 0%{?registry_path:1} > 0
cat >> %{buildroot}%{_datadir}/%{name}-gateway/gateway.toml.default <<EOF
supervisor_image = "%{registry_path}/openshell-supervisor:latest"
sandbox_runtime_image = "%{registry_path}/openshell-sandbox:latest"
EOF
%endif

# Example provider profiles and the policy quickstart.
# Without these files a # user has to fetch them from GitHub; see providers/README.md.
install -d %{buildroot}%{_datadir}/%{name}/providers %{buildroot}%{_datadir}/%{name}/examples
install -pm 0644 providers/*.yaml providers/README.md %{buildroot}%{_datadir}/%{name}/providers/
install -pm 0644 examples/sandbox-policy-quickstart/policy.yaml examples/sandbox-policy-quickstart/README.md \
    %{buildroot}%{_datadir}/%{name}/examples/

# systemd user unit, following upstream's RPM unit
install -d %{buildroot}%{_userunitdir}
cat > %{buildroot}%{_userunitdir}/%{name}-gateway.service << 'EOF'
[Unit]
Description=OpenShell Gateway (user)
Documentation=https://github.com/NVIDIA/OpenShell
After=podman.socket
Wants=podman.socket

[Service]
Type=exec
ExecStartPre=%{_libexecdir}/%{name}-gateway-migrate-config %%E/openshell/gateway.toml %{_datadir}/%{name}-gateway/gateway.toml.default %{_datadir}/%{name}-gateway/gateway.toml.default.v1
ExecStartPre=%{_bindir}/%{name}-gateway config preflight
Environment=OPENSHELL_LOCAL_TLS_DIR=%%h/.local/state/openshell/tls
ExecStartPre=%{_bindir}/%{name}-gateway generate-certs --output-dir ${OPENSHELL_LOCAL_TLS_DIR} --server-san host.openshell.internal
EnvironmentFile=-%%E/openshell/gateway.env
ExecStart=%{_bindir}/%{name}-gateway
StateDirectory=openshell
Restart=on-failure
RestartSec=5
NoNewPrivileges=yes
ProtectSystem=strict
PrivateTmp=yes
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX

[Install]
WantedBy=default.target
EOF

install -Dpm 0644 openshell.1         %{buildroot}%{_mandir}/man1/openshell.1
install -Dpm 0644 openshell-gateway.8 %{buildroot}%{_mandir}/man8/openshell-gateway.8

%check
%{buildroot}%{_bindir}/openshell --version
%{buildroot}%{_bindir}/openshell-prover --version
%{buildroot}%{_bindir}/openshell-gateway --version
%{buildroot}%{_bindir}/openshell-gateway config preflight --path %{buildroot}%{_datadir}/%{name}-gateway/gateway.toml.default
%{buildroot}%{_bindir}/openshell-supervisor --version
%{buildroot}%{_bindir}/openshell-sandbox --version
# the sandbox runtime must run inside any root filesystem: no dynamic loader,
# no NEEDED entries.
if readelf -d %{buildroot}%{_bindir}/openshell-sandbox | grep -q 'NEEDED'; then
    echo "openshell-sandbox is dynamically linked; the sandbox runtime must be static" >&2
    exit 1
fi
# the supervisor is meant to be dynamic (glibc from the image)
readelf -d %{buildroot}%{_bindir}/openshell-supervisor | grep -q 'NEEDED.*libc\.so'

%files
%license LICENSE THIRD-PARTY-NOTICES
%doc README.md
%{_bindir}/openshell
%{_datadir}/%{name}/
%{_mandir}/man1/openshell.1%{?ext_man}

%files prover
%license LICENSE THIRD-PARTY-NOTICES
%{_bindir}/openshell-prover

%files sandbox
%license LICENSE THIRD-PARTY-NOTICES
%{_bindir}/openshell-sandbox

%files supervisor
%license LICENSE THIRD-PARTY-NOTICES
%{_bindir}/openshell-supervisor

%files gateway
%license LICENSE THIRD-PARTY-NOTICES
%doc %{_docdir}/%{name}-gateway/
%{_bindir}/openshell-gateway
%{_userunitdir}/%{name}-gateway.service
%{_libexecdir}/%{name}-gateway-migrate-config
%dir %{_datadir}/%{name}-gateway
%{_datadir}/%{name}-gateway/gateway.toml.default
%{_datadir}/%{name}-gateway/gateway.toml.default.v1
%{_datadir}/%{name}-gateway/80-openshell-delegate.conf
%{_mandir}/man8/openshell-gateway.8%{?ext_man}

%changelog
