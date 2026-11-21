# spec file for package rpmcrab
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). In either case, the license is the
# MIT License.
#
# Please submit bugfixes or comments via https://github.com/plusky/rpmcrab/issues
#

Name:           rpmcrab
Version:        0.4.2
Release:        0
Summary:        Rust rewrite of rpmlint
License:        GPL-2.0-or-later
URL:            https://github.com/plusky/rpmcrab
Source:         https://github.com/plusky/rpmcrab/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Re-vendor per bump with plain `cargo vendor vendor` (unversioned dirs),
# then strip the Windows-only import libraries no Linux target reads:
#   python3 <skill>/scripts/vendor-strip.py vendor.tar.zst -o vendor.tar.zst 'winapi-i686-pc-windows-gnu/lib/**' 'winapi-x86_64-pc-windows-gnu/lib/**'
Source1:        vendor.tar.zst
# Test corpus the suite reads as data, never executed or linked:
# Source-Binary-Exception: rpmcrab-*.tar.gz:*/tests/parity/* -- test-data: parity-test corpus RPMs the checks lint as input, never executed
# Source-Binary-Exception: rpmcrab-*.tar.gz:*/tests/fixtures/* -- test-data: fixture RPMs the tests read as lint input, never executed
# Source-Binary-Exception: vendor.tar.zst:vendor/rpm/tests/* -- test-data: rpm crate testsuite assets, never built or run for the Linux target
# Source-Binary-Exception: vendor.tar.zst:vendor/librpm/testdata/* -- test-data: librpm testsuite distro-RPM fixtures, read only by its own tests
# Source-Binary-Exception: vendor.tar.zst:vendor/libloading/tests/* -- test-data: fixtures loaded only by libloading's Windows-only tests, never on Linux
# Shells own the completion dirs installed below (cf. helm)
BuildRequires:  bash-completion
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  fish
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  zsh
BuildRequires:  zstd
BuildRequires:  pkgconfig(rpm)
# - AppDataCheck: invalid-appdata-file/invalid-metainfo-file via appstream-util
Requires:       appstream-glib
# - PostCheck: scriptlet syntax check via /bin/sh and /bin/bash -n
Requires:       bash
# - BinariesCheck: binary analysis via strings and ar (binutils)
Requires:       binutils
# - FilesCheck: decompression of .bz2 files via bzip2 -dc
Requires:       bzip2
Requires:       checkbashisms
# External tools invoked by checks (see comments for which check needs each):
# - BashismsCheck: bin-sh-syntax-error via dash, potential-bashisms via checkbashisms
Requires:       dash
# - MenuXDGCheck: invalid-desktopfile via desktop-file-validate
Requires:       desktop-file-utils
# - File classification: libmagic description of files via file -b
Requires:       file
# - FilesCheck: decompression of .gz files via gzip -dc
Requires:       gzip
# - SpecCheck: specfile-error/specfile-warning via rpm --specfile
#   (rpm re-execs /usr/bin/rpmspec from rpm-build since rpm 4.9)
Requires:       rpm-build
# - FilesCheck: decompression of .xz files via xz -dc
Requires:       xz
# - FilesCheck: decompression of .zst files via zstd -dc
Requires:       zstd
# - TagsCheck: spelling-error via the en_US hunspell dictionary
Recommends:     myspell-en_US

%description
rpmcrab is a Rust rewrite of rpmlint, the RPM package linter.
It checks RPM packages for common issues and policy violations.

%package bash-completion
Summary:        Bash completion for rpmcrab
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for rpmcrab.

%package zsh-completion
Summary:        Zsh completion for rpmcrab
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for rpmcrab.

%package fish-completion
Summary:        Fish completion for rpmcrab
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for rpmcrab.

%package rpmlint-compat
Summary:        Rpmlint compatibility symlinks for rpmcrab
Requires:       %{name} = %{version}-%{release}
# PolkitCheck reads the standard profile from the installed
# polkit-default-privs data, mirrored from rpmlint-mini
Requires:       polkit-default-privs
Supplements:    (%{name} unless rpmlint)
Conflicts:      rpmlint
Conflicts:      rpmlint-mini
# Drop-in replacement for rpmlint and rpmlint-mini
Provides:       rpmlint
Provides:       rpmlint-mini = 2.10.0+git20261020.513f17e8
BuildArch:      noarch

%description rpmlint-compat
The %{_bindir}/rpmlint compatibility symlink (and its man page) that
makes rpmcrab a drop-in replacement for rpmlint and rpmlint-mini.
Installing this package removes rpmlint.

%prep
%autosetup -a1
# Configure cargo to use vendored sources
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build -- --package rpmcrab

%install
%{cargo_install -p crates/rpmcrab}
install -D -m 644 crates/rpmcrab/man/rpmcrab.1 %{buildroot}%{_mandir}/man1/rpmcrab.1
# Shell completions (from crates/rpmcrab/completions/ in the tarball)
install -D -m 644 crates/rpmcrab/completions/rpmcrab.bash %{buildroot}%{_datadir}/bash-completion/completions/rpmcrab
install -D -m 644 crates/rpmcrab/completions/rpmcrab.zsh %{buildroot}%{_datadir}/zsh/site-functions/_rpmcrab
install -D -m 644 crates/rpmcrab/completions/rpmcrab.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/rpmcrab.fish
# Drop-in symlink for rpmlint compatibility
ln -sf %{_bindir}/rpmcrab %{buildroot}%{_bindir}/rpmlint
ln -sf %{_mandir}/man1/rpmcrab.1%{?ext_man} %{buildroot}%{_mandir}/man1/rpmlint.1%{?ext_man}

%check
%cargo_test

%files
%license LICENSE
%{_bindir}/rpmcrab
%{_mandir}/man1/rpmcrab.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/rpmcrab

%files zsh-completion
%{_datadir}/zsh/site-functions/_rpmcrab

%files fish-completion
%{_datadir}/fish/vendor_completions.d/rpmcrab.fish

%files rpmlint-compat
%{_bindir}/rpmlint
%{_mandir}/man1/rpmlint.1%{?ext_man}

%changelog
