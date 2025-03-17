#
# spec file for package yq
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


%global provider_prefix github.com/openrdap/rdap
%global import_path     %{provider_prefix}

Name:           rdap
Version:        0.9.1
Release:        0
Summary:        RDAP command line client
License:        MIT
URL:            https://github.com/openrdap/rdap
Source0:        https://github.com/openrdap/rdap/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
OpenRDAP is an command line Registration Data Access Protocol (RDAP) client implementation in Go.
Supports all RDAP query types (domain, ip, asn, help, nameserver, and searches).
Automatic query type detection (domain, ip, asn queries).
Full bootstrapping support (using data.iana.org, or a custom URL).

%prep
%setup -qa1

%build
go build -trimpath -buildmode=pie -mod=vendor ./cmd/%{name}

%check
go test ./...

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
