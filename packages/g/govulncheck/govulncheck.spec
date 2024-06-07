#
# spec file for package govulncheck
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


Name:           govulncheck
Version:        1.1.2
Release:        0
Summary:        CLI tool to report known CVE vulnerabilities in Go source code and binaries
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Languages/Go
URL:            https://github.com/golang/vuln
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18

%description
govulncheck is a CLI tool to report known vulnerabilities that affect Go code. It uses static analysis of source code or a binary's symbol table to narrow down reports to only those that could affect the application.

By default, govulncheck makes requests to the Go vulnerability database at https://vuln.go.dev. Requests to the vulnerability database contain only module paths, not code or other properties of your program. See https://vuln.go.dev/privacy.html for more. Use the -db flag to specify a different database, which must implement the specification at https://go.dev/security/vuln/database.

%prep
%autosetup -a 1

%build
go build \
   -buildmode=pie \
   ./cmd/govulncheck

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
