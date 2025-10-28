#
# spec file for package kryoptic
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kryoptic
Version:        1.3.1
Release:        0
Summary:        PKCS #11 software token written in Rust
License:        GPL-3.0-or-later
URL:            https://github.com/latchset/kryoptic
Source0:        %{URL}/releases/download/v%{version}/kryoptic-%{version}.tar.gz
Source1:        %{URL}/releases/download/v%{version}/kryoptic-%{version}.tar.gz.asc
Source2:        vendor.tar.gz
Source3:        %{name}.keyring
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  openssl-devel
BuildRequires:  sqlite3-devel

ExclusiveArch:  %{rust_tier1_arches} riscv64

Requires:       sqlite3

%description
A PKCS #11 software token written in Rust.

%package tools
Requires:       %{name} = %{version}-%{release}
Summary:        Supporting tools for kryoptic software token

%description tools
Supporting tools for kryoptic software token. Most notably a migration tool for
the SoftHSM database.

%prep
%autosetup -a2

%build
%{cargo_build} -F standard,dynamic,pqc --all

%install
%{cargo_install -p tools}
install -Dp -m 0755 target/release/libkryoptic_pkcs11.so %{buildroot}/%{_libdir}/pkcs11/libkryoptic_pkcs11.so
rm -f %{buildroot}/%{_bindir}/conformance
rm -f %{buildroot}/%{_bindir}/kryoptic_init
rm -f %{buildroot}/%{_bindir}/test_signature
mkdir -p %{buildroot}/%{_datadir}/p11-kit/modules/
echo "module: libkryoptic_pkcs11.so" > %{buildroot}/%{_datadir}/p11-kit/modules/kryoptic.module

%check
%{cargo_test}

%files tools
%{_bindir}/softhsm_migrate

%files
%license LICENSE.txt
%doc README.md
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/libkryoptic_pkcs11.so
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%{_datadir}/p11-kit/modules/kryoptic.module

%changelog
