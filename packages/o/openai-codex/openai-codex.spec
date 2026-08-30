#
# spec file for package openai-codex
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


Name:           openai-codex
Version:        0.151.0
Release:        0
Summary:        OpenAI Codex coding agent for the terminal
# Legal-Review-Notice: upstream codex is Apache-2.0. Everything after that
# covers the third-party Rust crates statically linked into the shipped
# %%{_bindir}/codex binary, enumerated with
#   cargo tree --offline -p codex-cli -e normal,no-proc-macro
# against the vendored tree (874 crates on aarch64, 876 on x86_64; every one
# of them declares a licence, none is missing). Electing Apache-2.0 where it
# is offered and MIT otherwise, the tally is Apache-2.0 647, MIT 174,
# Unicode-3.0 20, MPL-2.0 12, ISC 7, BSD-3-Clause 6, Zlib 5, BSD-2-Clause 1,
# CC0-1.0 1, CDLA-Permissive-2.0 1.
#  - self_cell 1.2.2 is "Apache-2.0 OR GPL-2.0-only" and is the ONLY crate
#    anywhere in the graph offering GPL. Apache-2.0 is elected, so this
#    package carries no GPL obligation; please do not re-derive it as GPL.
#    (self_cell 0.10.3, also linked, is Apache-2.0 only.)
#  - MPL-2.0 is unavoidable and comes from nucleo, nucleo-matcher, option-ext
#    and the nine symphonia-* crates. MPL-2.0 section 3.2 source availability
#    is satisfied by vendor.tar.zst, which ships in the src.rpm.
#  - CC0-1.0 is notify, CDLA-Permissive-2.0 is webpki-roots, and Unicode-3.0
#    is forced by the icu/zerovec family. unicode-ident's "AND Unicode-3.0"
#    is proc-macro-only and is not linked into the binary.
#  - Unicode-DFS-2016 (finl_unicode, wezterm-bidi) and WTFPL (terminfo) are
#    present in vendor.tar.zst but are NOT linked: they are reachable only
#    through ratatui's optional "termina"/"termwiz" backends, and the
#    workspace builds ratatui with default-features = false and only the
#    "crossterm", "layout-cache" and "underline-color" features.
#  - The v8 crate and the bundled bubblewrap C sources are removed before the
#    build and are not shipped (see %%prep and the patches).
#  - aws-lc-sys carries the most complex expression in the tree,
#    "ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND
#    (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)". Electing
#    Apache-2.0 in each OR leaves ISC, Apache-2.0, MIT and BSD-3-Clause, all of
#    which the tag already carries. It is one of the bundled C libraries listed
#    in the Provides: bundled(...) lines below. matchit (MIT AND BSD-3-Clause),
#    encoding_rs, ring and aws-lc-rs similarly keep ISC / BSD-3-Clause in the
#    tag even when Apache-2.0 is elected as the crate's primary licence.
License:        Apache-2.0 AND MIT AND Unicode-3.0 AND MPL-2.0 AND ISC AND BSD-3-Clause AND Zlib AND BSD-2-Clause AND CC0-1.0 AND CDLA-Permissive-2.0
URL:            https://github.com/openai/codex
Source0:        https://github.com/openai/codex/archive/refs/tags/rust-v%{version}.tar.gz#/codex-rust-v%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE codex-drop-v8-code-mode.patch mpluskal@suse.com -- drop the workspace members whose v8 dependency downloads a prebuilt library at build time
Patch0:         codex-drop-v8-code-mode.patch
# PATCH-FIX-OPENSUSE codex-no-startup-update-check.patch mpluskal@suse.com -- distribution policy: do not probe github.com for updates on startup
Patch1:         codex-no-startup-update-check.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging >= 1.2.0
BuildRequires:  cmake
BuildRequires:  gcc-c++
# %%limit_build: cap parallel rustc jobs by available memory (see %%build)
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
BuildRequires:  zstd
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(openssl)
# The Linux sandbox launcher looks up bwrap in PATH and panics when it is
# absent, so this is a hard requirement rather than a recommendation.
Requires:       bubblewrap
# codex reads and writes the working tree through git.
Requires:       git-core
# Used for the built-in code search when present.
Recommends:     ripgrep
# Rust -sys crates that compile and statically link a bundled C library rather
# than using the system one. There is no crate-level switch to unbundle
# aws-lc-sys (it is reached through rama-tls-rustls); the others are the
# crates' only supported build mode.
Provides:       bundled(aws-lc) = 1.71.0
Provides:       bundled(bzip2) = 1.0.8
Provides:       bundled(libzstd) = 1.5.7
Provides:       bundled(oniguruma) = 6.9.10
Provides:       bundled(sqlite) = 3.51.3
ExclusiveArch:  %{rust_tier1_arches}

%description
Codex is OpenAI's coding agent for the terminal. It runs an interactive TUI
that pairs with the Codex models to read, edit and reason about the code in
the current working directory, run shell commands inside a sandbox and drive
common developer workflows from the command line.

The %{_bindir}/codex binary is a multicall executable: the helper programs
(apply_patch, codex-linux-sandbox, codex-execve-wrapper) are dispatched from
argv[0], and the remaining tools are subcommands (exec, mcp-server,
app-server, execpolicy, sandbox, responses-api-proxy, completion, doctor,
agents, queue).

