#
# spec file for package goben
#
# Copyright (c) 2021-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           goben
Version:        1.0.2
Release:        0
Summary:        Measure TCP/UDP transport layer throughput between hosts
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://github.com/udhos/goben
#Git-Clone:     https://github.com/udhos/goben.git
Source:         https://github.com/udhos/goben/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.25
BuildRequires:  golang-packaging
BuildRequires:  openssl
%{go_provides}

%description
A tool to measure TCP/UDP transport layer throughput between hosts.

%prep
%autosetup -a 1

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -o goben.bin ./cmd/goben

%install
install -Dm 0755 goben.bin %{buildroot}%{_bindir}/goben

%check
make test

%files
%license LICENSE
%doc README.md
%{_bindir}/goben

%changelog
