#
# spec file for package rustup
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 William Brown <william@blackhats.net.au>
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


%define rust_version 1.56
%define obsolete_rust_versioned() \
Obsoletes:      %{1}1.55%{?2:-%{2}} < %{rust_version} \
Provides:       %{1}1.55%{?2:-%{2}} = %{rust_version} \
Obsoletes:      %{1}1.54%{?2:-%{2}} < %{rust_version} \
Provides:       %{1}1.54%{?2:-%{2}} = %{rust_version} \
Obsoletes:      %{1}1.53%{?2:-%{2}} < %{rust_version} \
Provides:       %{1}1.53%{?2:-%{2}} = %{rust_version} \
Obsoletes:      %{1}1.52%{?2:-%{2}} < %{rust_version} \
Obsoletes:      %{1}1.51%{?2:-%{2}} < %{rust_version}

Name:           rustup
Version:        1.25.2~0
Release:        0
Summary:        A tool for managing user Rust toolchains
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
Group:          Development/Languages/Rust
URL:            https://github.com/rust-lang/rustup
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
Source3:        %{name}-rpmlintrc
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
# For system linker
Requires:       gcc
ExclusiveArch:  %{rust_tier1_arches}

# Rustup now provides rust-analyzer which we take over.
Provides:       rust-analyzer = 2022.09.11
Obsoletes:      rust-analyzer < 2022.09.11

# Ensure we can upgrate from ancient versions of rust that used
# to ship these tools. We can probably remove this in the future.
%obsolete_rust_versioned rls
%obsolete_rust_versioned rust doc
%obsolete_rust_versioned rust src
%obsolete_rust_versioned rust analysis
%obsolete_rust_versioned cargo doc

Obsoletes:      cargo-doc < %{rust_version}
Obsoletes:      cargo-fmt < %{rust_version}
Obsoletes:      clippy < %{rust_version}
Obsoletes:      rls < %{rust_version}
Obsoletes:      rust-analysis < %{rust_version}
Obsoletes:      rust-doc < %{rust_version}
Obsoletes:      rust-src < %{rust_version}
Obsoletes:      rustfmt < %{rust_version}

Conflicts:      rust+cargo
Conflicts:      rust+rustc

%description
A tool to manager user Rust toolchains. This is generally used by developers
managing multiple parallel toolchains in their environment.

%prep
%setup -q
%setup -qa1
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build} --features=no-self-update

%install
# manual process
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/rustup-init %{buildroot}%{_bindir}/rustup
# rustup-init and rustup are the same binary, but that binary behaves
# differently based on the name it's executed by.
# rustup-init takes care of the initial setup, which includes setting PATH,
# modifying .bashrc etc. It's supposed to be called only once.
# rustup doesn't perform those steps and it only manages toolchains. It
# can be used the entire time.
#
# https://github.com/rust-lang/rustup/blob/master/src/lib.rs#L21
ln -sf rustup %{buildroot}%{_bindir}/rustc
ln -sf rustup %{buildroot}%{_bindir}/rustdoc
ln -sf rustup %{buildroot}%{_bindir}/cargo
ln -sf rustup %{buildroot}%{_bindir}/rust-analyzer
ln -sf rustup %{buildroot}%{_bindir}/rust-lldb
ln -sf rustup %{buildroot}%{_bindir}/rust-gdb
ln -sf rustup %{buildroot}%{_bindir}/rust-gdbgui
ln -sf rustup %{buildroot}%{_bindir}/rls
ln -sf rustup %{buildroot}%{_bindir}/cargo-clippy
ln -sf rustup %{buildroot}%{_bindir}/clippy-driver
ln -sf rustup %{buildroot}%{_bindir}/cargo-miri
ln -sf rustup %{buildroot}%{_bindir}/rustfmt
ln -sf rustup %{buildroot}%{_bindir}/cargo-fmt

# shell completions
install -D -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
ls %{buildroot}%{_bindir}
ls %{buildroot}%{_bindir}/rustup

%{buildroot}%{_bindir}/rustup completions bash > %{buildroot}%{_datadir}/bash-completion/completions/rustup
%{buildroot}%{_bindir}/rustup completions bash cargo > %{buildroot}%{_datadir}/bash-completion/completions/cargo
install -D -d -m 0755 %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/rustup completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_rustup
%{buildroot}%{_bindir}/rustup completions zsh cargo > %{buildroot}%{_datadir}/zsh/site-functions/_cargo

%files
%{_bindir}/rustup
# %{_bindir}/rustup-init
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/cargo
%{_bindir}/rust-analyzer
%{_bindir}/rust-lldb
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%{_bindir}/rls
%{_bindir}/cargo-clippy
%{_bindir}/clippy-driver
%{_bindir}/cargo-miri
%{_bindir}/rustfmt
%{_bindir}/cargo-fmt
%{_datadir}/bash-completion/completions/cargo
%{_datadir}/bash-completion/completions/rustup
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cargo
%{_datadir}/zsh/site-functions/_rustup

%changelog
