#
# spec file for package vexctl
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


Name:           vexctl
Version:        0.3.0
Release:        0
Summary:        CLI tool to create, transform and attest VEX metadata 
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/openvex/vexctl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
vexctl is a CLI tool to create, apply, and attest VEX (Vulnerability
Exploitability eXchange) data. Its purpose is to help with the creation and
management of VEX documents that allow "turning off" security scanner alerts of
vulnerabilities known not to affect a product.

VEX can be thought of as a "negative security advisory". Using VEX, software
authors can communicate to their users that an otherwise vulnerable component
has no security implications for their product.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{name} --help

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
