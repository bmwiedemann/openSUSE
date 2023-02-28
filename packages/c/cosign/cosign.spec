#
# spec file for package cosign
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


Name:           cosign
Version:        2.0.0
Release:        0
%define revision 69c9b37f2a021326c67b2aa9552c790e12ae5fb8
Summary:        Container Signing, Verification and Storage in an OCI registry
License:        Apache-2.0
URL:            https://github.com/sigstore/cosign
Source:         https://github.com/sigstore/cosign/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  go1.18
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API)

%description
Cosign aims to make signatures invisible infrastructure.

Cosign supports:

- Hardware and KMS signing
- Bring-your-own PKI
- Our free OIDC PKI (Fulcio)
- Built-in binary transparency and timestamping service (Rekor)

%prep
%autosetup -p1 -a1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

CLI_PKG=github.com/sigstore/cosign/pkg/version
CLI_LDFLAGS="-X ${CLI_PKG}.gitVersion=%{version} -X ${CLI_PKG}.gitCommit=%{revision} -X ${CLI_PKG}.gitTreeState=release -X ${CLI_PKG}.buildDate=${BUILD_DATE}"

go build -mod=vendor -buildmode=pie -ldflags "${CLI_LDFLAGS}" -o cosign ./cmd/cosign
go build -mod=vendor -buildmode=pie -ldflags "${CLI_LDFLAGS}" -o sget ./cmd/sget
./cosign version
./sget version
# ./cosigned version ... wants something kubernetes

%install
install -D -m 0755 cosign %{buildroot}%{_bindir}/cosign
install -D -m 0755 sget %{buildroot}%{_bindir}/sget

%files
%license LICENSE
%doc *.md
%{_bindir}/cosign
%{_bindir}/sget

%changelog
