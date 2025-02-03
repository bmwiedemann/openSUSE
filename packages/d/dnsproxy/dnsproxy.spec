#
# spec file for package dnsproxy
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dnsproxy
Version:        0.75.0
Release:        0
Summary:        A DNS proxy server
License:        Apache-2.0
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/AdguardTeam/dnsproxy
Source:         dnsproxy-%{version}.tar
Source1:        vendor.tar.zstd
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.23

%description
A DNS proxy server that supports numerous protocols, including
DNS-over-TLS, DNS-over-HTTPS, DNSCrypt, and DNS-over-QUIC. Moreover,
it can work as a DNS-over-HTTPS, DNS-over-TLS or DNS-over-QUIC
server.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# Skip tests which require network
go test -count=1 -short -failfast -shuffle=on -timeout=2m -skip='Test((Udp|Tcp|Tls|Https|Quic|DNSCrypt)Proxy|FilteringHandler|LookupNetIP|ExchangeParallel|Upstream.*|NewUpstreamResolver_validity|Proxy_trustedProxies|ProxyRace|DNSCrypt_Exchange_dialFail|FallbackFromInvalidBootstrap|OneByOneUpstreamsExchange|ExchangeWithReservedDomains|RatelimitingProxy)' ./...

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
