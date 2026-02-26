#
# spec file for package goreleaser
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


Name:           goreleaser
Version:        2.14.1
Release:        0
Summary:        CLI tool for release engineering in Go, Rust, Zig and TypeScript
License:        MIT
URL:            https://goreleaser.com/
Source:         goreleaser-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.26

%description
CLI tool that provides a single command to build, archive, package, sign and publish artifacts.

%prep
%autosetup -D -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# Tests are currently broken because they require network.
#go test ./...

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}

%changelog
