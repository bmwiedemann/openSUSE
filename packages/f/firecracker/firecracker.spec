#
# spec file for package firecracker
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


# Use hardening ldflags.
%define cargo_home cargo-home

Name:           firecracker
Version:        0.19.1
Release:        0
Summary:        Virtual Machine Monitor for creating microVMs
License:        Apache-2.0
Group:          System/Emulators/PC
URL:            https://firecracker-microvm.github.io/
Source0:        %{name}-%{version}.tar.xz
# Created using cargo_vendor service
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  rust >= 1.35.0
%ifarch aarch64
BuildRequires:  libfdt-devel
%endif
ExclusiveArch:  x86_64 aarch64

%description
Firecracker is a virtualization technology for creating and managing
multi-tenant container and function-based services.

%prep
%setup -q -a1

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
find . -mindepth 1 -maxdepth 1 -exec cp -r {} $HOME/rust/%{name} \;

%build
cd $HOME/rust/%{name}
# This should eventually migrate to distro policy
# Enable optimization, debuginfo, and link hardening.
export CARGO_HOME=`pwd`/%{cargo_home}/

cargo install \
  --path `pwd` \
  --root=%{buildroot}%{_prefix} \
  --target %{_arch}-unknown-linux-gnu

%install
# remove spurious file
rm -f %{buildroot}%{_prefix}/.crates.toml
rm -f %{buildroot}%{_prefix}/.crates2.json

%files
%doc README.md
%{_bindir}/firecracker
%{_bindir}/jailer

%changelog
