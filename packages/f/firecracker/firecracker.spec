#
# spec file for package firecracker
#
# Copyright (c) 2022 SUSE LLC
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


# Use hardening ldflags.
%define cargo_home cargo-home

Name:           firecracker
Version:        1.2.0
Release:        0
Summary:        Virtual Machine Monitor for creating microVMs
License:        Apache-2.0
Group:          System/Emulators/PC
URL:            https://firecracker-microvm.github.io/
Source0:        %{name}-%{version}.tar.xz
# Created using cargo_vendor service
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  rust >= 1.46.0
ExclusiveArch:  x86_64 aarch64

%description
Firecracker is a virtualization technology for creating and managing
multi-tenant container and function-based services.

%prep
%setup -q -a1

cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking
find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
mkdir %{cargo_home}
cat > %{cargo_home}/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

# Copying the file elsewhere is required, because rpm build for aarch64
# tries to change all the config.guess files found in BUILD with
# some arch specific stuff.
rm -rf $HOME/rust/%{name}
mkdir -pv $HOME/rust/%{name}

cargo build --offline --all --release \
  --target-dir $HOME/rust/%{name} \
  --target %{_arch}-unknown-linux-gnu

%install
cd $HOME/rust/%{name}
# This should eventually migrate to distro policy
# Enable optimization, debuginfo, and link hardening.

install -D -d -m 0755 %{buildroot}%{_bindir}

install -m 0755 ./%{_arch}-unknown-linux-gnu/release/firecracker %{buildroot}%{_bindir}/firecracker
install -m 0755 ./%{_arch}-unknown-linux-gnu/release/jailer %{buildroot}%{_bindir}/jailer
install -m 0755 ./%{_arch}-unknown-linux-gnu/release/seccompiler-bin %{buildroot}%{_bindir}/seccompiler-bin

%files
%doc README.md
%{_bindir}/firecracker
%{_bindir}/jailer
%{_bindir}/seccompiler-bin

%changelog
