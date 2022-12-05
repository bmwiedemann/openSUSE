#
# spec file for package rekor
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


%define apps cli server

Name:           rekor
Version:        1.0.1
Release:        0
%define revision d3162350e96098ca8a24adfdbee42057e43b5de6
Summary:        Supply Chain Transparency Log
License:        Apache-2.0
URL:            https://github.com/sigstore/rekor
Source:         https://github.com/sigstore/rekor/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        rekor-zypper-verify.sh
BuildRequires:  golang-packaging
BuildRequires:  golang(API)
%{go_nostrip}

%description
Rekor's goals are to provide an immutable tamper resistant ledger of metadata generated within a software projects supply chain. Rekor will enable software maintainers and build systems to record signed metadata to an immutable record. Other parties can then query said metadata to enable them to make informed decisions on trust and non-repudiation of an object's lifecycle. For more details visit the sigstore website

The Rekor project provides a restful API based server for validation and a transparency log for storage. A CLI application is available to make and verify entries, query the transparency log for inclusion proof, integrity verification of the transparency log or retrieval of entries by either public key or artifact.

Rekor fulfils the signature transparency role of sigstore's software signing infrastructure. However, Rekor can be run on its own and is designed to be extensible to working with different manifest schemas and PKI tooling.

%prep
%autosetup -p1 -a1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
for app in %{apps} ; do
CLI_PKG=github.com/sigstore/rekor/cmd/rekor-${app}/app
CLI_LDFLAGS="-X ${CLI_PKG}.gitVersion=%{version} -X ${CLI_PKG}.gitCommit=%{revision} -X ${CLI_PKG}.gitTreeState=release -X ${CLI_PKG}.buildDate=${BUILD_DATE}"
go build -mod=vendor -buildmode=pie -ldflags "${CLI_LDFLAGS}" ./cmd/rekor-${app}
./rekor-${app} version
done

%install
for app in %{apps} ; do
install -D -m 0755 rekor-${app} %{buildroot}%{_bindir}/rekor-${app}
done
install -m 0755 %SOURCE2 %{buildroot}%{_bindir}/rekor-zypp-verify

%files
%license LICENSE
%doc *.md
%{_bindir}/rekor-*

%changelog
