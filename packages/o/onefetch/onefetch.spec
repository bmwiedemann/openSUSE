#
# spec file for package onefetch
#
# Copyright (c) 2020 SUSE LLC
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


Name:           onefetch
Version:        2.5.0
Release:        0
Summary:        Git repository summary on your terminal
License:        MIT AND GPL-2.0-only
Group:          System/X11/Terminals
URL:            https://github.com/o2sh/onefetch
Source0:        https://github.com/o2sh/onefetch/archive/v%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  rust

%description
Onefetch is a command line tool that displays information about your Git repository directly on your terminal.

%prep
%setup -q
%setup -q -D -T -a 1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
# bypass error https://bugzilla.opensuse.org/show_bug.cgi?id=1175502
# to avoid cargo reported error if config.guess has been changed
# by build macro.
%ifarch ppc64le
guessname='src/libbacktrace/config.guess'
cfgguess="./vendor/backtrace-sys/$guessname"
chkjson='./vendor/backtrace-sys/.cargo-checksum.json'
if [[ -f $cfgguess ]] && [[ -f $chkjson ]]; then
  chksum=`sha256sum $cfgguess |sed -e 's/ .*//'`
  grep -q $guessname $chkjson && grep -q $chksum $chkjson || sed -i -e "s#\($guessname.:.\)[0-9a-f]*#\1$chksum#" $chkjson
fi
%endif
cargo build --release %{?_smp_mflags}

%check
cargo test --release %{?_smp_mflags}

%install
install -Dm0755 target/release/onefetch %{buildroot}%{_bindir}/onefetch

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/onefetch

%changelog
