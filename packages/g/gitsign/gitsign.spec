#
# spec file for package gitsign
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


Name:           gitsign
Version:        0.13.0
Release:        0
Summary:        Keyless Git signing using Sigstore
License:        Apache-2.0
URL:            https://github.com/sigstore/gitsign
Source:         gitsign-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        gitsign-credential-cache.service
Source3:        gitsign-credential-cache.socket
BuildRequires:  golang(API) >= 1.23

%description
Keyless Git signing with Sigstore!

This is heavily inspired by https://github.com/github/smimesign, but uses
keyless Sigstore to sign Git commits with your own GitHub / OIDC identity.

%package credential-cache
Summary:        Credential cache for gitsign
Requires:       %{name} = %{version}-%{release}
Provides:       gitsign:%{_bindir}/gitsign-credential-cache

%description credential-cache
This package provides the gitsign-credential-cache binary and systemd
user units for caching Sigstore credentials.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/sigstore/gitsign/pkg/version.gitVersion=%{version}" \
   -o bin/gitsign .

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/sigstore/gitsign/pkg/version.gitVersion=%{version}" \
   -o bin/gitsign-credential-cache ./cmd/gitsign-credential-cache/

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
install -D -m 0755 bin/gitsign-credential-cache "%{buildroot}/%{_bindir}/gitsign-credential-cache"
# systemd user unit files
install -D -m 644 %{SOURCE2} %{buildroot}%{_userunitdir}/gitsign-credential-cache.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_userunitdir}/gitsign-credential-cache.socket
# move README so both READMEs can be packaged
mv cmd/gitsign-credential-cache/README.md cmd/gitsign-credential-cache/README-credential-cache.md

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%pre credential-cache
%service_add_pre gitsign-credential-cache.service gitsign-credential-cache.socket

%post credential-cache
%service_add_post gitsign-credential-cache.service gitsign-credential-cache.socket

%preun credential-cache
%service_del_preun gitsign-credential-cache.service gitsign-credential-cache.socket

%postun credential-cache
%service_del_postun gitsign-credential-cache.service gitsign-credential-cache.socket

%files credential-cache
%doc cmd/gitsign-credential-cache/README-credential-cache.md
%{_bindir}/gitsign-credential-cache
%{_userunitdir}/gitsign-credential-cache.service
%{_userunitdir}/gitsign-credential-cache.socket

%changelog