%package bash-completion
Summary:        Bash completion for codex
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for codex.

%package fish-completion
Summary:        Fish completion for codex
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for codex.

%package zsh-completion
Summary:        Zsh completion for codex
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for codex.

%prep
%autosetup -p1 -n codex-rust-v%{version}
# Upstream pins an exact toolchain via rustup; drop it so the distribution
# rust/cargo is used instead of trying to invoke rustup at build time.
rm -f codex-rs/rust-toolchain.toml
# codex-rs/vendor holds a complete bubblewrap 0.11.2 C source tree that the
# bwrap crate's build script would compile and bundle. Drop it and use the
# system bubblewrap instead (see CODEX_SKIP_BWRAP_BUILD in %%build and
# Requires: bubblewrap).
rm -rf codex-rs/vendor
tar -xf %{SOURCE1} -C codex-rs
# Removed from the workspace by Patch0 because they pull in the v8 crate,
# whose build script downloads a prebuilt library from the network.
rm -rf codex-rs/v8-poc codex-rs/code-mode-runtime codex-rs/code-mode-host

%build
# %%cargo_build otherwise fans out one job per CPU, which OOM-kills the build
# on many-core workers. Cap the job count by available memory (paired with
# _constraints). 4000 rather than the usual 2000 because a single rustc here
# wants 4-5 GB: at 2000 an aarch64 worker with 22 GB took -j8 and the kernel
# OOM-killed rustc while compiling codex-tui, whereas -j4 on a 16 GB x86_64
# worker (3.9 GB per job) was fine.
%limit_build -m 4000
# Belt and braces: the bwrap crate is not in codex-cli's dependency graph, but
# should it ever become one, this keeps its build script from compiling and
# bundling a private bubblewrap. The sandbox launcher looks up the system bwrap
# on PATH first (codex-rs/linux-sandbox/src/launcher.rs).
export CODEX_SKIP_BWRAP_BUILD=1
# Upstream's release profile uses thin LTO. Combined with the -C debuginfo=2
# the distribution adds (so find-debuginfo.sh can split out -debuginfo), the
# single LTO rustc peaks at 43 GB RSS here - far beyond what any OBS worker
# offers (chromium, the largest package in Factory, asks for 14 GB). Turning
# LTO off keeps the peak inside a realistic _constraints request; it costs some
# binary size and a little run-time performance.
export CARGO_PROFILE_RELEASE_LTO=off
# Upstream's codegen-units = 4 leaves the final crate as one 33-minute, ~18 GB
# rustc even with LTO off. Cargo's own release default splits it four ways,
# which parallelises that step and brings the peak down to what _constraints
# asks for.
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
cd codex-rs
# Only codex-cli is built: a workspace-wide build would also pull the v8
# crate through the code-mode members, which cannot be built offline.
%{cargo_build} -p codex-cli --bin codex

%install
# Where the binary lands depends on the cargo-packaging version: recent ones
# point CARGO_TARGET_DIR at the top of the build tree, older ones leave cargo
# to use the workspace directory. Accept either rather than guessing.
targetdir=
for d in target codex-rs/target; do
    if test -x "$d/release/codex"; then
        targetdir="$d"
        break
    fi
done
if test -z "$targetdir"; then
    echo "cannot find the built codex binary" >&2
    exit 1
fi
install -D -m 0755 "$targetdir/release/codex" %{buildroot}%{_bindir}/codex

install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d %{buildroot}%{_datadir}/zsh/site-functions
# Generate the completions from the build tree, NOT from the copy already in
# %%{buildroot}: codex is a multicall binary that re-execs itself, and the
# short-lived child keeps the executable open, so find-debuginfo can lose the
# race and abort with "Failed to open input file ...: Text file busy".
"$targetdir/release/codex" completion bash > %{buildroot}%{_datadir}/bash-completion/completions/codex
"$targetdir/release/codex" completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/codex.fish
"$targetdir/release/codex" completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_codex

%check
cd codex-rs
# Deliberately an allowlist rather than --workspace. --workspace cannot be used
# at all: it reaches the members Patch0 removes. Beyond that the choice is one
# of build cost - compiling the test harnesses of core, tui and app-server (the
# three largest crates) roughly doubles a build that already takes over an
# hour, for tests that exercise upstream's own logic rather than anything
# packaging can get wrong. The crates below are the self-contained ones: no
# network, no container, no terminal. The suite's genuinely environment-bound
# tests are #[ignore]d upstream anyway - a live API key for
# core/tests/suite/live_cli.rs, tmux for tui/tests/suite/resize_reflow.rs - and
# the landlock tests self-skip when the kernel lacks support.
# --release reuses the artifacts built in %%build instead of recompiling the
# whole dependency graph with the dev profile.
%{cargo_test} --release -p codex-protocol -p codex-apply-patch \
    -p codex-execpolicy -p codex-file-search -p codex-config

%files
%license LICENSE NOTICE
%doc README.md CHANGELOG.md docs/
%{_bindir}/codex

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/codex

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/codex.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_codex

%changelog
