#
# spec file for dnsproxy
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


Name:           dnsproxy
Version:        0.49.1
Release:        0
Summary:        A DNS proxy server
License:        Apache-2.0
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/AdguardTeam/dnsproxy
Source:         dnsproxy-%{version}.tar
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
%{go_nostrip}

%description
A DNS proxy server that supports numerous protocols, including
DNS-over-TLS, DNS-over-HTTPS, DNSCrypt, and DNS-over-QUIC. Moreover,
it can work as a DNS-over-HTTPS, DNS-over-TLS or DNS-over-QUIC
server.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
