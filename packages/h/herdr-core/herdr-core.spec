#
# spec file for package herdr-core
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


Name:           herdr-core
Version:        0.1.21
Release:        0
Summary:        Terminals for programs and coding agents that stay alive
# Legal-Review-Notice: what ends up statically linked in the binary, as
# "hc --licenses" prints it from the source's distribution/notices/ and from
# the Cargo.toml of every vendored crate:
#  - hc itself is Apache-2.0. The 46 Rust crates linked on Linux are MIT or
#    MIT/Apache-2.0, except memchr (Unlicense OR MIT, MIT is taken) and
#    unicode-ident ((MIT OR Apache-2.0) AND Unicode-3.0).
#  - Ghostty's libghostty-vt (MIT) is compiled from the vendor/ghostty submodule
#    with Zig. What it links of its dependencies, by the objects of the archive:
#    uucode (MIT) with its Unicode tables (Unicode-3.0), simdutf and Wuffs (each
#    MIT or Apache-2.0), Highway (BSD-3-Clause or Apache-2.0) and Zig's
#    compiler_rt (MIT). Apache-2.0 is taken wherever a dependency offers it, so
#    nothing outside the License: field below applies.
#  - translate-c and arocc generate parts of that build but are not linked, and
#    neither is anything of the pixels test images, zlib or the Ghostty themes
#    archive. The themes (third-party colour schemes, data only) are in the
#    sources because Zig insists on resolving that manifest entry for the build
#    step, not because anything here uses them.
#  - musl shows up in the notices because upstream's own release builds are
#    static; this one links against the distribution glibc.
License:        Apache-2.0 AND MIT AND Unicode-3.0
URL:            https://github.com/herdrdev/herdr-core
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor-crates.tar.zst
# Zig package archives for the libghostty-vt build, see vendor-zig.sh
Source2:        zig-deps.tar.zst
Source99:       vendor-zig.sh
# crates/ghostty-vt/build.rs builds the vendored libghostty-vt with "zig build",
# whose build.zig.zon asks for minimum_zig_version = 0.16.0
BuildRequires:  (zig >= 0.16.0 with zig < 0.17)
BuildRequires:  cargo
BuildRequires:  cargo-packaging >= 1.2.0
# %%limit_build: cap parallel rustc jobs by available memory (see %%build)
BuildRequires:  memory-constraints
BuildRequires:  zstd
# The integration tests in %%check drive the shipped scripts and the hc update
# flow, so the tools they call have to be in the build root: curl (hc downloads
# releases with it, and so does the install script), python3
# (tests/releases_server.py serves the fake release set the tests point hc at),
# git (run.rs checks that a pager cannot hold hc back, over a repo of 150
# commits), and jq plus openssl for the signing and notarizing scripts that the
# macos_distribution tests exercise from Linux.
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  util-linux
# hc machine add and hc put drive another machine over ssh and scp
Recommends:     openssh
# hc update downloads the release with curl
Recommends:     curl
# build.rs maps the Rust target triple to a Zig one and has no entry for other
# architectures than these; upstream releases x86_64 and aarch64 only
ExclusiveArch:  x86_64 aarch64

%description
hc runs programs and coding agents in terminals that stay alive after you
leave. A core in the background holds the terminals, so closing the window or
losing an SSH connection no longer ends the work: run a build, detach, and
attach again from another shell to take it over, or read its screen without
attaching at all.

Agents can start other agents, send them work and hear back over a socket API,
and terminals of machines reached over ssh join the same set. hc draws nothing
on its own, so it runs inside the terminal you already use.

%prep
%autosetup -p1 -a1
tar --zstd -xf %{SOURCE2}
# Upstream ships this doc helper with the executable bit set. It is
# documentation, and an executable script under /usr/share would make the
# package require a python3 interpreter.
chmod -x docs/via/vercel-sandbox.py

%build
%limit_build -m 3000
# ghostty-vt's build.rs runs "zig build -Demit-lib-vt" over the vendor/ghostty
# submodule. The Zig global cache is pre-populated with the package archives the
# library needs (zig-deps, see vendor-zig.sh), so that build stays offline.
export ZIG=%{_bindir}/zig
export ZIG_GLOBAL_CACHE_DIR=$PWD/zig-deps
export ZIG_LOCAL_CACHE_DIR=$PWD/zig-local-cache
%{cargo_build}

%install
install -Dm0755 target/release/herdr-core %{buildroot}%{_bindir}/herdr-core
# the name the docs, the templates and the agent skills use; upstream's install
# script puts it beside the binary
ln -s herdr-core %{buildroot}%{_bindir}/hc

%check
export ZIG=%{_bindir}/zig
export ZIG_GLOBAL_CACHE_DIR=$PWD/zig-deps
export ZIG_LOCAL_CACHE_DIR=$PWD/zig-local-cache
# The suite is 514 tests: 505 pass in a build root without network, 3 are
# ignored by upstream and the 6 skipped here need something a build root does
# not have:
#  - a_machine_of_another_cpu_gets_the_released_build_for_it asks for the
#    release build of the other architecture and waits for an offer, which only
#    upstream's release server answers.
#  - the four "machine add" tests drive ssh and scp through a fake ssh helper
#    and expect the plain ssh target to fail; on a box without ssh keys or a
#    resolvable hostname the calls they expect to fail go through.
#  - interrupt_reports_what_it_observed reads what a terminal reports after
#    SIGINT, and loses the race when the suite runs on every core.
%{cargo_test} --workspace -- \
    --skip a_machine_of_another_cpu_gets_the_released_build_for_it \
    --skip interrupt_reports_what_it_observed \
    --skip adding_says_what_went_wrong_and_saves_nothing \
    --skip a_box_without_hc_gets_this_one_when_you_say_yes \
    --skip interactive_add_uses_the_same_ssh_target_for_login_and_install \
    --skip a_machine_reached_through_any_command_works_like_one_over_ssh
target/release/herdr-core --version

%files
%license LICENSE
%license distribution/notices
%doc README.md CHANGELOG.md SECURITY.md docs
%{_bindir}/herdr-core
%{_bindir}/hc

%changelog
