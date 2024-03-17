#
# spec file for package gitsign
#
# Copyright (c) 2024 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           gitsign
Version:        0.9.0
Release:        0
Summary:        Keyless Git signing using Sigstore
License:        Apache-2.0
URL:            https://github.com/sigstore/gitsign
Source:         gitsign-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Keyless Git signing with Sigstore!

This is heavily inspired by https://github.com/github/smimesign, but uses keyless Sigstore to sign Git commits with your own GitHub / OIDC identity.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/sigstore/gitsign/pkg/version.gitVersion=%{version}" \
   -o bin/gitsign .

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
