#
# spec file for package rustup
#
# Copyright (c) 2021 SUSE LLC
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
Obsoletes:      %{1}1.55%{?2:-%{2}} \
Provides:       %{1}1.55%{?2:-%{2}} \
Obsoletes:      %{1}1.54%{?2:-%{2}} \
Provides:       %{1}1.54%{?2:-%{2}} \
Obsoletes:      %{1}1.53%{?2:-%{2}} \
Provides:       %{1}1.53%{?2:-%{2}} \
Obsoletes:      %{1}1.52%{?2:-%{2}} \
Obsoletes:      %{1}1.51%{?2:-%{2}}

Name:           rustup
Version:        1.24.3~git0.ce5817a9
Release:        0
Summary:        A tool for managing user Rust toolchains
License:        ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR ISC OR MIT ) AND ( Apache-2.0 OR MIT ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT
Group:          Development/Languages/Rust
Url:            https://github.com/rust-lang/rustup
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        %{name}-rpmlintrc
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_tier1_arches}

%obsolete_rust_versioned rls
%obsolete_rust_versioned rust doc
%obsolete_rust_versioned rust src
%obsolete_rust_versioned rust analysis
%obsolete_rust_versioned cargo doc

Obsoletes:      cargo-doc < %{rust_version}
Obsoletes:      rustfmt < %{rust_version}
Obsoletes:      cargo-fmt < %{rust_version}
Obsoletes:      clippy < %{rust_version}
Obsoletes:      rust-analysis < %{rust_version}
Obsoletes:      rls < %{rust_version}
Obsoletes:      rust-src < %{rust_version}
Obsoletes:      rust-doc < %{rust_version}

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

%files
%{_bindir}/rustup

%changelog

