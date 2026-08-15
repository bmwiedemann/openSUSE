#
# spec file for package python-uv
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%global debug_package %{nil}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define origname python-uv
%if 0%{?suse_version} >= 1699
%bcond_without mold
%else
%bcond_with    mold
%endif
%bcond_without libalternatives
%if %{with mold}
%global build_rustflags -C linker=clang -C link-arg=-fuse-ld=%{_bindir}/mold -C link-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C incremental=false -C strip=none
%endif
Name:           %{origname}%{psuffix}
Version:        0.12.5
Release:        0
Summary:        A Python package installer and resolver, written in Rust
# Legal-Review-Notice: uv itself is "Apache-2.0 OR MIT", but the binary
# statically links the vendored Rust dependencies. Re-derived on this
# re-vendor with "cargo tree --offline -p uv -e normal" over the vendored
# tree (512 crates); the copyleft licences in the linked graph are:
#  - MPL-2.0 from astral-pubgrub, astral-version-ranges and option-ext
#    (the last via shellexpand -> dirs -> dirs-sys),
#  - priority-queue, which is "LGPL-3.0-or-later OR MPL-2.0" - we elect
#    MPL-2.0, so no LGPL obligation is taken on.
# configparser is "MIT OR LGPL-3.0-or-later" and we elect MIT; r-efi
# offers an LGPL-2.1-or-later option but is UEFI-target-only and absent
# from the Linux graph; colored is not in this binary's graph at all.
# Everything else is permissive. MPL-2.0 section 3.2 is satisfied because
# the complete vendor.tar.zst ships in the src.rpm.
License:        (Apache-2.0 OR MIT) AND MPL-2.0
URL:            https://github.com/astral-sh/uv
Source0:        https://github.com/astral-sh/uv/archive/refs/tags/%{version}.tar.gz#/%{origname}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.95
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  zstd
%if %{with test}
# A stock build chroot has no /etc/ssl/certs at all, and reqwest's
# ClientBuilder refuses to build with no trust anchors at all
# ("No CA certificates were loaded from the system"). That is a
# constructor error, not a network one, so it took out 38 tests across
# uv-auth, uv-client and uv-test that never touch the network.
BuildRequires:  ca-certificates-mozilla
%endif
# The test flavour only builds and runs the Rust test suite. It needs no
# Python at all, so it skips the singlespec machinery entirely - running
# cargo test once per Python flavour would double the cost for no gain.
# Every Provides/Obsoletes and every %%package declaration is guarded, not
# just the %%files: rpmbuild would drop a subpackage that has no %%files,
# but OBS parses the declarations for scheduling, so an unguarded one
# would advertise a competing provider of uv from the test flavour.
%if %{without test}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python3
Obsoletes:      uv < %{version}
Provides:       uv = %{version}
%endif
%if 0%{?suse_version} >= 1699
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  clang
BuildRequires:  mold
%else
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
BuildRequires:  libstdc++6-devel-gcc13
%endif
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%if %{without test}
%package        -n uv-fish-completion
Summary:        Fish Completion for %{name}
Requires:       fish
Requires:       uv
Supplements:    (uv and fish)
Provides:       python-uv-fish-completion = %{version}
BuildArch:      noarch

%description    -n uv-fish-completion
Fish command-line completion support for %{name}.

%package        -n uv-zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       uv
Requires:       zsh
Supplements:    (uv and zsh)
Provides:       python-uv-zsh-completion = %{version}
BuildArch:      noarch

%description    -n uv-zsh-completion
Zsh command-line completion support for %{name}.

%package        -n uv-bash-completion
Summary:        Bash Completion for %{name}
Requires:       bash-completion
Requires:       uv
Supplements:    (uv and bash-completion)
Provides:       python-uv-bash-completion = %{version}
BuildArch:      noarch

%description    -n uv-bash-completion
Bash command-line completion support for %{name}.

%python_subpackages
%endif

%description
uv is a Python package installer and resolver, written in Rust. Designed as a
drop-in replacement for common pip and pip-tools workflows.

%prep
%autosetup -p1 -a1 -n uv-%{version}
%ifnarch x86_64
# Reduce memory consumption for non x86 arches
sed -i '/lto = "fat"/d' Cargo.toml
%endif

%build
%if %{without test}
export CARGO_AUDITABLE="auditable"
export CARGO_INCREMENTAL=0
export CARGO_FEATURE_VENDORED=1
export RUSTFLAGS="%{build_rustflags}"
export CARGO_NET_OFFLINE=true
%ifarch %{arm} %{ix86}
# Debuginfo needs too much memory for 32-bit architectures.
export CARGO_PROFILE_RELEASE_DEBUG=none
export RUSTFLAGS="%{build_rustflags} -C debuginfo=0"
%else
export CARGO_PROFILE_RELEASE_DEBUG=full
%endif
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_wheel
%endif

