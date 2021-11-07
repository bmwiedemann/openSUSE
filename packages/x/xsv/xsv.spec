#
# spec file for package xsv
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           xsv
Version:        0.13.0
Release:        0
Summary:        A fast CSV toolkit written in Rust
License:        MIT OR Unlicense
Group:          Productivity/Text/Utilities
URL:            https://github.com/BurntSushi/xsv/
Source:         https://github.com/BurntSushi/xsv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        xsv.bash
BuildRequires:  cargo
BuildRequires:  pkgconfig
BuildRequires:  rust

%description
xsv is a command line program for indexing, slicing, analyzing,
splitting and joining CSV files.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -qa1
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
export CARGO_HOME=$PWD/cargo-home
cargo build --release --locked %{?_smp_mflags}

%install
export CARGO_HOME=$PWD/cargo-home
cargo install --root=%{buildroot}%{_prefix}
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# remove residue crate file
rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%files
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md
%{_bindir}/xsv

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
