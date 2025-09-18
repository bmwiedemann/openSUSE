#
# spec file for package lego
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


Name:           lego
Version:        4.26.0
Release:        0
Summary:        Let's Encrypt/ACME client and library written in Go
License:        MIT
URL:            https://github.com/go-acme/lego
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
Let's Encrypt/ACME client and library written in Go.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.version=%{version}" \
   -o bin/lego ./cmd/lego

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
cd %{buildroot}/%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
