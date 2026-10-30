#
# spec file for package herdr
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


Name:           herdr
Version:        0.9.5
Release:        0
Summary:        Terminal workspace manager for AI coding agents
# Legal-Review-Notice: licences of what is statically linked into the binary.
#  - Rust crates, from "cargo tree -p herdr -e normal --target x86_64-unknown-linux-gnu"
#    (221 entries) against the vendored Cargo.toml files: all permissive, the
#    non-default ones being 0BSD (doctest-file), Zlib (foldhash) and Unicode-3.0
#    (unicode-ident). No copyleft crate is linked.
#  - The vendored libghostty-vt (MIT) and the Zig packages it is built from,
#    all permissive: uucode (MIT), highway (Apache-2.0 or BSD-3-Clause),
#    simdutf and wuffs (each Apache-2.0 or MIT). translate-c, arocc and the
#    pixels test images take part in the build only and are not linked.
#  - portable-pty is vendored under vendor/ and is MIT.
#  - assets/sounds/{done,request}.mp3 are embedded in the binary; upstream
#    states no separate licence for them, so they are covered by its Apache-2.0.
License:        Apache-2.0 AND MIT AND 0BSD AND Unicode-3.0 AND Zlib
URL:            https://github.com/herdrdev/herdr
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-crates.tar.zst
# Zig package archives for the libghostty-vt build, see vendor-zig.sh
Source2:        zig-deps.tar.zst
Source99:       vendor-zig.sh
# PATCH-FEATURE-OPENSUSE 0001-disable-background-update-checks-by-default.patch -- no herdr.dev requests unless the user opts in
Patch0:         0001-disable-background-update-checks-by-default.patch
# crates/ghostty-vt/build.rs builds the vendored libghostty-vt with "zig build"
# and upstream requires exactly the 0.16 series
BuildRequires:  (zig >= 0.16.0 with zig < 0.17)
BuildRequires:  cargo
BuildRequires:  cargo-packaging >= 1.2.0
# %%limit_build: cap parallel rustc jobs by available memory (see %%build)
BuildRequires:  memory-constraints
BuildRequires:  zstd
# git for worktrees and branch display, ssh for remote machines
Recommends:     git-core
Recommends:     openssh-clients
# build.rs maps the Rust target to a Zig one and has no entry for the others
ExclusiveArch:  x86_64 aarch64

%description
herdr is a terminal workspace manager for AI coding agents. It keeps agent
terminals running in a background server so a session survives closing the
client or losing an SSH connection, marks every pane as working, blocked or
idle, combines local and remote machines in one window, and lets agents drive
it through a command line interface and a socket API.

It runs on top of the terminal already in use and does not wrap or replace
the agents it hosts.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional package supplying bash command completion for herdr.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional package supplying zsh command completion for herdr.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Optional package supplying fish command completion for herdr.

%prep
%autosetup -p1 -a1
tar --zstd -xf %{SOURCE2}
# Upstream pins an exact toolchain through rustup; use the distribution one.
rm -f rust-toolchain.toml

%build
%limit_build -m 3000
# ghostty-vt's build.rs runs "zig build" for the vendored libghostty-vt. The
# Zig global cache is pre-populated with the package archives it needs
# (zig-deps), so the build stays offline.
export ZIG=%{_bindir}/zig
export ZIG_GLOBAL_CACHE_DIR=$PWD/zig-deps
export ZIG_LOCAL_CACHE_DIR=$PWD/zig-local-cache
%{cargo_build}

%install
install -Dm0755 target/release/herdr %{buildroot}%{_bindir}/herdr
install -d %{buildroot}%{_datadir}/bash-completion/completions \
           %{buildroot}%{_datadir}/zsh/site-functions \
           %{buildroot}%{_datadir}/fish/vendor_completions.d
target/release/herdr completion bash > %{buildroot}%{_datadir}/bash-completion/completions/herdr
target/release/herdr completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_herdr
target/release/herdr completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/herdr.fish

%check
# Only the configuration unit tests run: most of the remaining suite needs git,
# agent CLIs, network access or a real terminal and fails in the build sandbox.
export ZIG=%{_bindir}/zig
export ZIG_GLOBAL_CACHE_DIR=$PWD/zig-deps
export ZIG_LOCAL_CACHE_DIR=$PWD/zig-local-cache
%{cargo_test} --bin herdr config::model::tests
target/release/herdr --version
# the update checks stay off by default (0001-disable-background-update-checks-by-default.patch)
target/release/herdr --default-config | grep -q '^# version_check = false'

%files
%license LICENSE
%doc README.md
%{_bindir}/herdr

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/herdr

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_herdr

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/herdr.fish

%changelog