%if %{with test}
%check
# The test flavour runs the Rust workspace suite: 67 of the 70 workspace
# members. Three crates are excluded, each for a reason that no amount of
# packaging can fix:
#  - uv, the CLI integration suite (78 test files under crates/uv/tests).
#    It resolves against the real package index and downloads managed
#    CPython interpreters; an OBS build chroot has no network.
#  - uv-dev, whose generate_sysconfig_mappings test fetches
#    cpython-unix/targets.yml from raw.githubusercontent.com - same
#    reason.
#  - uv-build-backend, which panics inside insta with "does not allow
#    inline snapshot assertions in loops". Upstream ships
#    .config/nextest.toml and runs the suite under cargo-nextest, which
#    gives every test its own process; insta's duplicate detection is
#    process-global, so a shared inline snapshot trips under plain
#    cargo test. --test-threads=1 does not help.
# Everything else is offline by construction: those crates carry only
# inline #[test] units (version parsing, PEP 508, resolver, wheel
# filenames, ...) against the vendored dev-dependencies. Two crates that
# look like they need more than that do not: uv-client's four pypi.org
# tests are behind the non-default test-pypi feature, and both of
# uv-keyring's integration test files are gated on
# #![cfg(feature = "native-auth")], also not a default feature, so they
# compile to zero tests and need no secret-service daemon.
#
# --test-threads=1 is not tuning, it is required for correctness. Several
# crates drive process-global state from their tests: uv-client's tls.rs
# points SSL_CERT_FILE/SSL_CERT_DIR at deliberately bogus paths through
# temp_env while base_client.rs builds a reqwest Client that reads them,
# and uv-python's discovery tests rewrite PATH while another test spawns
# a /bin/sh mock interpreter that then cannot find cat. Upstream never
# sees either because cargo-nextest gives every test its own process;
# one test thread is the equivalent for the stock harness.
#
# The single skip is environmental: linehaul reports the distro from
# /etc/os-release, which a build chroot does not have, so the snapshot
# gets null where it expects a name and version.
#
# The leading "--" is required: %%cargo_test is a parametrised macro, so
# without it rpm parses "--workspace" as a macro option and aborts.
%{cargo_test -- --workspace --exclude uv --exclude uv-dev --exclude uv-build-backend -- --test-threads=1 --skip user_agent_version::test_user_agent_has_linehaul}
%endif

%if %{without test}
%install
export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
export CARGO_AUDITABLE="auditable"
export CARGO_INCREMENTAL=0
export CARGO_FEATURE_VENDORED=1
export RUSTFLAGS="%{build_rustflags}"
export CARGO_NET_OFFLINE=true
%ifarch %{rust_tier1_arches}
export CARGO_PROFILE_RELEASE_DEBUG=full
%else
export CARGO_PROFILE_RELEASE_DEBUG=limited
%endif
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/uv
%python_group_libalternatives uv
%python_clone -a %{buildroot}%{_bindir}/uvx
%python_group_libalternatives uvx

%python_expand uv-%{$python_bin_suffix} --generate-shell-completion bash > %{buildroot}%{_datadir}/bash-completion/completions/uv
%python_expand uv-%{$python_bin_suffix} --generate-shell-completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/uv.fish
%python_expand uv-%{$python_bin_suffix} --generate-shell-completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_uv
%python_expand uv-%{$python_bin_suffix} tool uvx --generate-shell-completion bash > %{buildroot}%{_datadir}/bash-completion/completions/uvx
%python_expand uv-%{$python_bin_suffix} tool uvx --generate-shell-completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/uvx.fish
%python_expand uv-%{$python_bin_suffix} tool uvx --generate-shell-completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_uvx

%pre
%python_libalternatives_reset_alternative uv
%python_libalternatives_reset_alternative uvx

%files %{python_files}
%license LICENSE-*
%doc README.md
%python_alternative %{_bindir}/uv
%python_alternative %{_bindir}/uvx
%{python_sitearch}/uv
%{python_sitearch}/uv-%{version}.dist-info

%files -n uv-bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/uv
%{_datadir}/bash-completion/completions/uvx

%files -n uv-fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/uv.fish
%{_datadir}/fish/vendor_completions.d/uvx.fish

%files -n uv-zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_uv
%{_datadir}/zsh/site-functions/_uvx
%endif

%changelog
