#
# spec file for package parsec
#
# Copyright (c) 2023 SUSE LLC
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%define archive_version 1.1.0

%{?systemd_ordering}
Name:           parsec
Version:        1.1.0
Release:        0
Summary:        Platform AbstRaction for SECurity
License:        Apache-2.0
URL:            https://parallaxsecond.github.io/parsec-book
Source0:        https://github.com/parallaxsecond/parsec/archive/%{archive_version}.tar.gz#/parsec-%{archive_version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        parsec.service
Source4:        config.toml
Source5:        parsec.conf
Source6:        system-user-parsec.conf
Source10:       https://git.trustedfirmware.org/TS/trusted-services.git/snapshot/trusted-services-389b506.tar.gz
# PATCH-FIX-UPSTREAM - https://github.com/parallaxsecond/parsec/pull/664
Patch1:         664.patch
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  llvm-devel
%if 0%{?sle_version} >= 150400
# Fix build with GCC11 on Backports SLE15-SP4/5 - Avoid to get -lstdc++ not found
BuildRequires:  libstdc++6-devel-gcc11
%endif
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  python3
# jwt-svid-authenticator (SPIFFE-based authenticator) needs rust >= 1.53
BuildRequires:  rust >= 1.53
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(tss2-esys) >= 2.3.3
# opensc is used to initialize HSM keys (PKCS#11 backend)
Recommends:     opensc
%sysusers_requires
# /dev/tpm* are owned by tss user
Requires(pre):  system-user-tss
# tpm2-0-tss holds the udev rule to make /dev/tpm* owned by tss user
Requires:       tpm2-0-tss
# Without libtss2-tcti-device0 parsec fails to start TPM properly
Requires:       libtss2-tcti-device0
ExcludeArch:    %{ix86} armv6l armv6hl

%description
PARSEC is the Platform AbstRaction for SECurity, an open-source initiative to provide
a common API to hardware security and cryptographic services in a platform-agnostic way.
This abstraction layer keeps workloads decoupled from physical platform details,
enabling cloud-native delivery flows within the data center and at the edge.

%prep
%setup -q -a1 -a10 -n parsec-%{archive_version}
%patch1 -p1
rmdir trusted-services-vendor
mv trusted-services-389b506 trusted-services-vendor
rm -rf .cargo && mkdir .cargo
cp %{SOURCE2} .cargo/config
# Enable all providers
sed -i -e 's#default = \["unix-peer-credentials-authenticator"\]##' Cargo.toml
# Features available in 1.0.0:
# all-providers = ["tpm-provider", "pkcs11-provider", "mbed-crypto-provider", "trusted-service-provider"]
# all-authenticators = ["direct-authenticator", "unix-peer-credentials-authenticator", "jwt-svid-authenticator"]
# But disable "trusted-service-provider" until we have a trusted-services package
echo 'default = ["tpm-provider", "pkcs11-provider", "mbed-crypto-provider", "all-authenticators"]' >> Cargo.toml

%build
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_build
%sysusers_generate_pre %{SOURCE6} parsec

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/
install -D -p -m0644 %{SOURCE3} %{buildroot}%{_unitdir}/parsec.service
install -D -p -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/parsec/config.toml
install -D -p -m0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/parsec
# Move parsec to _libexecdir
mkdir -p %{buildroot}%{_libexecdir}
mv target/release/parsec %{buildroot}%{_libexecdir}

# currently delete it from bin if there
rm -f %{buildroot}%{_bindir}/parsec
# Clean-up
find %{buildroot} -name .crates2.json -delete
rm -rf %{buildroot}%{_datadir}/cargo/registry

%check
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_test -- --lib

%pre -f parsec.pre
%service_add_pre parsec.service

%post
%service_add_post parsec.service
%tmpfiles_create %_tmpfilesdir/parsec.conf

%preun
%service_del_preun parsec.service

%postun
%service_del_postun parsec.service

%files
%license LICENSE
%doc README.md config.toml
%attr(0750,parsec,parsec) %dir %{_sysconfdir}/parsec/
%attr(0750,parsec,parsec) %dir %{_localstatedir}/lib/parsec/
%attr(0644,parsec,parsec) %config(noreplace) %{_sysconfdir}/parsec/config.toml
%{_libexecdir}/parsec
%{_tmpfilesdir}/parsec.conf
%{_unitdir}/parsec.service
%{_sysusersdir}/system-user-parsec.conf

%changelog
