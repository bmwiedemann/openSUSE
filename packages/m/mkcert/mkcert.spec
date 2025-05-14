#
# spec file for package mkcert
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

Name:           mkcert
Version:        1.4.4
Release:        0
Summary:        CLI tool for making locally-trusted development certificates
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/FiloSottile/mkcert
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18
Requires:       mozilla-nss-tools

%description
mkcert is a simple tool for making locally-trusted development certificates.
It requires no configuration.

Using certificates from real certificate authorities (CAs) for development can
be dangerous or impossible (for hosts like example.test, localhost or
127.0.0.1), but self-signed certificates cause trust errors. Managing your own
CA is the best solution, but usually involves arcane commands, specialized
knowledge and manual steps.

mkcert automatically creates and installs a local CA in the system root store,
and generates locally-trusted certificates. mkcert does not automatically
configure servers to use the certificates, though, that's up to you.

Warning: the rootCA-key.pem file that mkcert automatically generates gives
complete power to intercept secure requests from your machine. Do not share it.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
